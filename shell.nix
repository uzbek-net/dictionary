# reference: https://nixos.wiki/wiki/Packaging/Python
{
  pkgs ? import <nixpkgs> { },
}:
let
  pythonEnv = pkgs.python3.withPackages (
    ps: with ps; [
      pip
      python-dotenv
      requests
    ]
  );
in
pkgs.stdenv.mkDerivation {
  name = "auto-profile-tg-dev";

  nativeBuildInputs = with pkgs; [
    # Nix
    nixd
    nixfmt
    statix
    deadnix

    nodejs
    # Python
    pythonEnv
    poetry
    python313Packages.typing-extensions
    python313Packages.polib
    python313Packages.toml
  ];
}
