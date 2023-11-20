def format_result(file_name):
    with open(f'gendiff/tests/fixtures/txt/{file_name}.txt', 'r') as open_path:
        return open_path.read()
