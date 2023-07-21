def main_condition():
    carry_on = input('Carry on?\n')
    while carry_on != 'no':
        carry_on = input('Carry on?\n')


def main_infinite():
    while True:
        carry_on = input('Carry on?\n')
        if carry_on == 'no':
            break


if __name__ == '__main__':
    main_condition()
    main_infinite()