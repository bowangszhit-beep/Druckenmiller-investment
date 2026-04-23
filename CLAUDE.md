# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CLI Settings

If Python packages need to be installed, use `pip` not `pip3`. If Python files need to be run, use `python` not `python3`.

## Project Overview

This is a research knowledge repository collecting Stanley Druckenmiller's investment philosophy and market commentary through curated interview transcripts. It is structured as an Obsidian vault with Git-backed version control.

## Directory Structure

- `访谈原文/` — Main interviews directory containing Markdown transcripts and the conversion script
- `访谈/` — Markdown transcripts of interviews translated into Chinese
- `他人分析总结/` — Placeholder directory for third-party analysis summaries (currently empty)

## Content Pipeline

New transcripts are added via:
1. Download YouTube auto-generated subtitles as `.en.vtt`. The filename must follow the pattern `Title [VideoID].en.vtt`.
2. Run the conversion script:
```
   && python convert_vtt_to_md.py
```
   This generates `.md` files directly in with a `# Title`, `**Source:**` YouTube link, and `## Transcript` section.

## Transcript Format

Each generated Markdown file has the structure:
```
# {Title}

**Source:** [{youtube_url}]({youtube_url})

---

## Transcript

{paragraphs of ~800 chars each, split at sentence boundaries}
```

