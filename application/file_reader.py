import sys

def line_to_int_list(line):
    int_list = []
    line_no_spaces = line.rstrip()

    for s in line_no_spaces:
        try:
            new_int = int(s)
            int_list.append(new_int)
        except ValueError:
            print('Non-digit in file, exiting')
            sys.exit()

    return int_list


def get_board_data(file_location):
    board_data = []
    
    with open(file_location, 'r') as data_file:
        text_data = data_file.readlines()
        for line in text_data:
            int_list = line_to_int_list(line)
            board_data.append(int_list)
    
    return board_data

