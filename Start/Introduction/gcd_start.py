# Example file for Programming Foundations: Algorithms by Joe Marini
# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcd(a, b):
    # if b == 0:
    #     return a
    
    # return gcd(min(a,b), max(a,b) % min(a,b))
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

# try out the function with a few examples
print(gcd(60, 96))  # should be 12
# print(gcd(20, 8))   # should be 4
# print(gcd(20, 4))   # should be 4
# print(gcd(4, 20))   # should be 4
