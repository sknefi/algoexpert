# difficulty: 2/4

# string: "1921680"

# output: [ "1.9.216.80",
#           "1.92.16.80",
#           "1.92.168.0",
#           "19.2.16.80",
#           "19.2.168.0",
#           "19.21.6.80",
#           "19.21.68.0",
#           "19.216.8.0",
#           "192.1.6.80",
#           "192.1.68.0",
#           "192.16.8.0" ]

def isIpValid(ipAddress):
    if len(ipAddress) >= 2 and ipAddress[0] == '0':
        return False

    if 0 <= int(ipAddress) <= 255:
        return True

    return False


def convertStringToIpAddress(pointer1, pointer2, pointer3, string):
    dot = '.'
    newIpAddress = (string[:(pointer1)] + dot + string[(pointer1):(pointer2)] +
                    dot + string[(pointer2):(pointer3)] + dot + string[(pointer3):])

    return newIpAddress


def couldStringBeIpAddress(ipAddress):
    if len(ipAddress) >= 4:
        return True

    return False


def validIPAddresses(string):
    if not couldStringBeIpAddress(string):
        return []

    ptr1 = 1
    ptr2 = 2
    ptr3 = 3
    result = []

    for _ in range(0, 4):
        if isIpValid(string[0:ptr1]):
            if isIpValid(string[ptr1:ptr2]):
                for _ in range(0, 4):
                    if isIpValid(string[ptr1:ptr2]) and ptr2 < len(string):
                        if isIpValid(string[ptr2:ptr3]):
                            for _ in range(0, 4):
                                if isIpValid(string[ptr2:ptr3]) and ptr3 < len(string):
                                #if isIpValid(string[ptr2:ptr3]):
                                    if isIpValid(string[ptr3:(len(string))]):
                                        result.append(convertStringToIpAddress(ptr1, ptr2, ptr3, string))
                                else:
                                    break
                                ptr3 += 1
                    else:
                        break
                    ptr2 += 1
                    ptr3 = ptr2 + 1
            ptr1 += 1
            ptr2 = ptr1 + 1
            ptr3 = ptr2 + 1
        else:
            break

    return result
