def main():
    x = int(input('what is x?'))

    if is_even(x):
        print('Even')
    else:
        print('odd')

def is_even(n):
    return True if n % 2 ==0 else False

main()
    