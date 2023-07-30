# Read the numbers for the height and width variables from the keyboard and create the following pattern:
#
# |*	  |
# | *     |
# |  *    |
# |   *   |
# |    *  |
# |     * |
# |      *|
# |     * |
# |    *  |
# |   *   |
# |  *    |
# | *     |
# |*      |
# | *     |
# |  *    |

width = int(input('width: '))
height = int(input('height: '))

w = 0

for h in range(height):
    if h == width:
        w = 0
    print('|', end='')
    for w in range(width):
        if h == w:
            print('*', end='')
        else:
            print(' ', end='')
    print('|')

