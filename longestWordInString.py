theString = input("Enter the string: ")

arr = []
arr = theString.split(" ")

length = len(arr)
i = 0
longest = ""

while i != length:
    if len(arr[i]) > len(longest):
        longest = arr[i]
    i += 1

print(longest)
