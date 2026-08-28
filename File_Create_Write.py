def main():
    try:
        fobj = open("Demo.txt","w")
        print("file gets oppend")

        fobj.write("Jay Ganesh...")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()