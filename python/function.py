#As invented by sideeq

def find_line(filename):
    """A function that gets the number of lines of a file"""
    count = 0
    for i in filename:
        count += 1
    print(count, end=" ")
