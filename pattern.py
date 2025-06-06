def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    width = 4 * size - 3
    lines = []

    for i in range(size):
        left = list(alpha[size-1 : i : -1]) + [alpha[i]]
        right = list(alpha[i+1 : size])
        s = '-'.join(left + right)
        lines.append(s.center(width, '-'))

    full_rangoli = lines[::-1] + lines[1:]

    for line in full_rangoli:
        print(line)


# your code goes here
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
