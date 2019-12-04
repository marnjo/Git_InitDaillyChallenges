print("Enter the palindrome")
palindrome = input()
length = len(palindrome)
i = 0
j = -1

def isPalindrome(palindrome,length,i,j):
    while i <= (length/2):
        if palindrome[i] != palindrome[j]:
            return False
        i += 1
        j -= 1
    return True

ans = isPalindrome(palindrome,length,i,j)

if ans:
    print(f"{palindrome} is a palindrome")
else:
    print(f"{palindrome} is not a palindrome")



