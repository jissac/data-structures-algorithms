def quicksort(nums: [int]) -> [int]:
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [num for num in nums[1:] if num < pivot]
        greater = [num for num in nums[1:] if num > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    nums = [10, 2, 3, 4, 1, 99]
    print(quicksort(nums))