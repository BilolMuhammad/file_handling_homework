def main(data: str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data = data.split('\n')
    list = []
    for d in data:
        list.append(len(d))

    return list


# Read data from file
file = open('txt_file/data06.txt')
read = file.read()
print(main(read))
