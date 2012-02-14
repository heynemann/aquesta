def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib (n - 2)

def main(argv):
    print fib(int(argv[1]))

    return 0

def target(driver, args):
    return main, None

if __name__ == '__main__':
    import sys
    main(sys.argv)
