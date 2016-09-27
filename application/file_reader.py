import sys

def get_board_data(file_location):
    board_data = []
    
    with open(file_location, 'r') as data_file:
        text_data = data_file.readlines()
        for i, line in enumerate(text_data):
            if i < 2:
                # .cells files have two lines before the data.
                continue
            line_no_endings = line.replace('\n', '')
            board_data.append(line_no_endings)

    return board_data

