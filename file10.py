def main(data: str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data = data.split('\n')
    max = len(data[0])
    for d in data:
        if len(d) > max:
            max = len(d)
    return max


# Read data from file
file = open('txt_file/data10.txt')
read = file.read()
print(main(read))
