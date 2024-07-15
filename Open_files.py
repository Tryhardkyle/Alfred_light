import os
import json
import sys

def open_file(file_path):
    file_path = os.path.abspath(file_path)
    os.system('start "" "{}"'.format(file_path))

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <command>")
        return
    
    command = " ".join(sys.argv[1:]).lower()

    # Create an empty file_paths dictionary
    file_paths = {}

    # Read the JSON file and update file_paths dictionary
    with open('file_paths.json', 'r') as file:
        data = json.load(file)
        for entry in data:
            text_array = entry['text_array']
            file_path = entry['file_path']
            file_paths.update({text.lower(): file_path for text in text_array})

    if command in file_paths:
        open_file(file_paths[command])
        print(f"Opening file: {file_paths[command]}")
    else:
        print("I don't know that one, please try again")

if __name__ == "__main__":
    main()
