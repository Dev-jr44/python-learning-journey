print("This program tests a hypothesis by a German mathematician named Lothar Collatz, which states;")
print("""
1.  Take any non-negative and non-zero integer number and name it c0;
2.  If it's even, evaluate a new c0 as c0 ÷ 2;
3.  Otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
4.  If c0 ≠ 1, go back to point 2.     
      """)

c0=int(input("Enter any number: "))

while c0!=1:
    print(c0)
    if c0%2==0:
        c0//=2
    else:
        c0=3*c0+1
print("1")



    