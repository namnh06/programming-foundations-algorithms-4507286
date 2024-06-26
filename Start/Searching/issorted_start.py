# Example file for Programming Foundations: Algorithms by Joe Marini
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    for i in range(1, len(itemlist)):
        if itemlist[i-1] > itemlist[i]:
            return False

    return True

print(is_sorted(items1))
print(is_sorted(items2))

