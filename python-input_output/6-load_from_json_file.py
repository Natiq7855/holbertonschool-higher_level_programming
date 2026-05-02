#!/usr/bin/python3
"""func of upload"""
import json


def load_from_json_file(filename):
    """func of"""

    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
