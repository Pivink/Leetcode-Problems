def majority(nums):
    counts = {}
    
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    majority_element = max(counts, key=counts.get)
    
    print(majority_element)

# Test the function
majority([1, 1, 1, 2, 3, 3])
