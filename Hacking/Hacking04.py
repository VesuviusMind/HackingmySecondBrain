# leetcode 01
# 给定一个整数数组nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# 暴力法和哈希表法
nums=[2,7,11,15]
target=9
def twoSum(nums,target):
    #暴力法
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i]+nums[j]==target:
    #             return [i,j]
    #哈希表法
    hashmap={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[num]=i
        
print(twoSum(nums,target))
# but i actually donot know why this code works kinda?I guess
# i just wander whether this is a apropriate way to learn python  just the minProject or the leetcode