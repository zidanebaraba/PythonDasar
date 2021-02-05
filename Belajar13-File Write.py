def main():
    #write to file
    out=open("test.txt","a")
    for i in range(3):
        inputToFile=input("enter string: ")
        out.write("{}\n".format(inputToFile))
    out.close()




if __name__ == "__main__":main()
