def lines_of_file(file):
    with open(file, 'r', newline="\r\n") as f:
        lines = f.read().splitlines()
        for line in lines:
            yield line
