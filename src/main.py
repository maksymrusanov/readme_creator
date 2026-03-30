import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_repo_url() -> str | None:
    url = input("Enter the GitHub repository URL (or press Enter to skip): ").strip()
    if url == "exit":
        print("Exiting the program.")
        return None
    elif not url.startswith("http") or "github.com" not in url:
        print("Invalid URL. Please enter a valid GitHub repository URL.")
        return get_repo_url()
    return url


def main(url: str | None = None):
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("GENAI_API_KEY not found in environment variables")

    prompt = f"""You are a professional technical writer. Generate a README.md for project on {url} .
Follow these guidelines:
- Use Markdown formatting consistently
- Include: Description, Features, Installation, Usage, Contributing, License
- Keep it concise and technically accurate"""

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt
    )
    if not response.text:
        raise ValueError("Empty response from API")
    else:
        filename = "readme.md" if url else "test.md"
        with open(filename, "w") as f:
            f.write(response.text)

    print(f"{filename} written to {Path().absolute()}")


if __name__ == "__main__":
    main(get_repo_url())
