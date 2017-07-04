#!/usr/bin/env python3
import random

square_size = 100
square_possibilities = ['.', 'O']
cell_probability = 0.50

def get_new_char(cell_probability):
    if cell_probability > random.random():
        return square_possibilities[0]
    else:
        return square_possibilities[1]

for i in range(square_size):
    row = []
    for j in range(square_size):
        new_char = get_new_char(cell_probability)
        row.append(new_char)
    formatted_string = ''.join(row)
    print(formatted_string)
