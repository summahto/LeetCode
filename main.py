# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def getMinimumCost(arr):
    # Write your code here
    # find neighbor has max difference
    cost = 0
    max_cost = 0
    f_index, s_index = 0, 0
    # find max diff between neighbors
    for i in range(len(arr)-1):
        first = arr[i]
        second = arr[i+1]
        if abs(second-first) > max_cost:
            max_cost = abs(second-first)
            f_index = i
            s_index = i + 1
    # new number between the max diff
    mid = (arr[f_index] + arr[s_index]) // 2
    # add the cost
    cost += (arr[f_index] - mid) * (arr[f_index] - mid)
    cost += (arr[s_index] - mid) * (arr[s_index] - mid)
    # add the cost
    for i in range(len(arr)-1):
        if i == f_index:
            continue
        first = arr[i]
        second = arr[i+1]
        cost += (first - second) * (first - second)
    return cost


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    arr = [1,3,5,2,10]
    print(getMinimumCost(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
