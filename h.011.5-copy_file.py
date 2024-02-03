# Write the function named copy_file,
# which copies a file by reading n characters from the source file in a loop and
# writing them to the other file

def copy_file(source_path, dest_path):
    with open(source_path, 'r', encoding='utf-8') as rf:
        with open(dest_path, 'w', encoding='utf-8') as wf:
            s = rf.read()
            wf.write(s)


copy_file('test.txt', 'text.txt')
