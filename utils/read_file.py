def read_file(fname, should_print=False):
    f = open(fname, "r")
    data = []
    for line in f:
        data.append(line.rstrip('\n'))

    if should_print:
        print(data)
    return data


def read_file_chunks(fname, split_text="\n\n", join_seperator=None):
    f = open(fname, "r")

    if(join_seperator == None):
        return [chunk.split()
                for chunk in f.read().split(split_text)]

    return [join_seperator.join(chunk.split())
            for chunk in f.read().split(split_text)]

def read_file_chunks_no_split(fname, split_text="\n\n", join_seperator=None):
    f = open(fname, "r")

    if(join_seperator == None):
        return [chunk
                for chunk in f.read().split(split_text)]

    return [join_seperator.join(chunk)
            for chunk in f.read().split(split_text)]
