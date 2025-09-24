# reference to poetry2nix: https://github.com/nix-community/poetry2nix
{
  description = "auto-profile-tg - Adds real-time clock to your telegram profile and more";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";

    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  } @ inputs:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      # poetryApp = inputs.poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };

      # autoProfileTgPkg = poetryApp.mkPoetryApplication {
      #   projectDir = pkgs.fetchFromGitHub {
      #     owner = "bahrom04";
      #     repo = "auto-profile-tg";
      #     rev = "master";
      #     sha256 = "sha256-w8WVuKQfp+LWr5RHBq1WgUkBnMQQ1a/hQMcesNXdiug=";
      #   };
      # };
    in {
      # Nix script formattar
      formatter = pkgs.alejandra;

      devShells.default = pkgs.callPackage ./shell.nix { inherit pkgs; };

      # Output package
      # packages.default = pkgs.callPackage ./. {};

      # apps.default = {
      #   type = "app";
      #   program = "${autoProfileTgPkg}/bin/runner";
      # };
    });
    # // {
    #   darwinModules.default = import ./module.nix self;
    # };
}