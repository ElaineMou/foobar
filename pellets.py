import sys

from collections import deque

def solution(n):
    q = deque()
    seen_numbers = set()
    q.append((int(n), 0))
    seen_numbers.add(int(n))

    while True:
        value, distance = q.popleft()
        # print("{}, {}".format(value,distance))
        if value == 1:
            return distance

        values = [value+1, value-1]
        if value % 2 == 0:
            values.append(value/2)

        for x in values:
            if not (x in seen_numbers):
                q.append((x, distance + 1))
                seen_numbers.add(x)

if __name__ == "__main__":
    print(solution(sys.argv[1]))
    print(solution('15'))
    print(solution('4'))
