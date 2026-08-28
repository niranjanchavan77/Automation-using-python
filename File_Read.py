def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets oppend")

        data = fobj.read(10)
        print(data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()