from collections import Counter
def plus_mult(nums: []):

    n = len(nums)
    i = 2

    r_even = nums[0]
    r_odd = nums[1]
    curr = 0

    while i < n:
        if i %2 == 0:

            if curr%2 == 1:
                r_even *= nums[i+2]
                r_odd *= nums[j+2]

            if curr%2 == 0:
                r_even += nums[i+2]
                r_odd += nums[j+2]


if __name__ == '__main__':
    arr = {12, 3, 5, 7, 13, 12}

    c1 = Counter("helllo")  # {'h': 1, 'e': 1, 'l': 3, 'o': 1}
    c2 = Counter("hell")  # {'h': 1, 'e': 1, 'l': 2}

    print(c1 - c2)
    print(f"{not (c2 - c1)} =>if this is true it means c2 is a subseet of c1 ")
