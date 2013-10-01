# This algorithm is the linear congruent method for generating random numbers
# Takes an old seed as a parameter, multiplies it by some constant a,
# adds another constant c, then takes the remainder of that number as the new random number
# Usually constant_a and the modulus are chosen so that they are relatively prime
# Relative prime means that the two numbers have the greatest common divisor of 1
# Usually constant_a is chosen so that constant_a - 1 is divisible by all prime factors of the modulus
# TODO: add check for prime factors
# Usually constant_a is a multiple of 4 if the modulus is a multiple of 4

import math

constant_a = 1664525
constant_c = 1013904223
modulus = int(math.pow(2, 32))

# Find the greatest common divisor
def gcd(a, b):
    # Get the remainder
    r = a % b
    if (r == 0):
        return b
    return gcd(b, r)

def linearCongruentRandom(seed):
    new_seed = (constant_a * seed + constant_c) % modulus
    return new_seed

if __name__ == "__main__":

    safety_check = gcd(constant_a, modulus)
    if (safety_check != 1):
        print("Warning: constant_a and modulus are not relatively prime. gdc(" + str(constant_a) + ", " + str(modulus) + " =  " + str(safety_check))

    if (modulus % 4 == 0 and constant_c % 4 != 0):
        print("Warning: the modulus is a multiple of 4, but constant_a is not")

    numbers = []
    seed = 2019
    count = 0
    while (count < 10):
        seed = linearCongruentRandom(seed)
        numbers.append(seed)
        count += 1
    print(numbers) 
