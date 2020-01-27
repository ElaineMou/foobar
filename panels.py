import sys

def solution(xs):
    product = 1
    zeros = 0
    negatives = 0
    positives = 0

    for x in xs:
        if x == 0:
            zeros += 1
        elif x > 0:
            product *= x
            positives += 1
        else:
            negatives += 1
    if zeros > 0 and (positives == 0 and negatives < 2):
        return str(0)
    xs.sort()

    if zeros == 0 and positives == 0 and negatives == 1:
        return str(xs[0])

    i = 0
    while i + 1 < len(xs):
        if xs[i] < 0 and xs[i+1] < 0:
            product *= xs[i]
            product *= xs[i+1]
            i += 2
        else:
            break

    return str(product)

if __name__ == "__main__":
  input = map(int, sys.argv[1].strip('[]').split(','))
  print(solution(input))
