#!/usr/bin/python3
"""
4-Append_write
Contains function that apppends to text file and returns number of chararcters added
"""

def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
