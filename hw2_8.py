# Linear Selection:
# Given an integer array nums and an integer k, return the k^th largest element.
def partition(nums, left, right):
    # Choose the rightmost element as the pivot
    pivot = nums[right]
    i = left
    # Reorder the array by comparing w/ the pivot
    for j in range(left, right):
        if nums [j] <= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            # Swap the pivot element to it's correct position
        nums[i], nums[right] = nums[right], nums[i]
        return i

def quickselect(nums, left, right, k):
    # Base case: the part of the array has only one element
    if left == right:
        return nums[left]
        # Partition the array and get the index of the pivot element in sorted order
    pivot_index = partition(nums, left, right)
    # If the pivot is at the k-th position, return it
    if k == pivot_index:
        return nums[k]
        #If k is less than at the pivot index, recur on the left sub-array
    else k < pivot_index:
        return quickselect(nums, left, pivot_index - 1, k)
        # Else recur on the right sub-array
    else
        return quickselect(nums, pivot_index + 1, right, k)

def find_kth_largest_element(nums, k):
    # Adjust k to be the index in zero-based indexing
    return quickselect(nums, 0, len(nums) -1, len(nums) - k)