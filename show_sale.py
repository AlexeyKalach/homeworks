import sys
nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as v:
    if len(nums) > 1:
        start_idx = int(nums[0])
        finish_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        finish_idx = sum(1 for line in v)
        v.seek(0)
    else:
        start.idx = int(nums[1])
        finish_idx = sum(1 for line v)
        v.seek(0)

    for idx, line in enumerate(v):
        if start_idx <= idx + 1 <= finish_idx:
            print(line.strip())
