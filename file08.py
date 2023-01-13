def main(data: str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

    max = 0
    for d in data:
        if d.isdigit():
            if int(d) > max:
                max = int(d)
    return max


# Read data from file
file = open('txt_file/data08.txt')
read = file.read()
print(main(read))
