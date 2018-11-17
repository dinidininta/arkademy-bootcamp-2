from datetime import timedelta, date


def between_days(firstDate, secondDate):
    first = firstDate.split('-')
    second = secondDate.split('-')

    d1 = date(int(first[0]), int(first[1]), int(first[2]))
    d2 = date(int(second[0]), int(second[1]), int(second[2]))

    delta = d2 - d1

    for i in range(delta.days + 1):
        print(d1 + timedelta(i))


if __name__ == '__main__':

    between_days('2008-10-01', '2008-10-05')
