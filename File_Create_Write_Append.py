def main():
    try:
        fobj = open("Demo.txt","a")
        print("file gets oppend")

        fobj.write(" Pune Maharashtra")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()