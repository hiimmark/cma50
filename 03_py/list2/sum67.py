def sum67(nums):
  state = False
  ans = 0
  for x in nums:
    if x == 6 and not state:
      state = not state
    elif x == 7 and state:
      state = not state
    elif not state:
      ans += x
  return ans

