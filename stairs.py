import sys

def splits_n_taller_than(n, lower_step):
    small_half = (n-1) // 2
    big_half = n - small_half

    start = n - lower_step - 1
    end = big_half - 1
    if start <= end:
        return []

    splits = []
    for i in range(start, end, -1):
        splits.append((i, n - i))
    return splits

def solution(n):
    tall_stairs = {}
    old_staircases = {(n,0) : 1}
    count = 0
    while True:
        new_dict = {}

        for small_stairs in old_staircases:
            taller_halves = tall_stairs.get(small_stairs)
            if not taller_halves:
                taller_halves = splits_n_taller_than(small_stairs[0],small_stairs[1])
                tall_stairs[small_stairs] = taller_halves

            small_stairs_count = old_staircases.get(small_stairs)
            for tall_half in taller_halves:
                if tall_half not in new_dict:
                    new_dict[tall_half] = small_stairs_count
                else:
                    new_dict[tall_half] = new_dict[tall_half] + small_stairs_count
                count += small_stairs_count
        if not new_dict:
            break
        old_staircases = new_dict
    return count

if __name__ == "__main__":
    print(solution(int(sys.argv[1])))