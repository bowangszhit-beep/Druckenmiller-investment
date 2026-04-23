# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CLI Settings

If Python packages need to be installed, use `pip` not `pip3`. If Python files need to be run, use `python` not `python3`.

## Project Overview

This is a research knowledge repository collecting Stanley Druckenmiller's investment philosophy and market commentary through ~36 curated interview transcripts. It is structured as an Obsidian vault with Git-backed version control.

## Directory Structure

- `访谈/` — Main interviews directory containing Markdown transcripts and the conversion script
  - `访谈/subtitles/` — Raw VTT subtitle files downloaded from YouTube (`.en.vtt` format)
  - `访谈/convert_vtt_to_md.py` — Script that converts VTT files into formatted Markdown transcripts
- `他人分析总结/` — Placeholder directory for third-party analysis summaries (currently empty)

## Content Pipeline

New transcripts are added via:
1. Download YouTube auto-generated subtitles as `.en.vtt` into `访谈/subtitles/`. The filename must follow the pattern `Title [VideoID].en.vtt`.
2. Run the conversion script from the `访谈/` directory:
   ```
   cd 访谈 && python convert_vtt_to_md.py
   ```
   This generates `.md` files directly in `访谈/` with a `# Title`, `**Source:**` YouTube link, and `## Transcript` section.

## Transcript Format

Each generated Markdown file has the structure:
```
# {Title}

**Source:** [{youtube_url}]({youtube_url})

---

## Transcript

{paragraphs of ~800 chars each, split at sentence boundaries}
```

## Obsidian Integration

The repository doubles as an Obsidian vault (`.obsidian/` config directory). Two plugins are active: `obsidian-git` (auto-sync via Git) and `claudian` (Claude AI integration). When browsing or annotating transcripts, Obsidian is the primary interface.
