def main(data: str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    dt = f.read()
    return len(dt)


link = 'txt_file/data02.txt'
print(main(link))
# Read data from file
