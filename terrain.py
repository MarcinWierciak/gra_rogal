import csv


def read_file(filename): # wczytuje plik i zamienia go na listę składająca się z list (linie i rzędy)
    board = []
    complete_board = []
    with open(filename, newline='') as inputfile:
        for row in csv.reader(inputfile):
            board.append(row)
    for element in board:
        complete_board.append(list(element[0]))
    return complete_board


def insert_object(board, x, y, sign): # umieszacza znak na planszy
    board[x][y] = sign
    return board
