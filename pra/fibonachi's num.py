myl = []

def fibona(sequence):
    if sequence == 1:
        myl.append(a)

    elif sequence > 1:
        myl.append(0)
        myl.append(1)
        for num in range(2 , sequence):
            new_num =myl[num-2] + myl[num - 1]
            myl.append(new_num)
           
    return myl
   
    

sequence = int(input("Enter the amount of sequence: "))

result = fibona(sequence)

print(result)