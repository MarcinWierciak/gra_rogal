import os
import mapz
import hero
import time

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def interact_with_object(x, y, new_xy, objects, board, player_stats, move_status):
    if new_xy in objects["items"]:
        mapz.insert_object(board, x, y, "·")
        hero.add_item(board, new_xy, player_stats)
        move_status.update({"coords":[x,y],"action":"","found_object":""})
        return move_status
    if new_xy in objects["enemies"]:
        move_status.update({"coords":[x,y],"action":"fight","found_object":new_xy})
        return move_status
    if new_xy in objects["actions"]:
        if new_xy  == "🌑":
            mapz.print_txt("'Cóż za wyjątkowa dziura, chyba w nią skoczę.'", board)
            time.sleep(0.5)
            board = mapz.load_map_file("level_2.txt")
            move_status.update({"coords":[x,y],"action":"next_level","found_object":board})
            return move_status
        if new_xy  == mapz.change_color("$", "P"):
            mapz.print_txt("Skrzynia w kształcie wielkiego znaku dolara? Co może być w środku? 'Spróbuję ją otworzyć.'", board)
            move_status.update({"coords":[x,y],"action":"chest", "found_object":new_xy})
            return move_status
        if new_xy == "W":
            mapz.print_txt("Tak groźnego bossa się nie spodziewałeś, umierasz.", board)
            raise SystemExit

def go_player(board, x, y, objects, player_stats):
    move_status = {"coords":[x,y], "action":"", "found_object":"","found_object":""}
    direction = getch()
    new_x = x
    new_y = y
    if direction == "s":
        new_x += 1
    if direction == "w":
        new_x -= 1
    if direction == "a":
        new_y -= 1
    if direction == "d":
        new_y += 1
    new_xy = board[new_x][new_y]
    if not new_xy in objects["border"]:
        mapz.insert_object(board, x, y, "·")
        x = new_x
        y = new_y
    if new_xy in objects["items"] or new_xy in objects["actions"] or new_xy in objects["enemies"]:
        move_status = interact_with_object(x, y, new_xy, objects, board, player_stats, move_status)
        return move_status
    if direction == "x":
        raise SystemExit("Żegnaj.\nCzasami jedynym wyjściem jest ucieczka.")

    move_status.update({"coords":[x,y]})
    return move_status
