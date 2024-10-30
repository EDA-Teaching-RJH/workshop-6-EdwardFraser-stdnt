#Your code goes here. 

import math
def safe_divide(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by 0")
        

def process_list(input_list):
    input_listsqr =[]
    for i in range(len(input_list)):
        try:    
            input_list[i] = int(input_list[i])
            input_listsqr.append(input_list[i]**2)
        except ValueError: 
            continue
        except NameError:
            continue
        except TypeError:
            continue
    print(sum(input_listsqr))


def nested_operations(a, b):
    try:
        a = int(a)
        b = int(b)
        c=a/b
        print(math.sqrt(c))
    except NameError:
        print("Both values must be integers")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except ValueError:
        try:
            a = int(a)
            b = int(b)
            print(math.sqrt(a/b))
        except TypeError:
            print("Must use two integers")
        except ValueError:
            print("Must use two non-negative integers and cannot divide by 0")

def process_input():
    a = input("Enter your value:")
    try:
        a = float(a)
        a = a**2
        print(a)
    except ValueError:
        print("must use valid number")
    else:
        return a
    finally:
        print("\n Process Complete")

process_list(['test',1,2,3,'seven',4,5,'6'])