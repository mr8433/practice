question=["Who is the prime minister\n 1.J.Nehru 2.Indira 3.Abdul Kalam 4.N.Modi\n ","Who is President\n 1.Pratibha Patil 2.Pranab Mukherjee 3.Ram Nath govind 4.Draupdi Murmu\n","What is the capital of india\n 1.New Delhi 2.Dehradun 3.Gurgaon 4.Mumbai",]
answers=["N.Modi","Draupdi Murmu","New Delhi"]

l=0
for i in question:
    print(i)
    
    ans=input("Enter the correct answer\n")
    if ans in answers:
        print("Right answer,100 credited")
        
    else:
        print("wrong answer,eliminated")
    l+=1
if l>0:
    
    print("Money Taken home",l*100)
else:
    print("You are eliminated")
