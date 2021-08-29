sample=[1,2,3,4,5,6,7,8,9]
while len(sample)>2:
    print(sample[2])
    sample.remove(sample[2])
    if (len(sample)>2):
        print(sample)