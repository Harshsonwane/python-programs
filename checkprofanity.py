def read_text():
    quotes=open("E:\Udacity\projects.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()
