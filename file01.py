def main(data: str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, encoding='utf8')
    r_list = f.read().split(',')
    list = []
    for l in r_list:
        list.append(int(l))
    return list

    return rd


# Read data from file
link = "txt_file/data01.txt"
print(main(link))
