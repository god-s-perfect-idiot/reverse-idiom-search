def read_data():
    with open("data-formatted.txt") as f:
        data = []
        line = f.readline()[:-1].split("\t")
        while(line!=['']):
            data.append(line)
            line = f.readline()[:-1].split("\t")


    return data
