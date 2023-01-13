def main(data: str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    list = []
    for l in data:
        if l.isdigit():
            list.append(int(l))

    return list


# Read data from file
file = open('txt_file/data03.txt')
read = file.read()
print(main(read))
