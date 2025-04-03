# File Hash Generator

## Overview
The File Hash Generator is a Python tool that computes cryptographic hashes for files using the `hashlib` library. It supports MD5 and SHA-256 algorithms and processes files in chunks for efficiency.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- No additional libraries beyond the Python standard library

## Usage
Run the script with the following arguments:

```bash
python3 file_hash_generator.py --file <FILE_PATH> [--algo <ALGORITHM>] [--config <CONFIG_FILE>]
