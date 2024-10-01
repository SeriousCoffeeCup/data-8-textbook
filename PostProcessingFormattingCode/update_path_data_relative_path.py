import os
import re

def update_path_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to find the path_data variable declaration with various paths, quote styles, and including partial paths
    path_data_regex = r"path_data\s*=\s*['\"](\.\./){1,3}(assets/data/)?['\"]"

    new_content = re.sub(path_data_regex, "from path_data_variable import *", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def update_files_in_directory(directory):
    current_code_file = os.path.abspath(__file__)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check for .py or .ipynb extension, avoid modifying current file
        if (file_path.endswith('.py') or file_path.endswith('.ipynb')) and file_path != current_code_file:
            update_path_data(file_path)
            print(f"Updated {filename}")

def main():
    directory_to_scan = '.'  
    update_files_in_directory(directory_to_scan)

if __name__ == "__main__":
    main()
