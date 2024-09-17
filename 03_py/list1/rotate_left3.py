def rotate_left3(nums):
  res = []
  for i in range(len(nums)-1):
    res.append(nums[i+1])
  res.append(nums[0])
  return res

