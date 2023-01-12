def main(data: str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    rd = file.read()
    list = []
    for l in rd:
        if l.isdigit():
            list.append(int(l))

    return list


# Read data from file
link = 'txt_file/data03.txt'
print(main(link))
