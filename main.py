def text_file():
    with open("text.txt", "a") as file:
        while True:
            text = input("Type a text (or 'exit'): ")
            if text == 'exit':
                break
        
            file.write(text + "\n")
        



def read_file():
    with open("text.txt", "r") as file:
        print("Saved text: ")
        print(file.read())


text_file()
read_file()


