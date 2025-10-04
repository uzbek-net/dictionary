"""
source: https://gist.github.com/devhero/8ae2229d9ea1a59003ced4587c9cb236
"""

import requests
import tarfile

gnome_49: str = "https://l10n.gnome.org/languages/uz/gnome-49/ui.tar.gz"
gnome_circle: str = "https://l10n.gnome.org/languages/uz/gnome-circle/ui.tar.gz"
gnome_infra: str = "https://l10n.gnome.org/languages/uz/gnome-infrastructure/ui.tar.gz"
gnome_librem: str = "https://l10n.gnome.org/languages/uz/librem5/ui.tar.gz"

archives: dict[str, str] = {
    "49": gnome_49,
    "circle": gnome_circle,
    "infra": gnome_infra,
    "librem": gnome_librem,
}

for k, v in archives.items():
    print(k, v)
    res = requests.get(v, stream=True)

    if res.status_code == 200:
        file = tarfile.open(fileobj=res.raw, mode="r|gz")
        file.extractall("gnome/{}".format(k), filter="data")