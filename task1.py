#gpay task
customer=["arun","rose","john","jack","maniii"]
amount=[1000,2000,3000,4000,50000]
a=input("enter the sender name:")
b=input("enter the receiver name:")
c=int(input("send the amount:"))
for i in customer:
        if(a==i):
            print("sender is available")
            Z=customer.index(i)
            print(i,"your account balance",amount[Z])
            print(i,"your balance amount",amount[Z]-c)
            print(i,"your debit amount",c)
            continue
        if(b==i):
            print("receiver is available")
            x=customer.index(i)
            print(i,"your account balance",amount[x])
            print(a,"credit your amount",amount[x]+c)
                
