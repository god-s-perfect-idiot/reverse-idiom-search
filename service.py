import model



def search(term):
    output = []
    term = term.lower()
    data = model.read_data()
    temp = term.split()
    if(len(temp)>0):
        for datum in data:
            dat = datum[1].lower()
            if term in dat:
                output.append(datum)
                continue
            hit_count = 0
            for word in temp:
                if(word in dat):
                    hit_count += 1
            if(hit_count>2):
                output.append(datum)


    return output
