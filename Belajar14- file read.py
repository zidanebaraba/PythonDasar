def main():
    ReadFile=open("test.txt","r")
    for line in ReadFile:
        print(line)
    ReadFile.close()




if __name__ == "__main__":main()