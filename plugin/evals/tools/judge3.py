#!/usr/bin/env python3
"""Three-state judge for subjective eval graders: PASS, FAIL or UNSURE.

The built-in LLM grader is binary. For judgement calls (for example "is this claim about 90% likely
to be true?") a wrong FAIL wastes time and a wrong PASS hides a problem, so this helper adds UNSURE.
UNSURE means the person operating the chat should decide.

Usage: judge3.py RESULT.json GRADERS_DIR [grader-name ...]
  RESULT.json   file written by `claude plugin eval ... --json`
  GRADERS_DIR   folder with the grader .md files (frontmatter, then the rubric)
  grader names  llm graders to re-judge (default: every llm grader in RESULT.json)
Objective graders (skill fired, regex, steps ran) stay with the harness.
"""
import json, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ASK = ("Answer with exactly one first word: PASS, FAIL or UNSURE. Use PASS only when the rubric is clearly "
       "met, FAIL only when it is clearly broken, and UNSURE when the answer depends on a judgement call a "
       "human should make. Then give at most 40 words, naming the quote that decides it.")

def rubric(path):
    return open(path).read().split('---\n', 2)[2].strip()

def judge(prompt):
    out = subprocess.run(['claude', '-p', '--model', 'sonnet'], input=prompt, capture_output=True, text=True).stdout.strip()
    word = out.split()[0].strip('*:.,').upper() if out else 'UNSURE'
    return (word if word in ('PASS', 'FAIL', 'UNSURE') else 'UNSURE'), out

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    data = json.load(open(sys.argv[1])); gdir = sys.argv[2]
    runs = data['cases'][0]['arms']['with']
    names = sys.argv[3:] or sorted({g['name'] for r in runs for g in r['graders'] if g.get('type') == 'llm' or 'judgeVotes' in g})
    jobs = []
    for i, r in enumerate(runs):
        evidence = next((g.get('evidence') for g in r['graders'] if g.get('evidence')), '')
        for n in names:
            prompt = f"Rubric:\n{rubric(f'{gdir}/{n}.md')}\n\nOutput to judge:\n<<<\n{evidence}\n>>>\n\n{ASK}"
            jobs.append((i + 1, n, prompt))
    with ThreadPoolExecutor(4) as ex:
        results = list(ex.map(lambda j: judge(j[2]), jobs))
    tally = {}
    for (i, n, _), (verdict, text) in zip(jobs, results):
        tally.setdefault(n, {'PASS': 0, 'FAIL': 0, 'UNSURE': 0})[verdict] += 1
        print(f'run {i} {n}: {verdict}  {text[len(verdict):].strip()[:160]}')
    print()
    for n, t in tally.items():
        print(f'{n}: PASS {t["PASS"]}  FAIL {t["FAIL"]}  UNSURE {t["UNSURE"]}  (UNSURE needs the person operating the chat)')

if __name__ == '__main__':
    main()
