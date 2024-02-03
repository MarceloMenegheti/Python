# How to print triangle pattern in python as show below:
# -----* 
# ----* * 
# ---* * * 
# --* * * * 
# -* * * * * 

for i in range(5):    
    print(" "*(5-i),end="")
    for i in range(i+1):
        print("* ", end="")
    print("")
    
