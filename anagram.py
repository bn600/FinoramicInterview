A = input().split(",")
output=[]

def duplicates(A, a):
   return [i for i, x in enumerate(A) if x == a]

for i in range(len(A)):
    A[i] = ''.join(sorted(A[i]))

for i in A:
    a = duplicates(A,i)
    a = [x+1 for x in a]
    if a not in output:
        output.append(a)
    print(output)

#Second Approach
'''def anagram_check(a,b):
    a =''.join(sorted(a))
    b =''.join(sorted(b))
    for i in range(len(a)):
        if(a[i]!=b[i]):
            return False
    return True'''
'''length=[]
a= []
if(len(A)==1):
    output.append([1])

for i in A:
    length.append(len(i))
# print(length)

for i in range(len(length)):
    for j in range(i+1,len(length)):
        if length[i]==length[j]:
            # print("into func")
            d = anagram_check(A[i],A[j])
            if(d):
                # print("true case")
                if(len(output)!=0):
                    for k in range(len(output)):
                        if i+1 in output[k]:
                            # print(output[k])
                            if j+1 not in output[k]:
                                output[k].append(j+1)
                        elif(j+1 in output[k]):
                            # print(output[K])
                            if i+1 not in output[k]:
                                output[k].append(i+1)
                        else:
                            # print(i,j)
                            output.append([i+1,j+1])
                else:
                    output.append([i+1,j+1])




for i in range(1,len(A)+1):
    for j in range(len(output)):
        if i in output[j]:
            break
        if(j==(len(output)-1)):
            output.append([i])'''


'''print(output)'''
