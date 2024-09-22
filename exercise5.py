def call():
    try:
        print("connection open to database")
        a=list(input("Enter a list\n"))
        b=int(input("enter index number\n"))
        print(a[b])
        
    except Exception as e:
        
        print("The error occured is",e)
      
        
    
    finally:
        print("connection closed to database")
call()
        
        
