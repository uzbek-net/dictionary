import polib, re, glob, argparse


def normalize_apostrophes(folder_path: str):
    """
    Normalize apostrophes in a .po file to use ʻ (U+02BB) for o' and g', as well as ʼ (U+02BC) for "tutuq belgisi".

    Args:
        folder_path (str): The folder path to the .po files. example: folder_path="locale/"
    """
    files: list[str] = glob.glob("{}*.po".format(folder_path))

    for file in files:
        # Load the .po file
        print("Load the .po file", file)

        po = polib.pofile(file)

        # Iterate through each entry in the .po file
        for entry in po:
            if entry.msgstr:
                # Replace all variations of apostrophes with the standard single quote
                entry.msgstr = re.sub("O'", "Oʻ", entry.msgstr)
                entry.msgstr = re.sub("O‘", "Oʻ", entry.msgstr)
                entry.msgstr = re.sub("O’", "Oʻ", entry.msgstr)
                entry.msgstr = re.sub("Oʼ", "Oʻ", entry.msgstr)
                entry.msgstr = re.sub("O`", "Oʻ", entry.msgstr)

                entry.msgstr = re.sub("o'", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o‘", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o’", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("oʼ", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o`", "oʻ", entry.msgstr)

                entry.msgstr = re.sub("G'", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G‘", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G’", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G’", "oʻ", entry.msgstr)

                entry.msgstr = re.sub("g'", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g‘", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g’", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("gʼ", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g`", "oʻ", entry.msgstr)

        # Save the changes back to the .po file
        po.save(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize apostrophes in a .po file.")
    parser.add_argument(
        "--folder_path",
        help='''The folder path to the .po files. example: folder_path="locale"''',
        required=True,
    )

    args = parser.parse_args()

    normalize_apostrophes(args.folder_path)
    print(f"Apostrophes in have been normalized.")
