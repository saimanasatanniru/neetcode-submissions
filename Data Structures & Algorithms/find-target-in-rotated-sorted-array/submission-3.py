class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[right]:
                if nums[left] <= target < nums[mid]: #if the target belong to the left half
                    right = mid - 1 #then we discard the right half and search in left half
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: #the target is in the right half 
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        