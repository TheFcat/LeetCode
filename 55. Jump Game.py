class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1:
            return True
        check_point = {0: -1}
        target = len(nums) - 1
        point = 0
        max_point = 0
        while True:
            while nums[point] != 0:
                point += nums[point]
                if point >= target:
                    return True

            max_point = max(max_point, point)
            while point + nums[point] <= max_point:
                point -= 1
                if point in check_point:
                    point = check_point[point]
                if point < 0:
                    return False

            check_point[max_point] = point


print(Solution().canJump([3,2,1,0,4]))