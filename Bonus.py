from collections import Counter

B = {2, 3, 11, 17, 23, 31, 43, 53, 67, 71, 79, 83, 107}
sorted_B = sorted(B)


def create_binary_vector(line):
    values = [int(x) for x in line.replace(",", "").split()]
    value_counter = Counter(values)
    vector = [value_counter[value] for value in sorted_B]
    return vector


file_path = "D:/vectors.txt"
with open(file_path, "r") as file:
    lines = [line.strip() for line in file.readlines() if line.strip()]

binary_vectors = [create_binary_vector(line) for line in lines]
for line, vector in zip(lines, binary_vectors):
    print(f"{vector}")
    print()
