mainlist=[int(x) for x in input().split()]
templist=[]
for i in range(len(mainlist)):
    for j in range(len(mainlist)):
        if mainlist[i] == mainlist[j]:
            break
        productval = int(mainlist[i]*mainlist[j])
        templist.append(productval)

print(templist)
print(max(sorted(templist)))

# newlist = []
# while templist:
#     minimum = templist[0]
#     for x in templist:
#         if x < minimum:
#             minimum = x
#     newlist.append(minimum)
#     templist.remove(minimum)
#
# print(newlist)