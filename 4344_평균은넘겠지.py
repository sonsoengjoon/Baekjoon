c = int(input())

for _ in range(c) :
  nums = list(map(int, input().split()))
  avg = sum(nums[1:]) / nums[0]
  count = 0

  for score in nums[1:] :
    if score > avg :
      count += 1

  result = count / nums[0] * 100
  print('%.3f'% result+'%')