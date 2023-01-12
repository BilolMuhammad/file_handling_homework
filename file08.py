def main(data: str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    file = open(data)
    rd = file.read()
    max = 0
    for r in rd:
        if r.isdigit():
            if int(r) > max:
                max = int(r)
    return max


# Read data from file
file = 'txt_file/data08.txt'
print(main(file))
