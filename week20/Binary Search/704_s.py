class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarysearch(left,right,target):
            if left<=right:
                mid = (left+right)//2
                if nums[mid]>target:
                    return binarysearch(left,mid-1,target)
                elif nums[mid]<target:
                    return binarysearch(mid+1,right,target)
                else:
                    return mid
            else:
                return -1


        return binarysearch(0,len(nums)-1,target)
