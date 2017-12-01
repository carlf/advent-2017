def sum_pairs(nums, step_size):
    total = 0
    characters = list(nums)
    for i, c in enumerate(characters):
        compare_index = (i + step_size) % len(characters)
        if characters[compare_index] == c:
            total += int(c)
    return total
