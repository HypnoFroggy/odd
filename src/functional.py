def f(pos):
    pos = int(pos) - 1
    i = 1
    nums = [1, 1]
    while i < pos:
        i += 1
        nums = [nums[1], nums[0] + nums[1]]
    c = nums[0]
    if pos == 0:
        c = 0
    elif pos == -1:
        c = '#'
    return (c)
