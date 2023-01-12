def main(data: str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data)
    rd = file.read()
    list = []
    for r in rd:
        if r.isnumeric():
            list.append(int(r))
    min = list[0]
    for l in list:
        if l < min:
            min = l
    return min


# Read data from file
link = 'txt_file/data09.txt'
print(main(link))
