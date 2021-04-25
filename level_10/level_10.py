distance = 0
regions_dict = dict()

with open('regions.txt', 'r') as f:
    for line in f:
        if line[-1] == '\n':
            line = line[:-1]
        direction = line.split()
        if not direction[0] in regions_dict:
            regions_dict[direction[0]] = {int(direction[-1]): direction[2]}
        else:
            regions_dict[direction[0]].update({int(direction[-1]): direction[2]})

        if not direction[2] in regions_dict:
            regions_dict[direction[2]] = {int(direction[-1]): direction[0]}
        else:
            regions_dict[direction[2]].update({int(direction[-1]): direction[0]})

visiteds = ['Namangan']
origin = visiteds[0]

for i in range(0, 7):
    check = True
    kms = list(regions_dict[origin].keys())

    while check:
        min_km = min(kms)
        point = regions_dict[origin][min_km]

        if point in visiteds:
            kms.remove(min_km)
        else:
            distance += min_km
            visiteds.append(point)
            origin = visiteds[-1]
            break

print(visiteds)
print(distance)
