inputString = raw_input("Enter a String").lower().replace(" ","")
frequency = {}
for x in inputString:
    if x in frequency:
        frequency[x]+=1
    else:
        frequency[x]=1
frequency =sorted(frequency,key=lambda x : frequency[x],reverse=True)
print frequency
