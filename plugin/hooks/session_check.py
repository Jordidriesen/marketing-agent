#!/usr/bin/env python3
"""SessionStart hook: confirm Python 3 can run the plugin's hooks.

When this script runs at all, Python 3 is there, and it stays silent. When python3 cannot
be started, Claude Code reports this hook as failed once at session start, which is the
warning: the save check and the publish gate need Python 3 (see the plugin README).
"""
import sys

if sys.version_info < (3, 8):
    print("marketing-agent: the save check and publish gate need Python 3.8 or newer; "
          f"found {sys.version.split()[0]}.", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
