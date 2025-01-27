# QuickSort
# Given an array of integers nums, sort the array in ascending order and return it.
def quicksort(nums, low, high):
    # If the current part of the array is not empty
    if low < high:
        # Partition the array and get the pivot element index
        pi = partition(nums, low, high)
        # Recursively sort elements before the partition
        quicksort(nums, low, pi - 1)
        # Recursively sort elements after the partition
        quicksort(nums, pi + 1, high)

def partition(nums, low, high):
    # Choose the last element as the pivot.
    pivot = nums[high]
    i = low - 1
    # Reorder elements around the pivot, so elements less than pivot go to the left
    for j in range (low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i], nums[i + 1], nums[high] = nums[high, nums[i + 1]
            # Swap the pivot element with the first element that is greater than the pivot
            return i + 1

def sort_array(nums):
    # Start quicksort from the first to the last element
    quicksort(nums, 0 , len(nums) - 1)
    return nums