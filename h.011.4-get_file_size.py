# Write the function called get_file_size,
# which obtains the length of a file using the seek and tell methods of the file object
# and returns it as a return value

def get_file_size(path):
    with open(path, 'r') as f:
        f.seek(0, 2)
        size = f.tell()
        print(size)


get_file_size('test.txt')
