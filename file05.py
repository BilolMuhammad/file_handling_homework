def main(data: str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    num = 0
    nonnum = 0
    for d in data:
        if d.isdigit():
            num += 1
        else:
            nonnum += 1
    return [num, nonnum]


# Read data from file
file = open('txt_file/data05.txt')
read = file.read()
print(main(read))
