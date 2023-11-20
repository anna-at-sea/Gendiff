import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    file_format = args.format
    return first_file, second_file, file_format
