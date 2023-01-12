def main(data: str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list = []
    rd = data.read().split(',')
    for i in rd:
        list.append(int(i))
    return list


# Read data from file
f = open('txt_file/data01.txt', encoding='utf-8')
print(type(main(data=f)[0]))
