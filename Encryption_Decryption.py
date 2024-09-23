
a=input("enter the message\n")
y=a
def code():
    
    global a
    if len(a)==3:
        a= a.__add__(a[0])
        print(a)
        a=a.replace(a[0],'',1)
        print(a)
        b=input("enter any 3 random words to add at starting\n")
        c=input("enter any 3 random words to add at end\n")
        if len(b)>3 or len(c)>3:
           print("invalid string")
        else:
            a=b+a+c
            
            print("String encrypted")
            return a
    else:
         a=a[::-1]
         
         print("string encrypted")
         return a
         

  
result=code()
print(result)
def decode():
    global result
    global y
    print(y)
    if len(y)==3:
        result=result[3:6]
        print(result)
        result=f'{result[-1]}{result}'
        print(result)
        result=result[0:3]
        print("Congrats! here is your original string",result)
         
    else:
        result=result[::-1]
        print(result)

decode()        
