def main(data: str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    list = []
    rd = f.read().split(',')
    for i in rd:
        list.append(int(i))
    return list


# Read data from file
link = "txt_file/data01.txt"
print(main(link))
