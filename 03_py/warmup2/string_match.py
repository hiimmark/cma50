def string_match(a, b):
  n = min(len(a), len(b))
  ans = 0
  for i in range(n-1):
    if a[i:i+2] == b[i:i+2]:
      ans += 1
  return ans
