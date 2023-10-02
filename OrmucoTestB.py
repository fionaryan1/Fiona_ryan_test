# Question B 
# The goal of this question is to write a software library that accepts 2 version string 
# as input and returns whether one is greater than, equal, or less than the other. 
# As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of. 


def compareVersion(version1, version2):

    v1 = version1.split('.')
    v2 = version2.split('.')

    while len(v1) < len(v2):
        v1.append(0)
    while len(v1) > len(v2):
        v2.append(0)


    for i in v1:
        for j in v2:
            if i < j:
                return version1 + " is less than " + version2
            elif j < i:
                return version1 + " is greater than " + version2
            
    
    return version1 + " is equal to " + version2


version_1 = input("Please input a version1 string: ")
version_2 = input("Please input a version2 string: ")

result = compareVersion(version_1, version_2)

print(result)


