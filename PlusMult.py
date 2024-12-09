
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
    plus_mult(arr)
