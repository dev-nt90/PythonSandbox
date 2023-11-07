import time
import random


def merge_sort(nums):
    if(len(nums) < 2):
        return nums

    left = nums[:len(nums)//2]
    right = nums[len(nums)//2:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(first, second):
    if(first is None):
        return second
    if(second is None):
        return first
    
    final = []
    i = 0
    j = 0
    
    len_first = len(first)
    len_second = len(second)

    while(i < len_first and j < len_second):
        if(first[i] <= second[j]):
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    
    if(i < len_first):
        for leftover in range(i, len_first):
            final.append(first[leftover])
    if(j < len_second):
        for rightover in range(j, len_second):
            final.append(second[rightover])

    return final

def benchmark(nums, show_nums):
    print(f"nums: {nums}")
    start = time.time()
    test(nums, show_nums)
    end = time.time()

    timeout = 1.00

    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"test took too long ({(end - start) * 1000} milliseconds). Speed it up!")
    print("====================================")


def test(nums, show_nums):
    res = merge_sort(nums.copy())
    if show_nums:
        print(f"nums: {nums}")
        print(f"sorted: {res}")
    else:
        print(f"len nums: {len(nums)}")
        print(f"len sorted: {len(res)}")
    print("------------------------------------")


def main():
    benchmark(get_nums(10), True)
    benchmark(get_nums(100), True)
    benchmark(get_nums(1000), False)
    benchmark(get_nums(10000), False)


def get_nums(num):
    nums = []
    random.seed(1)
    for i in range(num):
        nums.append(random.randint(0, len(nums)))
    return nums


main()
