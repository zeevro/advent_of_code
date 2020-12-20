adapters = [49, 89, 70, 56, 34, 14, 102, 148, 143, 71, 15, 107, 127, 165, 135, 26, 119, 46, 53, 69, 134, 1, 40, 81, 140, 160, 33, 117, 82, 55, 25, 11, 128, 159, 61, 105, 112, 99, 93, 151, 20, 108, 168, 2, 109, 75, 139, 170, 65, 114, 21, 92, 106, 162, 124, 158, 38, 136, 95, 161, 146, 129, 154, 121, 86, 118, 88, 50, 48, 62, 155, 28, 120, 78, 60, 147, 87, 27, 7, 54, 39, 113, 5, 74, 169, 6, 43, 8, 29, 18, 68, 32, 19, 133, 22, 94, 47, 132, 59, 83, 12, 13, 96, 35]

adapters.sort()

def get_diffs(l):
    diffs = [0, 0, 0, 1]
    last = 0

    for a in adapters:
        diffs[a - last] += 1
        last = a

    return diffs

diffs = get_diffs(adapters)

print(diffs[1] * diffs[3])


## Don't know if solution for part 2 is correct. Either of my attempts take too much time to run.

def count_all_valid_slow(l, start=1):
    ret = 1
    for i in range(start, len(l) - 1):
        if l[i + 1] - l[i - 1] <= 3:
            ret += count_all_valid_slow(l[:i] + l[i + 1:], i)
    return ret

def count_all_valid(l, places=None):
    # print(len(l), places)
    if places is None:
        places = list(filter(lambda i: l[i + 1] - l[i - 1] <= 3, range(1, len(l) - 1)))
    if not places:
        return 1
    ret = 1
    for p, i in enumerate(places):
        ret += count_all_valid(l[:i] + l[i + 1:], places[p + 1:])
    return ret

print(count_all_valid(adapters))
