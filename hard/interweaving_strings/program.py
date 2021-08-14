# time = O(nm) and space = O(nm) => n = len(str1) | m = len(str2)
def interweavingStrings(str1, str2, str3):
    if len(str1) + len(str2) != len(str3): return False

    return interweavingStringsHelper(str1, str2, str3, 0, 0, {})

def interweavingStringsHelper(str1, str2, str3, i1, i2, memo):
    if (i1, i2) in memo: return memo[(i1, i2)]

    i3 = i1 + i2
    if i3 == len(str3): return True

    pass1 = pass2 = False
    if i1 < len(str1) and str1[i1] == str3[i3]: 
        pass1 = interweavingStringsHelper(str1, str2, str3, i1+1, i2, memo)
    if i2 < len(str2) and str2[i2] == str3[i3]: 
        pass2 = interweavingStringsHelper(str1, str2, str3, i1, i2+1, memo)

    return pass1 or pass2