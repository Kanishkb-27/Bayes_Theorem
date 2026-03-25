def find(a,b):
    if a==1:
        p_a=0.2
        if b==1:
            pga=0.85
        elif b==2:
            pga=0.15
        else:
            print("Invalid")
        p_a_and_b=p_a*pga
        print("Probability of b given a is",pga)
        print("Probability of both events occurring is",p_a_and_b)
    elif a==2:
        p_a=0.8
        if b==1:
            pga=0.02
        elif b==2:
            pga=0.98
        else:
            print("Invalid")
        p_a_and_b=p_a*pga
        print("Probability of b given a is",pga)
        print("Probability of both events occurring is",p_a_and_b)
    else:
        print("Invalid")
print("Let's calculate the probability")
print("Person has strep throat? \n 1.Yes 2.No")
a=int(input("Enter your choice 1/2"))
print("Person has tested positive? \n 1.Yes 2.No")
b=int(input("Enter your choice 1/2"))
print("Probability of event a and b")
find(a,b)