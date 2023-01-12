def main(data: str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data, encoding='utf-8')
    rd = file.read().split('\n')
    leng = []
    for r in rd:
        leng.append(len(r))
    return max(leng)


# Read data from file
link = 'txt_file/data10.txt'
print(main(link))
