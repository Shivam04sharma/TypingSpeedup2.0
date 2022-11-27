while True:
    print("#"*60)
    print('''# Press:
> S or s to start
> E or e to exit''')
    print("-"*60)
    z=input("Enter the command: ")
    if z in "Ss":
        import random
        import time
        print("*"*60)
        a1=time.time()
        n=int(input("Enter the no. of rounds:"))
        print("-"*60)
        b1=[]
        b2=[]
        b3=["@","$","?","&","=","+"]
        for i in range(65,91):
            b1.append(chr(i))
        for j in range(97,123):
            b2.append(chr(j))
        r2=0
        for k in range(1,n+1):
            c=random.randint(4,5)
            d=random.choice(b1)
            d2=random.choice(b3)
            d3=random.randint(1,10)
            a2=random.choice(b2)
            f=a2
            g=random.randint(2,4)
            g2=random.randint(2,4)
            g3=random.randint(2,4)
            for l in range(1,c+1):
                e=random.choice(b2)
                if l==g2 and g2<=c:
                    f=f+d2
                if l==g3 and g3<=c:
                    f=f+str(d3)
                if l==g and g<=c:
                    f=f+d
                else:
                    f=f+e
            print("# Type the given(round-"+str(k)+"):",f)
            r=input(">>> ")
            while r!=f:
                r2=r2+1
                print("! Wrong input")
                print("Type again(round-",k,"):",f)
                r=input("> ")
        print("*"*60)
        print(" "*20,"-"*5,"SUMMARY","-"*5)
        print()
        a2=time.time()
        a3=int(a2-a1)
        print("-Effective round played:",n)
        print("-Wrong inputs:",r2)
        print("-Total round(right+wrong):",n+r2)
        print("-Total time taken:",a3//60,"Minute",a3%60,"Second")
        print()
        print("*"*14,"Time taken:",a3//60,"Minute",a3%60,"Second","*"*14)
        print()
    elif z in "Ee":
        print("#"*60)
        break
    else:
        print("-"*60)
        print("! Invalid Input, Try Again...")