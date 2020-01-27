import sys

def solution(s):
    going_right = []
    going_left = []
    for i in range(len(s)):
        char = s[i]
        if char == '>':
            going_right.append(i)
        elif char == '<':
            going_left.append(i)
        else:
            continue
    
    salutes = 0
    i = 0
    j = 0
    while i < len(going_right):
        while j < len(going_left) and going_left[j] < going_right[i]:
            j += 1
        collisions = len(going_left) - j
        salutes += collisions * 2
        i += 1
    return salutes

if __name__ == "__main__":
  print(solution(sys.argv[1]))
