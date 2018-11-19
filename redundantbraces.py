input_string = input("Enter the String")
'''count_op = 0;
count_braces = 0;
op = '+' or '*' or '-' or '/'
for i in input_string:
    print(i)
    if i=='*' or i=='+' or i=='-' or i=='/':
        print(i)
        count_op = count_op+1

    if i=='(':
        print(i)
        count_braces = count_braces+1
print(count_op)
print(count_braces)
if(count_braces == 0):
    print(0)
elif(count_op>=count_braces):
    print(0)
else:
    print(1)'''


# Stack implementation
a=[]
redundant = False
for i in input_string:
    if i==')':
        top = a.pop()
        redundant = True
        while(top!='('):
            if top =='*' or top=='+' or top=='-' or top=='/':
                redundant = False
            top = a.pop()
        if redundant:
            print(1)
    else:
        a.append(i)
if (redundant==False):
    print(0)
