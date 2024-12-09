from bisect import bisect_right

if __name__ == '__main__':

    items = [[1,2],[1,2],[1,3],[1,4]]
    queries = [1]

    i = bisect_right(items, queries[0], key=lambda x: x[0])

    print(items[i-1][1])
