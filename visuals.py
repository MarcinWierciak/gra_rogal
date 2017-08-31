
def change_color(string, color):
    if color == 'W':
        colored_string = '\033[0m' + string + '\033[0m' # white (normal)
    if color == 'R':
        colored_string = '\033[31m' + string + '\033[0m' # red
    if color == 'G':
        colored_string = '\033[32m' + string + '\033[0m' # green
    if color == 'O':
        colored_string = '\033[33m' + string + '\033[0m' # orange
    if color == 'B':
        colored_string = '\033[34m' + string + '\033[0m' # blue
    if color == 'P':
        colored_string = '\033[35m' + string + '\033[0m' # purple
    if color == 'S':
        colored_string = '\033[36m' + string + '\033[0m' # sea blue
    return colored_string


def change_color_of_chosen_sign_on_board(lista, chosen_sign, color):
    for element in lista:
        if element == chosen_sign:
            new_element = visuals.change_color(element, color)
            loc = lista.index(element)
            lista.remove(element)
            lista.insert(loc, new_element)
