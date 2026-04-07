# AGENTS.md

Keep changes small and literal. This repository mixes teaching notebooks and Python scripts, so avoid broad churn.

## Setup
- Read `README.md` and `environment.yml` first.
- Run Python-related commands in the `edu` Conda environment, whether via `conda run -n edu ...`, `conda activate edu`, or an equivalent method.
- If the task appears to require a different environment or setup, ask before switching.

## Scope and change control
- Stay extremely close to the user's request.
- Do not invent features, refactors, cleanup passes, or dependency changes.
- Keep diffs minimal and local.
- Preserve existing behavior, user edits, notebook outputs, and file structure unless the user explicitly asks otherwise.
- Do not take destructive actions without explicit approval. This includes deleting files, overwriting user work, `rm`, `git reset`, force checkouts, and similar commands.
- If anything is unclear, ask a concise clarifying question before editing. Do not guess.

## Python rules
- For Python changes, follow PEP 8.
- Prefer simple, readable code.
- When printing numeric values inside strings, use explicit formatting such as `:,.4f` where appropriate.

## Notebook rules
- When touching notebooks, avoid unnecessary output or metadata churn.
- Keep notebook markdown cells concise enough not to overflow the typical VS Code notebook viewport.
- Split long explanations into smaller adjacent markdown cells when appropriate, using the existing notebook style as the benchmark.
- For notebook presentation, put large rendered outputs such as tables and figures in their own code cell directly below the cell that prepares them, and render them with `display()`.
- This presentation rule applies to notebooks, not normal Python files.

## Verification
- Verify the exact change you made when practical.
- Say clearly if you could not run a check.