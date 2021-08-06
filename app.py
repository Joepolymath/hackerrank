# write a function that takes in three variables and checks if any two are equal. Returns true if any two are equal and returns false otherwise

def check(a,b,c):
    if a == b or a == c or b == c:
        return True
    else:
        return False

# write a function that takes a number as input and returns true if the number is a prime number and false if it is not a prime number

def isPrime(x):
    num = 13
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False

if __name__ == '__main__':
    print(check(2,3,3))
    print(isPrime(3))