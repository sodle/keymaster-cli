# keymaster-cli
Linux and OS X CLI for https://github.com/sodle/keymaster

## Installation
1. `sudo pip install -r requirements.txt`
2. Copy/move/rename/symlink/etc. `keymaster.py` to a directory in your PATH.

## Usage
`keymaster <path_to_public_key>`

## Roadmap
Keymaster and its CLI are in beta. Future planned features for the CLI include:
- Windows support (should in theory work already, but not yet tested)
- Read key from standard in
- Generate a keypair if it doesn't exist
- Package manager scripts for Homebrew, RPM, Aptitude, etc.
