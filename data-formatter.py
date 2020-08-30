raw_dataset = []

def read_and_process():
    with open("dataset.txt") as data:
        line = data.readline()
        while(line!=""):
            raw_dataset.append(line.split("\t"))
            line = data.readline()

    with open("data-formatted.txt","w") as f:
        for i in range(len(raw_dataset)):
            f.write(raw_dataset[i][0]+"\t"+raw_dataset[i][1]+"\n")

def error_check():
    with open("data-formatted.txt") as f:
        data = f.read()

    data = data.split("\n")
    new = []
    for datum in data:
        new.append(datum.split("\t"))

    for i in range(len(new)):
        if(len(new[i])<2):
            print(i+1, new[i])
