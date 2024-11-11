def water(heights):
    l = 0
    r = len(heights) - 1
    max_c = 0
    while l < r:
        lh = heights[l]
        rh = heights[r]
        min_h = min(lh, rh)
        max_c = max(max_c, min_h * (r - l))
        if lh > rh:
            r -= 1
        else:
            l += 1
    return max_c

l = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Container with max water for {} has a volume of {}".format(l, water(l)))
