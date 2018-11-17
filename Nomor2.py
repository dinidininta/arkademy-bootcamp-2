import re


def verify_username(username):
    special = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    letter = re.compile('[A-Za-z]')

    if len(username) < 8:
        return "username harus berjumlah lebih dari 8 karakter"
    else:
        if special.search(username) is None or letter.search(username) is None:
            return "username harus memiliki huruf besar, huruf kecil, dan karakter spesial"
        else:
            return "username valid"


if __name__ == '__main__':

    print verify_username("Dininta_1")
