def multiply_and_greet(*number,**student):
    num=1
    for y in number:
        num*=y
        print (num)
    print (f"Hello{student}")
    
