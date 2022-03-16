array = [0,1,0,0,4,5,6,7,0,8,-4,0]
input = [1,4,5,6,7,8,-4]
i=set(input)
print([x for x in array if x not in i])