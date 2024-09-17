def last2(str):
  if len(str) < 2:
    return 0
  else:
    ans = 0
    s = str[len(str)-2:];
    for i in range(len(str)-2):
      if str[i:i+2] == s:
        ans += 1
    return ans
