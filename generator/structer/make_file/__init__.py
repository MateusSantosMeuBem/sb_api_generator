def make_file(path_name: str, file_content):
    with open(path_name, 'w') as file:
        file.write(file_content)