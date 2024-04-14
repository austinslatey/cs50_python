import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Regex to match the src of an iframe element containing a YouTube URL
    pattern = r'<iframe[^>]*\s+src\s*=\s*"https?://(?:www\.)?youtube\.com/embed/([^"]*)"'
    match = re.search(pattern, s, re.IGNORECASE)

    # If a mtach is found, extract the video ID and construct the YT URL
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None


if __name__ == "__main__":
    main()
