# Example file for Programming Foundations: Algorithms by Joe Marini
# Bubble sort algorithm


def bubbleSort(dataset: list):
    # TODO: start with the array length and decrement each time
    n = len(dataset)
    for i in range(n):
        for j in range(1, n-i):
            print(dataset[j-1], dataset[j], dataset[j-1] > dataset[j])
            if dataset[j-1] > dataset[j]:
               dataset[j], dataset[j-1] = dataset[j-1], dataset[j]
            print("Current state: ", dataset)


list1 = [100, 6, 20, 8, 19, 56, 23, 87, 41, 49, 53, 4]
print("Start: ", list1)
bubbleSort(list1)
print("Result: ", list1)
