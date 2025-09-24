import polib, re, glob


def normalize_apostrophes():
    """
    Normalize apostrophes in a .po file to use ʻ (U+02BB) for o' and g', as well as ʼ (U+02BC) for "tutuq belgisi".

    Args:
        po_file_path (str): The path to the .po file.
    """
    files: list[str] = glob.glob("locale/*.po")

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
                entry.msgstr = re.sub("O`", "Oʻ", entry.msgstr)

                entry.msgstr = re.sub("o'", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o‘", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o’", "oʻ", entry.msgstr)
                entry.msgstr = re.sub("o`", "oʻ", entry.msgstr)

                entry.msgstr = re.sub("G'", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G‘", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G’", "Gʻ", entry.msgstr)
                entry.msgstr = re.sub("G’", "oʻ", entry.msgstr)

                entry.msgstr = re.sub("g'", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g‘", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g’", "gʻ", entry.msgstr)
                entry.msgstr = re.sub("g`", "oʻ", entry.msgstr)

        # Save the changes back to the .po file
        po.save(file)


if __name__ == "__main__":
    normalize_apostrophes()
    print(f"Apostrophes in have been normalized.")
