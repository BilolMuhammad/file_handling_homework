def main(data: str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    rd = file.read()
    list = []
    for r in rd:
        if not r.isdigit():
            list.append(r)
    return list


# Read data from file
link = 'txt_file/data04.txt'
print(main(link))
