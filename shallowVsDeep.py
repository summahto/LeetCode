import copy

def function(string):
    string = "created"

    return string


if __name__ == '__main__':
    s = "Sumit"

    print(function(s))

    print(f"{s=}")

    test = lambda x, y: x**y

    print(f"{test(2,3)=}")

    nums = [(i*2, i/2) for i in range(10, -1, -1)]

    print(f"{nums=}")
    nums.sort(key=lambda x: x)


    # Original list with a nested list
    original = [1, 2, [3, 4]]

    # Shallow copy
    shallow_copy = copy.copy(original)

    # Deep copy
    deep_copy = copy.deepcopy(original)

    # Modify the nested list in the shallow copy
    shallow_copy[2][0] = 100

    # Modify the nested list in the deep copy
    deep_copy[2][0] = 200

    print("Original:", original)
    print("Shallow Copy:", shallow_copy)
    print("Deep Copy:", deep_copy)

