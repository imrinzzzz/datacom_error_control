import datacomm as dc

# mylist = [7, 8, 1]
# hi = declist2bilist(mylist)
# print(list2string(hi, max([len(x) for x in hi])))

print("Hello, this is data communication assignment 1 by Thanirin (6088122)")
print("====================================================================")
print("First of all please choose which function you would like to use.")
print("     Enter 0 to use 'Unreliable Transmission'")
print("     Enter 1 to use 'Code generators'")
print("     Enter 2 to use 'Code checkers'")
x = input("Enter a number.. ")
if x == '0':
    binary = input("Please enter a string of only 0 and 1: ")
    percent = input("Please enter a percentage from 0 to 1; e.g. 20% means 0.2: ")
    percent = float(percent)
    if not (0 <= percent <= 1):
        print("Please enter valid percentage!")
    error = dc.unreliable_transmission(binary, percent)
    print("The output of ", binary, " with the percentage of ", percent, " error is ", error, ".")

elif x == '1':
    print("You chose 'Code generators! Next please choose which algorithms you want.'")
    print("     Enter 0 to use 'Parity Bit'")
    print("     Enter 1 to use 'CRC'")
    print("     Enter 2 to use 'Checksum'")
    print("     Enter 3 to use 'Hamming Code'")
    y = input("Enter a number.. ")
    if y == '2':
        word_block = int(input("Please enter how many words or numbers you want to input: "))
        list2 = list()
        for i in range(word_block):
            temp = input("Enter the word: ")
            list2.append(dc.ASCIItoBinary(temp))
        size = max([len(x) for x in list2])
        print("The output of checksum encoded string is ", dc.Checksum_gen(list2, size, word_block))

    elif y == '0' or y == '1' or y == '3':
        word = input("Please enter a word: ")
        ASCIIword = dc.ASCIItoBinary(word)

        if y == '0':
            print("Please enter the type of parity bit.")
            print("     Enter 0 for even parity bit")
            print("     Enter 1 for odd parity bit")
            print("     Enter 2 for even 2D parity bit")
            print("     Enter 3 for even parity bit")
            type0 = int(input("Enter a VALID number: "))
            size = ""
            if type0 == 2 or type0 == 3:
                size = str(int(len(ASCIIword) / len(word)))
                size += 'x'
                size += str(len(word))
            print("The output of parity bit encoded string is ", dc.parity_gen(ASCIIword, type0, size))

        elif y == '1':
            print("Please enter the CRC method you want.")
            print("    Enter 0 for CRC-4")
            print("    Enter 1 for CRC-8")
            print("    Enter 2 for reversed CRC-16")
            print("    Enter 3 for CRC-16")
            print("    Enter 4 for CRC-24")
            print("    Enter 5 for CRC-32")
            type1 = int(input("Enter a VALID number: "))
            print("The output of CRC encoded string is ", dc.CRC_gen(ASCIIword, type1))

        elif y == '3':
            print("The output of hamming code encoded string is ", dc.Hamming_gen(ASCIIword))

    else:
        print("Please input a valid number!")

elif x == '2':

    print("You chose 'Code Checker! Next please choose which algorithms you want.'")
    print("     Enter 0 to use 'Parity Bit'")
    print("     Enter 1 to use 'CRC'")
    print("     Enter 2 to use 'Checksum'")
    print("     Enter 3 to use 'Hamming Code'")
    z = input("Enter a number.. ")
    bistring = input("Please enter a string of 0 and 1 only: ")

    if z == '2':
        word_block = int(input("Please enter how many words or numbers you have input: ")) + 1
        size = int(len(bistring) / word_block)
        list2 = dc.string2list(bistring, size, word_block)
        print(dc.Checksum_check(list2, size, word_block))

    if z == '0':
        print("Please enter the type of parity bit.")
        print("     Enter 0 for even parity bit")
        print("     Enter 1 for odd parity bit")
        print("     Enter 2 for even 2D parity bit")
        print("     Enter 3 for even parity bit")
        type0 = int(input("Enter a VALID number: "))
        size = ""
        if type0 == 2 or type0 == 3:
            size = "8"
            size += 'x'
            size += str(int(len(bistring)/8))
        print(dc.parity_check(bistring, type0, size))

    elif z == '1':
        print("Please enter the CRC method you want.")
        print("    Enter 0 for CRC-4")
        print("    Enter 1 for CRC-8")
        print("    Enter 2 for reversed CRC-16")
        print("    Enter 3 for CRC-16")
        print("    Enter 4 for CRC-24")
        print("    Enter 5 for CRC-32")
        type1 = int(input("Enter a VALID number: "))
        print(dc.CRC_check(bistring, type1))

    elif z == '3':
        print(dc.Hamming_check(bistring))

    else:
        print("Please input a valid number!")

else:
    print("Please input a valid number!")
