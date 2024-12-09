import heapq


def even(start, n):
    ans = []
    i = start

    while n >= 0:
        if start % 2 == 0:
            ans.append(start)
            n -= 1

        start += 1

    return ans


if __name__ == '__main__':
    # print(even(5, 10))
    print(ord('a'), chr(90))

    pq = [(1, 2), (1, 5), (1, 1), (1, 0), (1, 3)]

    while pq:
        (d, node) = heapq.heappop(pq)
        print(d, node)

