while True:
    cmd = input('CSD>').split()
    if len(cmd) == 0:
        continue
    match cmd:
        case 'length', text:
            print(len(text))
        case 'upper', text:
            print(text.upper())
        case 'lower', text:
            print(text.lower())
        case 'concat', text1, text2:
            print(text1.concat(text2))
        case 'reverse', text:
            print(text[::-1])
        case 'repitition', text, n:
            print(text * int(n))
        case 'count', text:
            d = dict()
            for t in text:
                c = text.count(t)
                d[t] = c
            for i in d:
                print(i, ' => ', d[i])
        case ['quit']:
            break
        case _:
            print(f'invalid command: {cmd[0]}')
