def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets oppend")

        data = fobj.read(5)
        print(data)

        fobj.seek(10,1)

        data = fobj.read(5)

        print(data)


    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()