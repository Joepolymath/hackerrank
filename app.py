# write a function that takes in three variables and checks if any two are equal. Returns true if any two are equal and returns false otherwise

def check(a,b,c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


if __name__ == '__main__':
    print(check(2,3,3))