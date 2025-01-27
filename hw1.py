def merge(nums1, m, nums2, n):

    i, j = m - 1, n -1

    k = m + n -1
# Index for placements in num1

#Two-Point Technique Merge in Reverse Order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]

            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)