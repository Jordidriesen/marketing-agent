#!/usr/bin/env python3
"""Report what a skill run loads: skill bodies and files read, with sizes and a rough token estimate.

Usage: loadreport.py PLUGIN_DIR RESULT.json [RESULT.json ...]
  PLUGIN_DIR    the plugin folder the eval ran against (to measure file sizes)
  RESULT.json   files written by `claude plugin eval ... --keep-temp --json`

Reads each run's trace, counts Skill calls (the body of that skill's SKILL.md is loaded) and Read calls
(the file is loaded), and sums the bytes. Tokens are estimated as bytes / 4. Agent calls are listed but
their inner loads are not counted.
"""
import json, os, sys

def size(path):
    try:
        return os.path.getsize(path)
    except OSError:
        return 0

def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    plugin = sys.argv[1]
    for result in sys.argv[2:]:
        data = json.load(open(result))
        name = data['cases'][0]['name']
        runs = data['cases'][0]['arms']['with']
        totals = []
        print(f'## {name} ({len(runs)} runs)')
        for i, run in enumerate(runs, 1):
            skills, reads, agents = [], [], 0
            try:
                for line in open(run['tracePath']):
                    try:
                        event = json.loads(line)
                    except ValueError:
                        continue
                    content = (event.get('message') or {}).get('content')
                    if not isinstance(content, list):
                        continue
                    for block in content:
                        if not (isinstance(block, dict) and block.get('type') == 'tool_use'):
                            continue
                        inp = block.get('input') or {}
                        if block['name'] == 'Skill':
                            skills.append(str(inp.get('skill', '')).split(':')[-1])
                        elif block['name'] == 'Read':
                            reads.append(str(inp.get('file_path', '')))
                        elif block['name'] == 'Agent':
                            agents += 1
            except OSError:
                print(f'  run {i}: trace not found'); continue
            skill_bytes = sum(size(f'{plugin}/skills/{s}/SKILL.md') for s in skills)
            read_bytes = 0
            for r in reads:
                rel = r.split('/skills/', 1)[-1] if '/skills/' in r else r
                read_bytes += size(r) or size(f'{plugin}/skills/{rel}')
            total = skill_bytes + read_bytes
            totals.append(total)
            print(f'  run {i}: skills {skills} = {skill_bytes} B; reads {len(reads)} = {read_bytes} B; agents {agents}; total {total} B (~{total // 4} tokens)')
            for r in reads:
                print(f'      read {r.split("/skills/", 1)[-1]}')
        if totals:
            avg = sum(totals) // len(totals)
            print(f'  average {avg} B (~{avg // 4} tokens)\n')

if __name__ == '__main__':
    main()
