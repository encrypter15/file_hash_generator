#!/usr/bin/env python3
# File Hash Generator
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Generates file hashes. Supported algorithms: md5, sha256.

import hashlib
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='file_hash.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"default_algo": "sha256"}

def generate_hash(file_path: str, algo: str) -> str:
    """Generate a hash for the file."""
    hash_obj = hashlib.md5() if algo == "md5" else hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except (FileNotFoundError, IOError) as e:
        logging.error(f"File error: {e}")
        return ""

def main():
    """Main function to parse args and generate hash."""
    parser = argparse.ArgumentParser(description="File Hash Generator")
    parser.add_argument("--file", required=True, help="File path")
    parser.add_argument("--algo", choices=["md5", "sha256"], help="Hash algorithm")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)
    algo = args.algo or config["default_algo"]

    logging.info(f"Generating {algo} hash for {args.file}")
    hash_result = generate_hash(args.file, algo)
    if hash_result:
        logging.info(f"Hash: {hash_result}")
        print(f"{algo} hash: {hash_result}")
    else:
        print("Error: Hash generation failed")

if __name__ == "__main__":
    main()
