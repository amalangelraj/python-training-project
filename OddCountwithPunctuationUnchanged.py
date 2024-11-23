def odd_Word_reverse(myString) :
    startCharacterList  = ['"','(','[','{',"'"]
    stopCharacterList   = ['"',')',']','}',"'",'.',',',':',';','?','!']
    counter=True									# Scan the first line and set the counter
    # print(counter)

    while counter:											# runs the while loop until counter becomes 0
        # myString=input()										# receive the line one by one
        myCounter=len(myString)
        if myString[0] in startCharacterList :					# check if the first character presents in the Start Character List
            if myString[-1] in stopCharacterList :				# check if the last character presents in the Stop Character List
                if myString[1] in startCharacterList :
                    if myString[-2] in stopCharacterList :
                        return (myString[0]+myString[1]+myString[-3:1:-1]+myString[-2]+myString[-1])
                elif myString[-2] in stopCharacterList:
                    return (myString[0] + myString[-3:0:-1]+myString[-2]+myString[-1])
                else:
                    return (myString[0]+myString[-2:0:-1]+myString[-1])	# Reverse by preserving the first and last character.
            else:
                return (myString[0]+myString[-1:0:-1])				# Reverse by preserving the first character only
        elif myString[-1] in stopCharacterList:					# check if the last character presents in the Stop Character List
            if myString[-2] in stopCharacterList:					# check if the last two character presents in the Stop Character List
                return (myString[-3:-myCounter-1:-1]+myString[-2]+myString[-1])
            else:
                return (myString[-2:-myCounter-1:-1]+myString[-1])				# Reverse by preserving the last character only
        else:
            return (myString[::-1])								# Reverse the whole word
        counter = False

    # print(myString[::-1])

outputString=""
myList=[x for x in input().split(" ") if x!=""]
for i in range(len(myList)):
    if not i%2  :
        outputString += (str(odd_Word_reverse(myList[i])) + " ")
    else:
        outputString += (myList[i] + " ")


print(outputString)

# mainList=[x for x in outputString.split(" ") if x!=""]
#
# print(mainList)
#
