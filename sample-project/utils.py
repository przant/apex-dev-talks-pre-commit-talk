#!/usr/bin/env python
# The script above should be executable but isn't - will trigger check-shebang-scripts-are-executable

def process_data(data):
    # Missing type annotation - will trigger python-use-type-annotations
    
    # Trailing whitespace - will trigger trailing-whitespace
    processed = data.upper()    
    
    # More trailing whitespace
    return processed  

# Missing merge conflict markers - will trigger check-merge-conflict
<<<<<<< HEAD
def another_function():
    return "This is the current version"
=======
def another_function():
    return "This is the incoming version"
>>>>>>> feature-branch

# Misspelled word - will trigger codespell
def comupte_metrics(values):
    # Missing type annotation
    total = sum(values)
    average = total / len(values)
    return {"total": total, "average": average}