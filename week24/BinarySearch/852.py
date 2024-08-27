class Solution(object):
    def find_peak(self,arr):
        left,right = 0, len(arr)-1

        while left<right:
            mid=(left+right)//2
            if arr[mid]>arr[mid+1]:
                right=mid
            else:
                left= mid+1
        return left
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        peak_el=Solution().find_peak(arr)
        left,right=0,peak_el
        while left < right:
            mid=(left+right)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right=mid
        return left
my_obj=Solution()