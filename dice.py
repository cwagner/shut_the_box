BORDER = '+-----+'
SPACER = '      '
EYE = ' o'


def print_dice(r1, r2):
    print(BORDER + SPACER + BORDER + '\n' +
          _top_row(r1) + SPACER + _top_row(r2) + '\n' +
          _middle_row(r1) + SPACER + _middle_row(r2) + '\n' +
          _top_row(r1)[::-1] + SPACER + _top_row(r2)[::-1] + '\n' +
          BORDER + SPACER + BORDER + '\n')


def _top_row(r):
    return f'| {EYE[r > 1]} {EYE[r > 3]} |'


def _middle_row(r):
    return f'| {EYE[r > 5]}{EYE[r % 2]}{EYE[r > 5]} |'
