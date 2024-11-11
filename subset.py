from itertools import combinations
def subset(s):
    subsets = []
    for i in range(len(s) + 1):
        subsets.extend(combinations(s, i))
        print(subsets)
    return [list(j) for j in subsets]
print(subset([1, 2, 2]))