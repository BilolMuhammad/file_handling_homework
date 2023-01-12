def main(data: str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data)
    rd = file.read()
    n_sum = 0
    for r in rd:
        if r.isdigit():
            n_sum += int(r)
    return n_sum


# Read data from file
link = 'txt_file/data07.txt'
print(main(link))
