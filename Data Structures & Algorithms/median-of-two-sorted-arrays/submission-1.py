class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
            - The concept is finding the right split for arr1, arr2
            - right split is when max(l1, l2) < min(r1, r2)
            - [1,3], [2,4] if the split is at index 1 for both
                - the last element in left half will be max(1,2)
                - the fisrt element in right half will be min(3,4)
                - so it's [2,3]
                - as the left and right halves have even number of elements
                - median = (2+3)//3
                - if left_count > right_count
                    median = last ele in left part
                - else
                    median = first element in right part
            '''
        n, m = len(nums1), len(nums2)
        even = (n+m)%2==0
        for i in range(n+1):
            for j in range(m+1):
                if ((even and i+j!=(n+m)//2)
                    or (not even and i+j!=(n+m)//2 + 1)):
                    continue
                l1, l2 = nums1[i-1] if i>0 else float('-inf'), nums2[j-1] if j>0 else float('-inf')
                r1, r2 = nums1[i] if i<n else float('inf'), nums2[j] if j<m else float('inf')
                if max(l1,l2) > min(r1,r2):
                    continue
                if even:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
        return -1
                    
        