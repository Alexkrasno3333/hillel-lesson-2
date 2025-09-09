res = []

num2 = [1,2,3,4,5,6]

if len(num2) > 0:
    split = round(len(num2)/2+0.1)
    firstlst = num2[:split]
    secondlst = num2[split:]
    res.append(firstlst)
    res.append(secondlst)
    print(res)
else:

    if len(num2) == 0:
        split2 = round(len(num2)/2)
        firstlst1 = num2[:split2]
        secondlst1 = num2[split2:]
        res.append(firstlst1)
        res.append(secondlst1)
        print(res)