array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 99]
def linear(l, t):
        nTries = 0
        for i in l:
            if i == t:
                return nTries
            nTries += 1

def binary(l, t): #t is the target we are looking for in the array
    nTries = 1
    m = int(len(l)/2)
    while True:
        if t == l[m]:
            return nTries
        elif t > l[m]:
            l = l[int(m):]
            m = int(len(l)/2)
            nTries += 1

        elif t < l[m]:
            l = l[:int(m)]
            m = int(len(l)/2)
            nTries += 1

# let's try how many times it takes to find each element of a range 0 - 99
linearTotalTries = 0
binaryTotalTries = 0
for target in range(100):
    linearTotalTries += linear(array, target)
    binaryTotalTries += binary(array, target)
print('It took the linear algorithm ' + str(linearTotalTries) + ' to find the all the targets in the array')
print('It took the binary algorithm ' + str(binaryTotalTries) + ' to find the all the targets in the array')
        
