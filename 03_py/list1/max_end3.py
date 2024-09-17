def max_end3(nums):
  x = max(nums[0], nums[-1])
  nums[0], nums[1], nums[2] = x, x, x
  return nums

