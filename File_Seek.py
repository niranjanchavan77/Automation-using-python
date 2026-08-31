def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets oppend")

        fobj.seek(10,0)

        data = fobj.read()

        print(data)

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()