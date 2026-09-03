import os

def main():
    ret = os.path.exists("Demo.txt")

    if(ret == True):
        print("file is present in cureent directory")
    else:
        print("there is no such file")
if __name__ == "__main__":
    main()