import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    print(f"paeameters: {len(args)}")
    for arg in args:
        print(F"{arg}: {len(len)}")

if __name__ == "__main__":
    main()
