import sys

def main():
    if len(sys.argv)!= 2:
        print("none")
        return
    
    param = sys.argv[1]
    user_input = input("What was the parameters? ")

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ =="__main__":
    main()