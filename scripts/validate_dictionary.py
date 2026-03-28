"""Validate dictionary.toml entries for structural and linguistic consistency."""

import sys
import tomllib
from pathlib import Path

REQUIRED_FIELDS = {"en", "uz", "part_of_speech", "description", "pronunciation_uz", "similar", "status"}

VALID_PART_OF_SPEECH = {"noun", "verb", "adjective", "adverb", "interjection"}

VALID_STATUS = {"Needs translation", "Pending review", "Obsolete", "Approved", "Do not translate"}

WRONG_APOSTROPHES = {"'", "\u2018", "\u2019", "`"}


def validate(path: Path) -> list[str]:
    """Validate dictionary TOML file. Returns list of error messages."""
    with open(path, "rb") as f:
        data = tomllib.load(f)

    entries = data.get("translations", [])
    if not entries:
        return ["No translations found in file"]

    errors: list[str] = []
    seen_en: dict[str, int] = {}

    for i, entry in enumerate(entries):
        prefix = f"Entry {i} (en={entry.get('en', '?')!r})"

        # 1. Field presence
        missing = REQUIRED_FIELDS - set(entry.keys())
        if missing:
            errors.append(f"{prefix}: missing fields {missing}")
            continue

        en = entry["en"]
        uz = entry["uz"]
        status = entry["status"]

        # 2. Unique en keys
        if en in seen_en:
            errors.append(f"{prefix}: duplicate 'en' key (first at entry {seen_en[en]})")
        else:
            seen_en[en] = i

        # 3. Valid enum values
        if entry["part_of_speech"] not in VALID_PART_OF_SPEECH:
            errors.append(f"{prefix}: invalid part_of_speech={entry['part_of_speech']!r}")

        if status not in VALID_STATUS:
            errors.append(f"{prefix}: invalid status={status!r}")

        # 4. Conditional completion — empty uz allowed for incomplete statuses
        skip_completion = status in ("Needs translation", "Pending review")
        if not skip_completion and not uz:
            errors.append(f"{prefix}: 'uz' is empty (status={status!r})")

        # 5. Apostrophe check
        for field in ("en", "uz", "description", "pronunciation_uz"):
            value = entry.get(field, "")
            for ch in WRONG_APOSTROPHES:
                if ch in value:
                    errors.append(
                        f"{prefix}: wrong apostrophe {ch!r} in '{field}' — "
                        f"use ʼ (U+02BC) or ʻ (U+02BB) instead"
                    )

        # 6. Lowercase check (abbreviations = all-uppercase are allowed)
        for field in ("en", "uz"):
            value = entry.get(field, "")
            if value and value != value.lower() and value != value.upper():
                errors.append(f"{prefix}: '{field}' must be lowercase (got {value!r})")

    return errors


def main() -> None:
    path = Path("dictionary.toml")
    if not path.exists():
        print("ERROR: dictionary.toml not found")
        sys.exit(1)

    errors = validate(path)

    if errors:
        print(f"FAILED: {len(errors)} error(s) found:\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("OK: all entries valid")
        sys.exit(0)


if __name__ == "__main__":
    main()
