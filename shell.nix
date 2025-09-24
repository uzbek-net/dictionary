# reference: https://nixos.wiki/wiki/Packaging/Python
{pkgs ? import <nixpkgs> {}}: let
  pythonEnv = pkgs.python3.withPackages (ps:
    with ps; [
      pip
      python-dotenv
      requests
    ]);
in
  pkgs.stdenv.mkDerivation {
    name = "auto-profile-tg-dev";

    nativeBuildInputs = with pkgs; [
      # Nix
      nixd
      alejandra
      statix
      deadnix

      # Python
      pythonEnv
      poetry
      nodejs
    ];
  }
