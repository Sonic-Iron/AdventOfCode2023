
def get_num(number, line, char):

    try:
        pass
    except IndexError:


def Day3A(inputtext):
    total = 0
    for line in range(len(inputtext)):
        for char in range(len(line)):
            if inputtext[line][char] != '.' and not inputtext[line][char].isalnum():
                for hor_dir in [-1,0,1]:
                    for ver_dir in [-1,0,1]:
                        hor_covered = False
                        if inputtext[line+ver_dir][char+ver_dir].isalnum():
                            number = inputtext[line+ver_dir][char+ver_dir]
                            number = get_num(number, line, char)



with open('./Day3txt') as f:
    inputtext = f.read().splitlines()
    Day3A(inputtext)