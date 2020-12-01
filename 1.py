nums = [int(x) for x in open('1.txt').read().splitlines()]
len_nums = len(nums)
for i in range(len_nums):
    for j in range(i+1, len_nums):
        if nums[i] + nums[j] == 2020:
            print('Part one: ' + str(nums[i] * nums[j]))
        for k in range(j+1, len_nums):
            if nums[i]+nums[j]+nums[k] == 2020:
                print('Part Two: ' + str(nums[i] * nums[j] * nums[k]))
