def sum13(nums):
  ans = 0
  i = 0
  while i < len(nums):
    while nums[i] == 13:
      i += 2
      if i >= len(nums):
        break
    if i >= len(nums):
      break
    ans += nums[i]
    i += 1
  return ans

