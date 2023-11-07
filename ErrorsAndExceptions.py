# while True:
#     try:
#         x=int(input("Please enter a number"))
#         break
#     except (ValueError, NameError):
#         pass
#         print("Oops! That was not a valid number. Try again...")
        
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
        
