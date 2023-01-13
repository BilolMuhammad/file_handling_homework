def main(data: str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """

    n_sum = 0
    for d in data:
        if d.isdigit():
            n_sum += int(d)
    return n_sum


# Read data from file
file = open('txt_file/data07.txt')
read = file.read()
print(main(read))
