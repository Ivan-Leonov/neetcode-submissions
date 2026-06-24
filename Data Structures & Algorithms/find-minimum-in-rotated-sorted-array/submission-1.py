class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while r - l > 1:
            
            m = (l + r) // 2

            print(f"l{l}, r{r}, m{m}, n_l{nums[l]}, n_r{nums[r]}, n_m{nums[m]}, rld{r-l}")
            if nums[l] <= nums[r]:
                return nums[l]
            
            if nums[m] < nums[r]:
                r = m
            elif nums[m] >= nums[r]:
                l = m
        return min(nums[l], nums[r])