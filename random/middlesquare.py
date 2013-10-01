# Von Neumann middle-square method for generating random numbers

import math

debug = False

def debugprint(*arg):
    if (debug == True):
        print(arg)

def middleSquareRandom(seed, n):

    # Square the seed and convert it to string
    newseed_string = str(seed*seed)
    count = -1
    out = ""

    debugprint(str(seed) + " squared is " + newseed_string)

    # If the new seed is of correct length, return it
    if (len(newseed_string) <= n):
        debugprint("new seed is less than n = " + str(n) + ", returning " + newseed_string)
        return int(newseed_string)
    
    # If the new seed is too long, see how many numbers
    # must be skipped from the beginning to get the middle portion
    numbers_to_skip = int(math.ceil(len(newseed_string)/4))
    debugprint("New number is too long, skipping " + str(numbers_to_skip) + " digits")

    # Add the correct numbers of numbers to the output and return it
    for char in newseed_string:
        count += 1
        # Skip any leading unimportant numbers
        if (count < numbers_to_skip):
            continue
        out += (newseed_string[count])
        debugprint("Adding " + newseed_string[count] + " to output: " + out) 
        if (len(out) == n):
            debugprint("Returning " + str(out))
            return int(out)
    debugprint("something went wrong: count: " + str(count) + " out: " + out)

if __name__ == "__main__":
    n = 4
    seed = 11
    i = 0
    numbers = []
    while i < 10:
        seed = middleSquareRandom(seed, n)
        numbers.append(seed)
        i += 1

    print(numbers)
    

