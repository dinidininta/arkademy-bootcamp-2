def segitiga(tinggi):

    for i in reversed(range(tinggi)):
        if i == tinggi-1:
            print(" " * (tinggi-i) + "*" * (2*i+1))
        elif i > 0:
            print(" " * (tinggi-i) + "*" + " " * (2*i) + "*")
        else:
            print(" " * (tinggi-i) + "*")

if __name__ == '__main__':

    segitiga(9)
