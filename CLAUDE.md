# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## CLI Settings

If Python packages need to be installed, use `pip` not `pip3`. If Python files need to be run, use `python` not `python3`.

## Project Overview

This is a research knowledge repository collecting Stanley Druckenmiller's investment philosophy and market commentary through curated interview transcripts. It is structured as an Obsidian vault with Git-backed version control.

## Directory Structure

- `interviews/` — Main interviews directory containing Markdown transcripts and the conversion script
- `interviews_translation/` — Markdown transcripts of interviews translated into Chinese
- `scripts/` - Relevant python scripts to perform operations on the knowledge base
- `indices` - Indices guiding the structure of the knowledge base 

## Content Pipeline

New transcripts are added via:
1. Download YouTube auto-generated subtitles as `.en.vtt`. The filename must follow the pattern `Title [VideoID].en.vtt`.
2. Run the conversion script in `scripts/`:
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

## Manual Cleanup: VTT → Canonical Format

Auto-generated subtitles often lack punctuation, paragraph breaks, and speaker labels. After running the conversion script, manually clean up each file to match the canonical format used in `interviews/`:

### 1. Add YAML Frontmatter

Replace the `# Title` + `**Source:**` header block with:

```yaml
---
title: {Title}
source: {youtube_url}
date: YYYY-MM-DD
language: en
original_transcript: {yes | no}
tags:
  - Druckenmiller
  - {topic}
  - {interview | speech}
---
# {Title}

---
## Transcript
```

### 2. Add Speaker Labels

Label each speaker as `**Name:**` at the start of their turn. Use the person's last name or role (e.g. `**Druckenmiller:**`, `**Joe:**`, `**Moderator:**`). For solo speeches/TED talks, label every paragraph with the single speaker.

### 3. Add Punctuation

VTT auto-captions are unpunctuated. Restore:
- Sentence-ending periods, question marks, exclamation marks
- Commas at clause boundaries
- Em dashes (`—`) for asides and interruptions
- Quotation marks where the speaker quotes someone
- Percent signs, dollar signs, and numeric formatting (e.g. `57%`, `$780 billion`)

### 4. Break into Paragraphs

Split the wall of text into logical paragraphs — one topic or argument per paragraph. Each speaker turn is a new paragraph. Long monologues should be broken at natural topic transitions.
