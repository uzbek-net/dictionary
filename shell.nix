# reference: https://nixos.wiki/wiki/Packaging/Python
{
  pkgs,
}:

pkgs.stdenv.mkDerivation {
  name = "dictionary";

  nativeBuildInputs = with pkgs; [
    # Nix
    nixd
    nixfmt
    statix
    deadnix

    nodejs
    python313Packages.pip
    python313Packages.python-dotenv
    python313Packages.requests
    python313Packages.toml
    python313Packages.polib
    python313Packages.setuptools

  ];
}
