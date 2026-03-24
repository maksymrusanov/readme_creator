import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_repo_url() -> str | None:
    if remote := os.getenv("REMOTE_URL"):
        return remote

    git_config = Path(".git/config")
    if not git_config.exists():
        return None

    for line in git_config.read_text().splitlines():
        if "url" in line and "github" in line.lower():
            return line.split("=")[-1].strip()
    return None


def main():
    parser = argparse.ArgumentParser(description="Generate README.md for your project")
    parser.add_argument("-o", "--output", default="README.md", help="Output file path")
    parser.add_argument("-m", "--model", default="gemini-3-flash-preview", help="Gemini model")
    parser.add_argument("--no-git", action="store_true", help="Skip reading git remote")
    args = parser.parse_args()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment")

    prompt = """You are a professional technical writer. Generate a README.md for this project.
Follow these guidelines:
- Use Markdown formatting consistently
- Include: Description, Features, Installation, Usage, Contributing, License
- Keep it concise and technically accurate"""

    contents = prompt
    if not args.no_git:
        if url := get_repo_url():
            contents += f"\n\nRepository: {url}"

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model=args.model, contents=contents)

    if not response.text:
        raise ValueError("Empty response from API")

    Path(args.output).write_text(response.text)
    print(f"README.md written to {args.output}")


if __name__ == "__main__":
    main()
