def main():
    try:
        fobj = open("Demo.txt","r")
        print("file gets oppend")

        print("file offset is : ",fobj.tell())      # 0

        data = fobj.read(10)
        print(data)

        print("file offset is : ",fobj.tell())      # 10

        data = fobj.read(10)
        print(data)

        print("file offset is : ",fobj.tell())      # 20

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()