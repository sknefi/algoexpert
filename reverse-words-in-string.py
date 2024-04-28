# difficulty: 2/4

# string: "AlgoExpert is the best!"

# output: "best! the is AlgoExpert"
def isWhiteSpace(char):
    # function returns if character we are iterating through is white space
    if char == " " or char == '\t' or char == '\n':
        return True

    return False


def reverseWordsInString(string):
    # here we will store our output
    result = ''

    # define pointer that points on last character in string
    ptr = len(string) - 1

    # store mutiple non-white characters or multiple white characters
    # for example: "Hello there  ObiWan."
    # first word:     "ObiWan."
    # second word:    "  "  - two spaces
    # third word:     "there"
    # fourth word:    " "   - one space
    # fifth word:     "Hello"
    word = ''

    # keep track of previous character (if it is white character or not)
    prevWhite = False

    # iterate through string from behind (start from last character)
    # (you can also use for loop, when I work with pointers I prefer while loops)
    while 0 <= ptr:
        # if current character is not white space
        if not isWhiteSpace(string[ptr]):
            # if previous character is white space
            if prevWhite:
                # till this moment we iterated through white characters, we need to add
                # these white characters to result and change $word to current character
                result += word
                # change $word to current character
                word = string[ptr]

            else:
                word = string[ptr] + word

            # character we are currently iterating is not white space, so we set $prevWhite to False
            # (our main while loop is ending here so in next iteration this character will be
            # viewed as previous character ~> thats why $prevWhite is called $prevWhite)
            prevWhite = False  # set current

        # if current character is white space
        else:
            # if previous character is white space
            if prevWhite:
                # add white character to word  " " ~~> "  "
                word += string[ptr]

            else:
                # till this moment we iterated through not white characters, we need to add
                # these characters to result and change $word to current white character
                result += word
                # change $word to current white character
                word = string[ptr]

            # character we are currently iterating is white space, so we set $prevWhite to True
            # (our main while loop is ending here so in next iteration this character will be
            # viewed as previous character ~> thats why $prevWhite is called $prevWhite)
            prevWhite = True  # set current


        # move pointer one character to left
        ptr -= 1

    # last word is not in $result so we have to add it there manualy
    result += word

    return result

