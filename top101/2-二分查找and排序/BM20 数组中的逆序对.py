MOD = 1000000007


def merge_count(nums, l, mid, r):
    if l >= r:
        return 0
    tmp = []
    i = l
    j = mid + 1
    cnt = 0
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            cnt = (cnt + (mid - i + 1)) % MOD
            tmp.append(nums[j])
            j += 1

    while i <= mid:
        tmp.append(nums[i])
        i += 1

    while j <= r:
        tmp.append(nums[j])
        j += 1

    for k in range(l, r + 1):
        nums[k] = tmp[k - l]

    return cnt


def calcZoneInverserPairs(nums, l, r):
    if l >= r:
        return 0
    mid = (l + r) // 2
    lc = calcZoneInverserPairs(nums, l, mid)
    rc = calcZoneInverserPairs(nums, mid + 1, r)
    cc = merge_count(nums, l, mid, r)

    return (lc + rc + cc) % MOD


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def InversePairs(self, nums: List[int]) -> int:
        # write code here
        n = len(nums)
        if n < 2:
            return 0
        return calcZoneInverserPairs(nums, 0, n - 1)
