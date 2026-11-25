# Handoff — One Line of Earned Pride

Competition: u-mang-one-line-of-earned-pride-a0138557 ($5)
Deadline: 2026-11-27 12:15 CST
Limit: 1–240 characters. Entry: 120 characters.

## Entry (verbatim, as given by the user)

I finally wrote the bug report I used to hate receiving: three steps, one screenshot, and an admission that I caused it.

## Method

- Pulled the kit from https://make.fun/c/u-mang-one-line-of-earned-pride-a0138557/kit and read RULES.txt / competition.yaml: program writes one line to `/output/entry.txt`, UTF-8, 1–240 characters, not only whitespace.
- Wrote all files by hand in `repo/` (no copied code, no generated content).
- `main.py` was written twice: v1 wrote the entry and ran clean; v2 added a real improvement — it reads `/output/entry.txt` back after writing and exits with an error if the content differs from ENTRY by even one character, is outside 1–240 characters, or ends with a newline.
- `main.py` writes UTF-8, no trailing newline, reads no external files, makes no network calls.

## Verification

- Ran `main.py` twice (v2): both exits 0.
- `cmp` run 1 vs run 2: byte-identical. `cmp` vs v1 output: byte-identical.
- entry.txt: 120 bytes / 120 characters, no trailing newline.
- sha256: 86799762671f097b695326875844053a338bd100c5f2f31eb02c6413229a57e9
- `prompt.txt` (120 bytes) is byte-identical to `entry.txt`.
- Files: `main.py`, `LICENSE` (MIT, SPDX-License-Identifier: MIT), `README.md` (competition link + 3 official badges), `prompt.txt`, `.makefun/owner.json`, `HANDOFF.md`.

## Not done (per task)

No submission, no GitHub repo created, no bundle touched.
