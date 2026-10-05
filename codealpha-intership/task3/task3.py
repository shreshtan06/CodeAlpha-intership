import re
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
INPUT_FILE = PROJECT_DIR / "input.txt"
OUTPUT_FILE = PROJECT_DIR / "extracted_emails.txt"
EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"


def extract_emails(text: str) -> list[str]:
    emails = re.findall(EMAIL_PATTERN, text)
    return sorted(set(emails), key=str.lower)


def read_file(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")
    except OSError as error:
        raise OSError(f"Unable to read the file: {error}")


def save_emails(emails: list[str], file_path: Path) -> None:
    try:
        file_path.write_text("\n".join(emails), encoding="utf-8")
    except OSError as error:
        raise OSError(f"Unable to save the output file: {error}")


def get_input_path() -> Path:
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).expanduser().resolve()
    return INPUT_FILE


def create_sample_input() -> None:
    sample_text = """Contact us at support@example.com or hello@company.org.
    For updates, email admin@sample.io.
    Duplicate addresses: hello@example.com
    """
    INPUT_FILE.write_text(sample_text, encoding="utf-8")


def main() -> None:
    print("=" * 55)
    print("       CODEALPHA - EMAIL EXTRACTOR")
    print("=" * 55)

    try:
        input_path = get_input_path()
        if not input_path.exists():
            create_sample_input()
            input_path = INPUT_FILE

        text = read_file(input_path)
        emails = extract_emails(text)

        if not emails:
            print("\nNo email addresses were found.")
            return

        save_emails(emails, OUTPUT_FILE)

        print(f"\nInput file     : {input_path}")
        print(f"Emails found   : {len(emails)}")
        print(f"Output file    : {OUTPUT_FILE}")

        print("\nExtracted Email Addresses:")
        print("-" * 55)

        for number, email in enumerate(emails, start=1):
            print(f"{number:>2}. {email}")

        print("\nEmail extraction completed successfully.")

    except (FileNotFoundError, OSError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()