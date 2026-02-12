def print_file_content(file_path):
    print(f"Reading file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)