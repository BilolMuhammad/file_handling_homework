def main(data: str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, encoding='utf8')
    data = f.read()
    r_list = data.split(',')
    list = []
    i = 0
    for i in r_list:
        b = int(i)
        list.append(b)
    return list


# Read data from file
link = "txt_file/data01.txt"
print(main(link))
