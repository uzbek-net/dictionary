import polib, re, argparse, glob


def normalize_apostrophes():
    """
    Normalize apostrophes in a .po file to use ʻ (U+02BB) for o' and g', as well as ʼ (U+02BC) for "tutuq belgisi".

    Args:
        po_file_path (str): The path to the .po file.
    """
    files: list = glob.glob("locale/*.po")
    print(files)
    for file in files:
        # Load the .po file
        print(file)

        po = polib.pofile(file)

        # Define a regex pattern to match different apostrophe characters
        # apostrophe_pattern = re.compile(r"[’‘`]")

        # Iterate through each entry in the .po file
        for entry in po:
            if entry.msgstr:
                # Replace all variations of apostrophes with the standard single quote
                entry.msgstr = re.sub("O'", "Oʻ", entry.msgstr)
                entry.msgstr = re.sub("o'", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("O‘", "O‘", entry.msgstr)
                entry.msgstr = re.sub("o‘", "o‘", entry.msgstr)
                entry.msgstr = re.sub("G'", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("g'", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("G‘", "G‘", entry.msgstr)
                entry.msgstr = re.sub("g‘", "g‘", entry.msgstr)
                entry.msgstr = re.sub("’", "ʼ", entry.msgstr)
                entry.msgstr = re.sub("'", "ʼ", entry.msgstr)

        # Save the changes back to the .po file
        po.save(file)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Normalize apostrophes in a .po file.")
    # parser.add_argument(
    #     "--po_file", help="Path to the .po file to normalize.", required=True
    # )

    # args = parser.parse_args()

    normalize_apostrophes()
    print(f"Apostrophes in '' have been normalized.")
