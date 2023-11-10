def pattern_indices(text, pattern):
    indices = []
    i = 0
    while i < len(text):
        if text[i:i + len(pattern)] == pattern:
            indices.append(i)
            i += len(pattern) - 1
        i += 1
    return indices

text = "ABABCDABCABCDBDCABBABABAABCD"
pattern = "ABCD"
indices = pattern_indices(text, pattern)

print("Indices of the first 'A' in each appearance of", pattern, "are:", indices)
