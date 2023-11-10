def count_swaps(s1, s2):
    if len(s1) != len(s2):
        return -1  

    s1 = list(s1)
    s2 = list(s2)
    swaps = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            for j in range(i + 1, len(s1)):
                if s1[j] == s2[i]:
                    s1[i], s1[j] = s1[j], s1[i]
                    swaps += 1
                    break

    return swaps

input_str = "MOM"
output_str = "MMO"

swaps_required = count_swaps(input_str, output_str)

if swaps_required == -1:
    print("Strings must be of the same length")
else:
    print(f"Minimum swaps required: {swaps_required}")
