name="dhrithi kashyap h r"
freq={}

for i in name:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("count"+str(freq))