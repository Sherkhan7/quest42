total_size = 28625
sum_ = 0

with open('hdd_sizes.txt', 'r') as f:
    for line in range(1):
        next(f)
    for line in f:
        hdd_sizes = line.split()

for index, item in enumerate(hdd_sizes):
    hdd_sizes[index] = int(item)

hdd_sizes.sort(reverse=True)
for index, size in enumerate(hdd_sizes):
    sum_ += size
    if sum_ > total_size:
        break

print(index + 1, f'totoal_sum:{sum_} TB')
