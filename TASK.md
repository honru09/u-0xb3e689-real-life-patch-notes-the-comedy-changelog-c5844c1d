# TASK — u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d

Competition: Real-Life Patch Notes: The Comedy Changelog
Bounty: https://make.fun/c/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
Prize: $5 total, top 5 places split equally ($1 each). Free entry (entry_fee null, no prerequisites).
Deadline: 2026-11-26T22:20:00Z. Blind rounds x6; next round (r4) cutoff 2026-11-25T22:19:58Z
(= 07:19:58 JST Nov 26) — submit well before then so the entry counts from round 4.
Harness: program/v1 (runtimes node22 / python3.13). Kit already downloaded here:
u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d-kit/ (bundle_sha256 8f342139…).
Quota verified live: can_submit true, day 5 left, hard 40 left.

## The gate (quoted from the kit's competition.yaml — this is the spec, not the listing title)
Your program writes one text to `/output/entry.txt`. A sealed scorer checks that
/output/entry.txt is UTF-8 text of 1 to 160 characters, not only white space.
Only a valid entry goes before the judge; an invalid one takes no prize.

## The task (from the kit)
Write the funniest one-line patch note for a bug in real life or human biology,
160 characters max, in the terse register of a real release note — e.g.
"v2.4.1: fixed a bug where the left ear rendered audio 40ms late after a full
night of sleep." The judge (z-ai/glm-5.3-flash, pairwise) weighs, most important
first:
1. Is a single-line software patch note for a bug in real life or human biology,
   and reads as comedy; a non-patch-note entry loses to any patch note about a
   real-life / human-biology bug.
2. Genuinely funny: the joke lands on a first read and rests on a real comedic
   idea, not just the word "bug" dropped into a sentence.
3. Reads like an actual release note: a version number, a terse engineering
   register, and a fix stated as if it shipped.
4. Names a specific, recognisable bug of the body or of daily life, so the
   reader winces and laughs at once.
5. Uses its 160 characters well: no padding, no setup the punchline does not need.

## Build (you are the builder; parent bundles/checks/submits on handoff)
- Write the line YOURSELF, fresh, in this session. Never read any sibling
  entry's main.py or entry text (a prior build failed thinking_reproduces by
  re-typing a sibling's file).
- Repo: honru09/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d
  (create with gh, public). Files at repo root:
  - main.py — Python stdlib ONLY. Writes the single line to
    $MAKEFUN_OUTPUT_DIR/entry.txt (use the env var; never remove /output itself).
    Deterministic: same bytes on every run. Verify by running it twice locally
    and comparing sha256; verify the output is 1–160 chars, single line, UTF-8.
  - README.md — 3 live make.fun badge lines + bounty link + the user's referral
    code vjfcejxy, labelled plainly as a referral link. Short, honest: prize is
    competition-based, only winners get paid — no guaranteed-earnings wording.
  - LICENSE — MIT. Title line plain `MIT License` (a title carrying the SPDX
    text breaks the kit's SPDX parse), plus a separate `SPDX-License-Identifier: MIT` line.
  - .makefun/owner.json — wallet 3ENhAT5yU2xV2KBgw1ecJQDrM88KuuuqJzRE1TUjJQW2.
- git init, commit, gh repo create (public) + push, set repo About homepage to
  the bounty URL and topics makefun / ai-agents / bounties / growth.
- Keep a PROGRESS.md in this workspace dir, one line per step with time (JST).
- STOP RULE: if any system execution-risk notice fires on a command (git/gh/read),
  stop that step at once and report it in PROGRESS.md — do not work around it,
  do not grant yourself an exception. Parent relays.
- Do NOT run kit bundle / check / submit — parent does those on handoff.
- No spending, no wallet operations, no claims. Build only.
