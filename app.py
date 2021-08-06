# 1. write a function that takes in three variables and checks if any two are equal. Returns true if any two are equal and returns false otherwise
def check(a,b,c):
    if a == b or a == c or b == c:
        return True
    else:
        return False

# 2. write a function that takes a number as input and returns true if the number is a prime number and false if it is not a prime number
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

# 3. write a function that takes in an array as input, removes any duplicate found in the array and returns the resulting array without duplicate
def removeDuplicate(arr):
    arr = list(arr)
    arr2 = list(dict.fromkeys(arr))
    return arr2

# 4. Write a function that takes an array and an integer as input, return any two numbers in the array that when summed up, will be equal to the value of the integer
def sumPairs(arr, n, sum):
    pairs = []

    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                pairs.append(arr[i])
                pairs.append(arr[j])
                break
    return pairs[2:]

def checkTwoNumbersInArray(arr, sum):
    n = len(arr)
    return sumPairs(arr, n, sum)

testArray = [1,5,7,-1,5]
test_number = 6
print(checkTwoNumbersInArray(testArray, test_number))


# 5. write a function that takes in a string as input and checks if it's a palindrome. Returns True if its a palindrome and False if it isn't.
def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False

# Bonus. Write a function that takes in an array and returns True if the array contains any duplicate value, or False if it doesn't contain any duplicate value
def checkDuplicate(arr):
    if len(arr) != len(set(arr)):
        return True
    else:
        return False


arr = [1,2,3,3,4,5,5,6,6,6,6,6,6,6,6,7,8]
if __name__ == '__main__':
    print(check(2,3,3))
    print(isPrime(3))
    print(removeDuplicate(arr))
    print(checkTwoNumbersInArray(testArray, test_number))
    print(palindrome('Hannah'))
    print(checkDuplicate(arr))