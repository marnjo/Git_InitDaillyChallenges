theString = input("Enter the string: ")

length = len(theString)
print(length)


def findPermutations(theString,length):
    print(theString)
    product = length
    while length > 1:
        length -= 1
        product *= length
    print("The number of times is " + str(product))

def permutations(theString,step = 0):
    if step == len(theString):
        # we have gotten to the end print the String
        print ("".join(theString))
    for i in range(step,len(theString)):
        theStringCopy = [c for c in theString]
        theStringCopy[step], theStringCopy[i] = theStringCopy[i], theStringCopy[step]
        permutations(theStringCopy,step + 1)

findPermutations(theString,length)
print(permutations(theString))
