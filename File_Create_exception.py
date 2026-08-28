def main():
    try:
        open("Demo.txt","w")
        print("file gets oppend")

    except FileNotFoundError as fobj:
        print("file is not present in current directory")

if __name__ == "__main__":
    main()