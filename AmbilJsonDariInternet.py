import urllib.request,json


def main():
    url="blob:https://extendsclass.com/ed8d3a5c-93cd-4d93-b06a-36362b49469f"
    data=urllib.request.urlopen(url).read()
    print(data)
    
if __name__ == "__main__":
    main()