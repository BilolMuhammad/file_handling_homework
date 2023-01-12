def main(data: str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    rd = file.read().split()
    list = []
    for r in rd:
        list.append(len(r))

    return list


# Read data from file
link = 'txt_file/data06.txt'
print(main(link))
