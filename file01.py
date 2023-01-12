def main(data: str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    data = data.read()
    r_list = data.split(',')
    list = []
    i = 0
    for i in r_list:
        b = int(i)
        list.append(b)
    return list


# Read data from file
file = open("txt_file\data01.txt", encoding='utf-8')
print(main(file))
