WORD_TO_LETTER = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}


def Day1A():
    with open("./Day1txt") as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        end_digit = None
        start_digit = None
        for idx in range(len(line)):
            if line[idx].isdigit() and not start_digit:
                start_digit = line[idx]
            if line[-idx - 1].isdigit() and not end_digit:
                end_digit = line[-idx - 1]
        print(start_digit, end_digit, start_digit + end_digit)
        total += int(start_digit + end_digit)
    print(total)


def Day1B(word_to_letter):
    with open("./Day1txt") as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        end_digit = None
        start_digit = None
        for idx in range(len(line)):
            for word in word_to_letter.keys():
                if line[idx:].startswith(word) and not start_digit:
                    start_digit = word_to_letter.get(word)
                if line[:-idx - 1].endswith(word) and not end_digit:
                    end_digit = word_to_letter.get(word)
        total += int(start_digit + end_digit)
    print(total)




Day1B(WORD_TO_LETTER)
