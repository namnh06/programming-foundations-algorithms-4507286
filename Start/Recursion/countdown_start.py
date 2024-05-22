# Example file for Programming Foundations: Algorithms by Joe Marini
# use recursion to implement a countdown counter


def countdown(x):
    # breaking point
    if x == 0:
        return None
    print(f'{x} ...')
    return countdown(x-1)


countdown(5)
