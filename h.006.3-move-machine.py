# Suppose an imaginary machine is at position (0, 0) in the Cartesian coordinate system.
# The following commands are sent to this machine:
#
# Up n
# DOWN n
# left n
# RIGHT n
#
# Here n denotes a number. Commands are not case sensitive.
# Write a function named move_machine that takes a text as a parameter.
# Let the text consist of the above commands.
# The function should receive this script and return a tuple in the form of (x, y)
# indicating the new location of the machine. You can test with the following program:
#
# def move_machine(s):
#      pass
#
# s = 'Up 4 ; Down 2 ; Down 3; Left 4; up 2'
# x, y = move_machine(s)
#
# print(x, y)

def move_machine(s):
    x = 0
    y = 0
    temp_key_value = []
    temp_s = s.split(';')
    for temp in temp_s:
        key_value = temp.split()
        temp_key_value.append(tuple(key_value))

    for (temp_key, temp_value) in temp_key_value:
        tk = temp_key.upper()
        tv = int(temp_value)

        match tk:
            case 'UP':
                y += tv
            case 'DOWN':
                y -= tv
            case 'RIGHT':
                x += tv
            case 'LEFT':
                x -= tv
            case _:
                print('invalid command')
                break

    return x, y


x, y = move_machine(input('enter your command: '))
print(x, y)
