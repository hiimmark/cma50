def centered_average(nums):
  nums.sort()
  ans = 0
  for i in range(1, len(nums)-1):
    ans += nums[i]
  return ans / (len(nums)-2)

