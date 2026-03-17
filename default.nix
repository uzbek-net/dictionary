{
  pkgs,
  python3,
  ...
}:

python3.pkgs.buildPythonPackage {
  name = "uzbek_net_dictionary";
  version = "0.1.0";
  pyproject = true;
  src = ./.;

  propagatedBuildInputs = with pkgs; [
    python313Packages.pip
    python313Packages.python-dotenv
    python313Packages.requests
    python313Packages.toml
    python313Packages.polib
    python313Packages.setuptools
  ];

  build-system = [
    pkgs.python313Packages.setuptools
  ];

  # No tests
  doCheck = false;

  meta = {
    description = "uzbek dictionary for various translations, including GNOME";
  };
}
