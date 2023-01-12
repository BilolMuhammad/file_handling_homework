def main(data: str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    file = open(data)
    rd = file.read().strip()
    num = 0
    nonnum = 0
    for r in rd:
        if r.isdigit():
            num += 1
        else:
            nonnum += 1
    return [num, nonnum]


# Read data from file
file = 'txt_file/data05.txt'
print(main(file))
