# GEMINI.md

This project is a research knowledge repository dedicated to the investment philosophy and market commentary of Stanley Druckenmiller. It is managed as an Obsidian vault.

## Project Overview

The repository collects, translates, and organizes transcripts of interviews and public appearances by Stanley Druckenmiller. The goal is to create a structured knowledge base for studying his investment strategies, macro views, and risk management principles.

## Directory Structure

- `访谈原文/` — Contains original English transcripts in Markdown format, primarily sourced from YouTube.
- `访谈/` — Contains Chinese translations of the interviews.
- `他人分析总结/` — Reserved for third-party analysis, summaries, and thematic deep-dives.
- `.obsidian/` — (IGNORED) Configuration for the Obsidian tool; do not index or modify.
- `temp/` — (IGNORED) Temporary storage for processing.

## Content Pipeline & Workflow

### 1. Acquisition
- Transcripts are typically sourced from YouTube auto-generated subtitles (`.vtt` files).
- Filename convention for raw subtitles: `Title [VideoID].en.vtt`.

### 2. Processing (English)
- Raw `.vtt` files are converted to Markdown.
- **English Markdown Format:**
  - `# {Title}`
  - `**Source:** [{youtube_url}]({youtube_url})`
  - `---`
  - `## Transcript`
  - Text is split into paragraphs of approximately 800 characters at sentence boundaries.

### 3. Translation & Formatting (Chinese)
- Interviews are translated into Chinese and stored in the `访谈/` directory.
- **Chinese Markdown Format:**
  - YAML Frontmatter:
    ```yaml
    ---
    title: {Chinese Title}
    source: {URL}
    date: {YYYY-MM-DD}
    language: zh
    tags: [Druckenmiller, investment, interview]
    ---
    ```
  - Header: `# {Chinese Title}`
  - Content Section: `## 访谈记录` or `## 摘要`

## Usage Guidelines

- **Researching Themes:** Use Obsidian's tagging and linking features (e.g., `#Druckenmiller`, `[[Investment Philosophy]]`) to connect concepts across different interviews.
- **Adding Content:** When adding new interviews, ensure they are placed in `访谈原文/` first, then translated and placed in `访谈/` following the established YAML metadata format.
- **Analysis:** Contributions to `他人分析总结/` should reference specific interviews using internal links.

## Tools & Environment

- **Python:** Used for conversion scripts (e.g., `convert_vtt_to_md.py`). Use `python` for execution and `pip` for package management.
- **Git:** The project uses Git for version control. The `.obsidian/` and `temp/` directories are ignored and should not be tracked or modified by the agent.
