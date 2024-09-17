def count_evens(nums):
  ans = 0
  for x in nums:
    ans += (x % 2) ^ 1
  return ans

