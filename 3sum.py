num_array = list(map(int,input().split(",")))
target = int(input("Enter the target number"))

num_array.sort()
print(num_array)
output =[]
presumed = abs(target- (num_array[0]+num_array[1]+num_array[2]))
threesum=num_array[0]+num_array[1]+num_array[2]
for i in range(len(num_array)-2):
    if((abs(target-(num_array[i]+num_array[i+1]+num_array[i+2])))<=(presumed)):
        output[:]=[]
        presumed = abs(target-(num_array[i]+num_array[i+1]+num_array[i+2]))
        output.append(num_array[i]) #Redundant
        output.append(num_array[i+1])
        output.append(num_array[i+2])
        threesum = num_array[i]+num_array[i+1]+num_array[i+2]


num_array1 = list(set(num_array))
num_array1.sort()
presumed1 = abs(target-(num_array1[0]+num_array1[1]+num_array1[2]))
threesum1 = num_array1[0]+num_array1[1]+num_array1[2]
print(num_array1)
for i in range(len(num_array1)-2):
    if((abs(target-(num_array1[i]+num_array1[i+1]+num_array1[i+2])))<=(presumed1)):
        output[:]=[]
        presumed1 = abs(target-(num_array1[i]+num_array1[i+1]+num_array1[i+2]))
        output.append(num_array1[i]) #Redundant
        output.append(num_array1[i+1])
        output.append(num_array1[i+2])
        threesum1 = num_array1[i]+num_array1[i+1]+num_array1[i+2]
print(threesum1)
print(threesum)
if(abs(target-threesum)<abs(target-threesum1)):
    print(threesum)
else:
    print(threesum1)
