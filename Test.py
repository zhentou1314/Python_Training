# 史少博
# 开发时间 2021/4/17 19:42
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
def test(self,nums,target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return nums.index(i)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

if __name__ == '__main__':
    result = test([1, 3, 5, 7],5)
    print(result)
