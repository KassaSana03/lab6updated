encoded_passwords= {}

#Kassahun Sanayew Encoder
def Encoder(password):
    # string to store encoded password
    encoded_pass = ""

    # encoding of each digit
    for char in password:
        encoded_pass = encoded_pass + str((int(char) + 3) % 10)  # shifting 3 digit

    # return encoded password
    return encoded_pass


def Decoder(password):


while True:

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = input("Please enter an option: ")

    if option == "1":
        password = input("Please enter your password to encode: ")
        encoded_pass = Encoder(password)
        encoded_passwords[encoded_pass]=password
        print("Your password has been encoded and stored")

    elif option =='2':



    elif option == '3':
        print("Goodbye!")
        break