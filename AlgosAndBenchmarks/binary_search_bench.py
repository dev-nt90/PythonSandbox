import time


def binary_search(target, arr, evaluate_higher = False):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        median = (low + high) // 2
        if(arr[median] < target):
            low = median + 1
        else:
            high = median - 1

        # key thing here is that we evaluate the "low" index, which should never exceed the size of the array
        # we might be able to speed this up by ALSO comparing what's currently at the high index
        if(
            (low != len(arr) and arr[low] == target) or 
            (evaluate_higher == True and high >= 0 and arr[high] == target)
            ):
            return True

    return False


def benchmark(names_dict, first_name):
    start = time.time()
    test(names_dict, first_name)
    end = time.time()

    print(f"test completed in less than {end-start} milliseconds!")
    print("====================================")


def test(target, arr):
    res = binary_search(target, arr)
    print(f"- len arr: {len(arr)}")
    print(f"- target: {target}")
    print(f"Result: {res}")
    print("------------------------------------")


def main():
    # TODO: capture time complexity of low+high comparison vs only low comparison
    complexity = 2000000
    nums = get_nums(complexity)
    benchmark(int(complexity * 0.2344), nums)
    benchmark(int(complexity * 2), nums)
    benchmark(int(complexity + 1), nums)
    benchmark(int(complexity * 0.765), nums)


def get_nums(num):
    nums = []
    for i in range(num):
        nums.append(i)
    return nums


main()
