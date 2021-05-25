class Solution:
    def massage(self, nums) -> int:
        if len(nums) == 0:
            return 0
        max_result = []
        for i in range(len(nums)):

            max_result.append(0)
        for i in range(len(nums)):
            temp_list = nums[0:i+1]
            if len(temp_list) == 1:
                max_result[i] = nums[0]
            elif len(temp_list) == 2:
                max_result[i] = max(temp_list)
            elif len(temp_list) == 3:
                max_result[i] = max([nums[i]+max_result[i-2],max_result[i-1]])
            else:
                max_result[i] = max([nums[i]+max_result[i-3],nums[i]+max_result[i-2],max_result[i-1]])
        return max_result[-1]

if __name__ == '__main__':
    nums = [1,1,1,2]

    a = Solution().massage(nums)
    print(a)

