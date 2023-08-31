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

pos = 0
direction = 1
for _ in range(height):
    print('|' + ' ' * pos + '*' + ' ' * (width - pos - 1) + '|')
    if pos == width - 1:
        direction = -1
    elif pos == 0:
        direction = 1
    pos += direction

