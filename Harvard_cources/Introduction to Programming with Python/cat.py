
def main():
    number =get_number()
    meaw(number)

def get_number ():
    while True:
        n=int(input("whats n"))
        if n >0:
            break
    return n

def meaw(n):
    for _ in range(n):
        print("good")
        print("bye")
