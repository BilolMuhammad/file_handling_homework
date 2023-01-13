def main(data: str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    list = []
    for d in data:
        if not d.isdigit():
            list.append(d)
    return list


# Read data from file
file = open('txt_file/data04.txt')
read = file.read()
print(main(read))
