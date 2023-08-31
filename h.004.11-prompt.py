while True:
    cmdline = input('CSD>').strip()

    i = 0
    while i < len(cmdline):
        if cmdline[i].isspace():
            break
        i += 1

    cmd = cmdline[:i]

    if len(cmd) == 0:
        continue

    match cmd:
        case 'length' | 'reverse' | 'lower' | 'upper' | 'count' | 'repitition':
            while i < len(cmdline) and cmdline[i].isspace():
                i += 1
            if i == len(cmdline) or cmdline[i] != '"':
                print('invalid string')
                continue
            i += 1
            start = i

            while i < len(cmdline) and cmdline[i] != '"':
                i += 1
            if i == len(cmdline):
                print('unterminated string')
                continue

            if cmd != 'repitition' and i != len(cmdline) - 1:
                print('command has extra characters')
                continue

            s = cmdline[start:i]
            if cmd == 'length':
                print(i - start)
            elif cmd == 'reverse':
                print(s[::-1])
            elif cmd == 'lower':
                print(s.lower())
            elif cmd == 'upper':
                print(s.upper())
            elif cmd == 'count':
                for c in set(s):
                    print(f'{c} => {s.count(c)}')
            elif cmd == 'repitition':
                i += 1
                while i < len(cmdline) and cmdline[i].isspace():
                    i += 1

                if i == len(cmdline):
                    print('repitition command without repitition count')
                    continue

                start = i
                while i < len(cmdline) and cmdline[i].isdigit():
                    i += 1

                if i != len(cmdline):
                    print('command count invalid')
                    continue

                n = int(cmdline[start:i])
                print(s * n)

        case 'reverse':
            print('reverse command')
        case 'quit':
            break

        
