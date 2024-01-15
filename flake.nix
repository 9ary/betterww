{
  description = "Better Wind Waker";

  inputs = {
    flake-compat = {
      url = "github:edolstra/flake-compat";
      flake = false;
    };
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };
    systems.flake = false;
  };

  outputs = { ... } @ inputs: inputs.flake-parts.lib.mkFlake {
    inherit inputs;
  } ({ config, flake-parts-lib, getSystem, inputs, lib, options, ... }:
    let
      rootConfig = config;
      rootOptions = options;
    in
    {
      _file = ./flake.nix;
      imports = [ ];
      config.perSystem = { config, inputs', nixpkgs, options, pkgs, system, ... }:
        let
          systemConfig = config;
          systemOptions = options;
        in
        {
          _file = ./flake.nix;
          config = {
            devShells.default = pkgs.callPackage
              ({ mkShell
              , python3Packages
              , qt5
              }: mkShell {
                name = "betterww";
                nativeBuildInputs = [
                  python3Packages.python
                  python3Packages.pyside2
                  python3Packages.pyyaml
                  python3Packages.pillow
                  qt5.qtwayland
                ];
              })
              {
                mkShell = pkgs.mkShell.override {
                  stdenv = pkgs.stdenvNoCC;
                };
              };
          };
        };
      config.systems = import inputs.systems;
  });
}
