
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Stores the smallest possible ending value
        # of an increasing subsequence of each length.
        # tails[i] represents a subsequence of length i + 1.
        tails = []

        # Process every number in the input array.
        for num in nums:

            # Binary search boundaries.
            # We search for the first position where tails[pos] >= num.
            left, right = 0, len(tails)

            # Binary search to find the lower bound.
            while left < right:

                # Find the middle index.
                mid = (left + right) // 2

                # If the middle value is smaller than num,
                # num must be placed somewhere to its right.
                if tails[mid] < num:
                    left = mid + 1

                # Otherwise, the middle value could be our answer.
                # Continue searching in the left half.
                else:
                    right = mid

            # If left reaches the end of tails,
            # num is greater than every existing tail.
            # So we can extend the increasing subsequence length.
            if left == len(tails):
                tails.append(num)

            # Otherwise, replace the first value >= num.
            # A smaller ending value gives more opportunities
            # to extend an increasing subsequence later.
            else:
                tails[left] = num

        # The number of elements in tails represents
        # the length of the longest increasing subsequence.
        return len(tails)
