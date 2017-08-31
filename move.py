import os
import terrain
import hero

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


def go_player(board, x, y, sign, monsters, items, player_stats, chests): # porusza postacią gracza
    direction = getch()
    move_status = {"coords":[0,0],"action":"", "found_object":""}
    new_x = x
    new_y = y
    added_item = ""
    if direction == "s":
        new_x += 1
    if direction == "w":
        new_x -= 1
    if direction == "a":
        new_y -= 1
    if direction == "d":
        new_y += 1
    if direction == "x":
        raise SystemExit("Bye")
    new_xy = board[new_x][new_y]
    if new_xy != "#":
        terrain.insert_object(board, x, y, "·")
        x = new_x
        y = new_y
    if new_xy in items:
        terrain.insert_object(board, x, y, "·")
        x = new_x
        y = new_y
        hero.add_item(board, new_xy, player_stats)
    if new_xy in monsters:
        print("GET READY FOR FIGHT!!")
        move_status.update({"coords":[x,y],"action":"fight","found_object":new_xy})
        return move_status
    if new_xy in chests:
        print("You found chest. It's locked.")
        move_status.update({"coords":[x,y],"action":"chest", "found_object":new_xy})
        return move_status

    move_status.update({"coords":[x,y]})
    return move_status
