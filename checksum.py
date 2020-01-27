import sys

def xor_0_to(n):
    return [n, 1, n+1, 0][n%4]

def xor_from(a, b):
    return xor_0_to(b) ^ xor_0_to(a-1)

def solution(start, length):
    xor = 0
    for i in range(length):
        first = start + i*length
        last = first + length - 1 - i
        xor_row = xor_from(first,last)
        xor ^= xor_row
    return xor

if __name__ == "__main__":
	print(solution(int(sys.argv[1]),int(sys.argv[2])))