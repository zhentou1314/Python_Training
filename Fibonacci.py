# 史少博
# 开发时间 2021/1/23 17:04
from operator import index

class Solution1(object):
    def twoSum(self):
        nums = [2, 7, 11, 15]
        target = 9
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    print("第一个下标为{}".format(i), "第二个数下标为{}".format(j))
                    return nums[i], nums[j]

class Solution(object):
    def twoSum(nums=[2,7,11,15],target=9):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    print(i, j)

    def fibonacci():
        a, b = 0, 1
        while b < 100:
            print(b)
            a, b = b, a + b
            # return b

if __name__ == "__main__":
    result = Solution.fibonacci()
    print(result)
