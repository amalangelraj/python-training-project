def canPalindromeBeFormed(alphaNumericString):
    if alphaNumericString.isdigit():
        listUpperCaseData=[0 for i in range(10)]
        print(listUpperCaseData)
        print(alphaNumericString)
        # count the alphabets & numbers
        for character in alphaNumericString:
            print(character, "ASCII is:", ord(character), "after -48 we find :", character, "is in", ord(character)-48+1, "th place, with index", ord(character)-48, "in the alpha list")
            print(listUpperCaseData)
            listUpperCaseData[ord(character)-48]+=1
            print("Hence updating that index value by +1, now list become")
            print(listUpperCaseData, "\n")
        # apply the odd or even policies
        oddCount=0
        for i in range(10):
            print("index:", i, "value is:",listUpperCaseData[i])
            if listUpperCaseData[i]%2: # ODD Filter
                oddCount+=1
                print("oddount value in outer if is", oddCount, "and is greater than 1?", oddCount > 1)

                if oddCount > 1:
                    print("oddount value in inner if is", oddCount)
                    print("Returning No")
                    return "NO"
            print("oddCount value in for loop is", oddCount)
        return "YES"

    else:
        listUpperCaseData=[0 for i in range(26)]
        print(listUpperCaseData)
        print(alphaNumericString)
        # count the alphabets & numbers
        for character in alphaNumericString:
            print(character, "ASCII is:", ord(character), "after -65 we find :", character, "is in", ord(character)-65+1, "th place, with index", ord(character)-65, "in the alpha list")
            print(listUpperCaseData)
            listUpperCaseData[ord(character)-65]+=1
            print("Hence updating that index value by +1, now list become")
            print(listUpperCaseData, "\n")
        # apply the odd or even policies
        oddCount=0
        for i in range(26):
            print("index:", i, "value is:",listUpperCaseData[i])
            if listUpperCaseData[i]%2: # ODD Filter
                oddCount+=1
                print("oddount value in outer if is", oddCount, "and is greater than 1?", oddCount > 1)

                if oddCount > 1:
                    print("oddount value in inner if is", oddCount)
                    print("Returning No")
                    return "NO"
            print("oddCount value in for loop is", oddCount)
        return "YES"
print(canPalindromeBeFormed(input()))