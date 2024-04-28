# difficulty: 1/4

# string:  "abcdcba"
# output:  true

def isPalindrome(string):
    # count of letters in $string
    n = len(string)
    # create right pointer which is pointing to last letter
    rightPtr = len(string) - 1

    # create left pointer which is pointing to first letter till it reachs middle letter
    # we can check only half of a word, we compare first half with second half
    for leftPtr in range(0, n//2):
        if string[leftPtr] != string[rightPtr - leftPtr]:
            # word is not palindrom
            return False

    # left half side of word is equal to right half side of word (from behind)
    return True