# <Client> marketing

Private working repository for <Client>, used by the marketing-agent plugin's
director (`/team`). One repository per client: never mix clients here.

## What lives here

- `.marketing-client.yaml`: marks the repository as dedicated to this client.
  The director checks it before writing a job.
- `brand/terms.txt` and `brand/terms-<product>.txt`: locked brand and product
  terms, checked by `check_rules.py --terms`.
- `brand/learnings.md`: what has worked, with numbers; read into every brief.
- `brand/voice-examples.md`: approved and rejected lines per channel, with why.
- `brand/linkedin-templates/`: the account's own Campaign Manager bulk templates.
- `jobs/<YYYY-MM-DD>-<job-slug>/`: one folder per job, with `brief.md`,
  `plan.md`, `decisions.md`, `research/` and `deliverables/`.
- `assets.md`: links to design files in Canva, Figma, Affinity or the drive.

## What does not live here

- Design source files, video and large images: keep them in their own tool or
  on the drive and link them in `assets.md`.
- Passwords, API keys, account exports with personal data.
- Anything from another client.

## How work flows

1. Each job runs on its own branch, `job/<YYYY-MM-DD>-<job-slug>`.
2. The director commits after each step and pushes only when that was agreed at
   the start of the job.
3. A pull or merge request is opened on request; merging is the owner's call.
4. Nothing goes live from here: publishing waits for an explicit yes.

Started from `templates/client-repo/` in the marketing-agent repository.
