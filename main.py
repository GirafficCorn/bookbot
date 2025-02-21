def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        

    def countWords(file_contents):
        count = 0
        words = file_contents.split()
        for i in words:
            count +=1 
        return count

    def countChars(file_contents):
        dict = {}
        for i in file_contents:
            letter = i.lower()
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        return(dict)


    def printReport():
        data = countChars(file_contents)
        count = countWords(file_contents)
        print("--- Report of Frankenstein Book Data ---")
        print(f"{count} words found in document")
        for k, v in data.items():
            if k.isalpha():
                print (f"The '{k}' character was found {v} times")


    printReport()

main()