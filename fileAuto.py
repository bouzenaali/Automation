import os
import shutil
import json
import logging
import argparse

# Setup logging
logging.basicConfig(level=logging.INFO)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Path to configuration file', required=True)
args = parser.parse_args()

# Load directories and extensions from configuration file
with open(args.config, 'r') as f:
    config = json.load(f)

src_dir = config['src_dir']
ext_dir_map = config['ext_dir_map']
other_dir = config['other_dir']

def move_files():
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        if os.path.isfile(src_path):
            ext = os.path.splitext(filename)[1].lower()
            if ext in ext_dir_map:
                dest_dir = ext_dir_map[ext]
            else:
                dest_dir = other_dir
            dest_path = os.path.join(dest_dir, filename)
            try:
                shutil.move(src_path, dest_path)
                logging.info(f"Moved {src_path} to {dest_path}")
            except (PermissionError, FileNotFoundError, IsADirectoryError) as e:
                logging.error(f"Error moving {src_path} to {dest_path}: {e}")

if __name__ == "__main__":
    try:
        move_files()
    except Exception as e:
        logging.error(f"An error occurred: {e}")