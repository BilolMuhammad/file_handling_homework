def main(data: str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

    list = []
    for d in data:
        if d.isnumeric():
            list.append(int(d))
    min = list[0]
    for l in list:
        if l < min:
            min = l
    return min


# Read data from file
file = open('txt_file/data09.txt')
read = file.read()
print(main(read))
