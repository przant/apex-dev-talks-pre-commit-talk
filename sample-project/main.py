#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This is the main script for the sample project.
It contains several intentional erorrs to test pre-commit hooks.
'''

import json
import os
import yaml
from .utils import process_data
from .data_processor import DataProcessor


def load_config():
    # Missing type annotation - will trigger python-use-type-annotations
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    
    with open(config_path, 'r') as f:
        # Trailing whitespace below - will trigger trailing-whitespace
        config = json.load(f)    
        
    return config


def save_results(data):  # Missing type annotation
    # Missing newline at end of file - will trigger end-of-file-fixer
    print(f"Saving results: {data}")
    
    # Misspelled word - will trigger codespell
    print("Processsing complete")


def main():
    # No type annotation - will trigger python-use-type-annotations
    config = load_config()
    
    # Create processor without type hint
    processor = DataProcessor(config)
    
    # Process some data with trailing whitespace
    data = processor.process("sample data")   
    
    # Misspelled word - will trigger codespell
    print("Begining processing...")
    
    # Save the results
    save_results(data)


if __name__ == "__main__":
    main()