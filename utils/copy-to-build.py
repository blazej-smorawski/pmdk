#!/usr/bin/env python
import os
import re
import shutil
import argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Copy files tree from $MESON_SOURCE_ROOT to $MESON_BUILD_ROOT')

# Optional positional argument
parser.add_argument('--regex', type=str, required=True,
                    help='Use regular expression to choose files.')

parser.add_argument('--root-directory', type=str, required=True,
                    help='Set root directory from which files will be copied recursively')
                    
args = parser.parse_args()

source_root = os.getenv('MESON_SOURCE_ROOT')
build_root = os.getenv('MESON_BUILD_ROOT')

root_directory = args.root_directory
regex = re.compile(args.regex)

for root, dirs, files in os.walk(root_directory):
    for file in files:
        relative_path = os.path.relpath(os.path.join(root,file), source_root)
        if regex.match(file):
            src = os.path.join(source_root,relative_path)
            dst = os.path.join(build_root,relative_path)
            if os.path.isdir(os.path.dirname(dst)):
                shutil.copy(os.path.join(source_root,relative_path),dst)

print('copy-to-build.py finished.')
