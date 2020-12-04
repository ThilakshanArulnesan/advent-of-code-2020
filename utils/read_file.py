def read_file(fname, should_print=False):
    f = open(fname, "r")
    data = []
    for line in f:
        data.append(line.rstrip('\n'))

    if should_print:
        print(data)
    return data