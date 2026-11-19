# Storage: where a job lives

Resolve this once at the start of every job that opens a job folder, before
`brief.md` is written. One-step jobs that skip the folder skip this too.

## Order

1. **A linked local folder.** If the session has a folder linked (Cowork, the
   desktop app, or a local Claude Code session started in a client folder), the
   storage root is that folder. Jobs go in `marketing-jobs/<brand>/` inside it.
   This is the default.
2. **No linked folder: a dedicated client repository.** GitHub or GitLab. The
   storage root is the repository root; jobs go in `jobs/`. Use it only when
   every check below passes.
3. **Neither.** Write no files: no job folder in the session's working
   directory or a scratch folder. Do the thinking anyway: give the brief (in the
   `brief.md` template) and the step plan (in the `plan.md` template) in the
   reply, marked as not saved, then send the reminder below and wait. Once
   storage is resolved, write both files unchanged unless the user changed
   something, and carry on.

The session's working directory is never a storage root by default. In a cloud
session it is usually the plugin repository, which is public: client material
written there could be committed and published.

## Checks for a client repository

All four must pass. Say which one failed and stop if any does.

| Check | How |
|---|---|
| Not a plugin or tooling repository | The remote is not `marketing-agent` or another plugin repository, and the root has no `plugin/` or `.claude-plugin/` folder |
| Dedicated to this client | `.marketing-client.yaml` at the root, and its `brand` matches the job's brand kit |
| Private | GitHub: read the repository's visibility through the GitHub tools. GitLab: this cannot be checked from here, so ask the user to confirm once and log the answer in `decisions.md` |
| Reachable | The repository is cloned in this session and `git status` works |

GitLab works in a local session through plain git. Whether a cloud session can
attach a GitLab repository is not confirmed; if it cannot, say so and ask for a
linked local folder or the GitHub mirror instead.

## The reminder

When step 3 applies, end the reply with the brief and plan above it, then this,
and wait:

> Nothing is saved yet: no local folder is linked and no dedicated client repository is connected for <brand>. Link a local folder, or connect the private repository for <brand> (GitHub or GitLab), and I'll save the brief and plan there and carry on. A new client repository can start from `templates/client-repo/` in the marketing-agent repository.

When a repository is connected but a check fails, name the check instead, for
example: "This repository has no `.marketing-client.yaml`, so I can't confirm it
belongs to <brand>."

## Layout of a client repository

Template: `templates/client-repo/` in the marketing-agent repository.

```
.marketing-client.yaml   brand, client, brand kit, owner
README.md                what lives here and what does not
.gitignore               design source files, large exports, secrets
brand/terms.txt          brand terms; brand/terms-<product>.txt per product
jobs/<YYYY-MM-DD>-<job-slug>/
  brief.md  plan.md  decisions.md  research/  deliverables/
assets.md                links to Canva, Figma, Affinity and drive files
```

In a linked local folder the same layout sits under `marketing-jobs/<brand>/`:
`marketing-jobs/<brand>/brand/terms.txt` and
`marketing-jobs/<brand>/jobs/<YYYY-MM-DD>-<job-slug>/`.

Design source files, video and large images stay in their own tools or on a
drive. The repository holds links to them in `assets.md` and small final exports
only.

## Git conventions (repository storage only)

- **Branch per job:** `job/<YYYY-MM-DD>-<job-slug>`, from the default branch.
  Never commit to the default branch.
- **Commit per step:** commit when a step in `plan.md` changes to Done, Waiting on
  user or Sent back. The message names the step and its status, for example
  `step 3 social posts: Done`. Commit only files inside the job folder and
  `brand/`.
- **Push once agreed per job.** At job start, ask one question: "Push the job
  branch to <repository>?" Log the answer in `decisions.md`. With a yes, push
  after each commit for the rest of that job. With a no, commit locally only and
  remind the user at the end of the job that nothing was pushed.
- **Pull or merge requests:** open one only when the user asks. Merging is the
  user's action, never the director's.
- **Publishing is separate.** A merged branch is a record of what was approved.
  Anything that goes live still waits for the explicit yes in the
  ask-before-publish step.

## Checks in a client repository

The director runs `check_rules.py` during acceptance whichever storage applies.
CI in a client repository is added once the first client repository exists; until
then the director's run is the only check, and the report line says so.
