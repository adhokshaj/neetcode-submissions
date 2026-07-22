class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(l,r,m):
            temp = []
            a,b,n = l,m+1, len(nums)
            while a<=m and b<=r:
                if nums[a]<nums[b]:
                    temp.append(nums[a])
                    a += 1
                else:
                    temp.append(nums[b])
                    b += 1
            
            while a<=m:
                temp.append(nums[a])
                a += 1

            while b<=r:
                temp.append(nums[b])
                b += 1
            a = l
            for i,num in enumerate(temp):
                nums[a] = num
                a += 1


        def merge(l,r):
            # print(l,r)
            if l==r:
                return
            m = (l+r)//2
            merge(l,m)
            merge(m+1,r)
            sort(l,r,m)

        merge(0,len(nums)-1)
        return nums
        
        
