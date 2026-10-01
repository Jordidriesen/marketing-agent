# AI content humanising: moved

The humanising rules now live in one place: the **`ai-content-cleaner`** skill. It holds the
pattern tiers, the DETECT / CLEAN / BALANCED modes, the language pattern files (NL including
Belgian Dutch, FR, DE, ES), the protected-spans rule and the invisible-Unicode pass.

Any skill that says "run the humanising pass" should invoke `ai-content-cleaner` in the mode it
names. This file stays only so older references to its path still resolve; don't add rules here.
