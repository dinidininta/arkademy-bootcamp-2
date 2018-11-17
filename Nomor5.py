def ganti(string, charA, charB):

    newstring = ""

    if charA not in string:
        newstring = "charA tidak terdapat pada string yang dimasukkan"
    else:
        for char in string:
            if char == charA:
                newstring += charB
            else:
                newstring += char

    return newstring

if __name__ == '__main__':
    print ganti("kelompok", "k", "u")