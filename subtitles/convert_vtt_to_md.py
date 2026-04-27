#!/usr/bin/env python
"""Convert VTT subtitle files to Markdown interview transcripts."""

import os
import re
import glob

SUBTITLES_DIR = os.path.join(os.path.dirname(__file__), "subtitles")
OUTPUT_DIR = os.path.dirname(__file__)

# Map video ID to YouTube URL
def parse_vtt(vtt_path):
    with open(vtt_path, encoding="utf-8") as f:
        content = f.read()

    # Remove WEBVTT header and metadata blocks
    content = re.sub(r"WEBVTT\n.*?\n\n", "", content, flags=re.DOTALL)

    # Remove timestamp lines (00:00:00.000 --> 00:00:00.000 ...)
    content = re.sub(r"\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}[^\n]*\n", "", content)

    # Remove block IDs (lines that are just numbers)
    content = re.sub(r"^\d+\s*$", "", content, flags=re.MULTILINE)

    # Remove HTML tags like <c>, </c>, <00:00:00.000>, position/align metadata
    content = re.sub(r"<[^>]+>", "", content)

    # Split into lines and deduplicate consecutive identical lines
    lines = content.split("\n")
    cleaned = []
    prev = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line != prev:
            cleaned.append(line)
            prev = line

    # Join into paragraphs: merge lines that are clearly continuations
    # (simple approach: join all into a single text block, then re-paragraph)
    text = " ".join(cleaned)

    # Clean up extra whitespace
    text = re.sub(r"\s{2,}", " ", text).strip()

    return text


def extract_title_and_id(filename):
    # filename: "Title [ID].en.vtt"
    match = re.match(r"^(.+) \[([A-Za-z0-9_-]+)\]\.en\.vtt$", filename)
    if match:
        return match.group(1).strip(), match.group(2)
    return filename, ""


def wrap_paragraphs(text, chars_per_para=800):
    """Split long text into readable paragraphs at sentence boundaries."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    paragraphs = []
    current = []
    length = 0
    for s in sentences:
        current.append(s)
        length += len(s)
        if length >= chars_per_para:
            paragraphs.append(" ".join(current))
            current = []
            length = 0
    if current:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs)


def main():
    vtt_files = sorted(glob.glob(os.path.join(SUBTITLES_DIR, "*.en.vtt")))
    print(f"Found {len(vtt_files)} VTT files")

    for vtt_path in vtt_files:
        filename = os.path.basename(vtt_path)
        title, video_id = extract_title_and_id(filename)

        # Sanitize title for filename (remove chars not safe for filenames)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
        safe_title = safe_title.replace("｜", "-").replace("：", " -").strip()
        md_filename = f"{safe_title}.md"
        md_path = os.path.join(OUTPUT_DIR, md_filename)

        transcript = parse_vtt(vtt_path)
        body = wrap_paragraphs(transcript)

        youtube_url = f"https://www.youtube.com/watch?v={video_id}"

        md_content = f"""# {title}

**Source:** [{youtube_url}]({youtube_url})

---

## Transcript

{body}
"""
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"  ✓ {md_filename}")

    print(f"\nDone. {len(vtt_files)} markdown files created in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
