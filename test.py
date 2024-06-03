import curses

# Это будет проверка правильности символов
def is_valid_char(ch):
    # Здесь мы просто проверяем, что символ является буквой
    return ch.isalpha()

def main(stdscr):
    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(0, 0, "Type something (only letters are valid):")

    current_text = ""
    y, x = 1, 0

    while True:
        ch = stdscr.getch()

        if ch == ord('\n'):
            break

        if ch == curses.KEY_BACKSPACE or ch == 127:
            if current_text:
                current_text = current_text[:-1]
                x -= 1
                stdscr.delch(y, x)
        else:
            char = chr(ch)
            if is_valid_char(char):
                stdscr.addch(y, x, char, curses.color_pair(2))
                current_text += char
            else:
                stdscr.addch(y, x, char, curses.color_pair(1))
            x += 1

        stdscr.refresh()

    stdscr.addstr(3, 0, f"Final text: {current_text}")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)



