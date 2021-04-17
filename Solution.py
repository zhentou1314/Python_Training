class Solution2:
    def __init__(self,a,b):
        print(a,b)

    def test(self, nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return nums.index(i)
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)

# class Solution1(object):
#     def twoSum(self, nums=[2, 7, 11, 15], target=9):
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     print("第一个下标为{}".format(i), "第二个数下标为{}".format(j))
#                     return nums[i], nums[j]
# def searchInsert():
#     return None
