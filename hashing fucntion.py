
# turns password into binary and puts each charecter in a list
def binary_conversion(password):
    binary = []
    for x in password:  # itterates through each letter of the password
        binary.append(str(bin(ord(x))[2:].zfill(8)))  # converts the letter into asci and adds it to a list
    return (binary)

# extends the list to an appropriate length
# binary is a list with each item bieng charecters
def extending(binary):
    if len(binary) < 61:  # checks if the binary is less than 61 which is when so
        binary.append("1" * 8)
    while len(binary) < 61:  # 35 is what I have taken as my max charecter count I will change it later on
        binary.append("0" * 8)
    if len(binary) < 61:  # checks if the binary is less than 61 which is when so
        binary.append("1" * 8)
    return binary

# returns the size of the list in a list with each number in binary
# binary is a list with each item bieng charecters note not the extended function answer
def size(binary):
    result = []
    x = (str(len(binary) * 8))# gets the length / size of the password
    while len(x) != 0: # iterates till all charecter / number is covered
        result.append(str(bin(ord(x[0]))[2:].zfill(8))) # converts into binary and adds it to the result
        x = x[1:]
    while len(result) < 3: # loops till answer is at least 3 items
        result.append("0" * 8) # adds filler data
    return result


# binary is a single string in bianry
def rightrotation(binary, num):
    return binary[-num:] + binary[:-num]

# binary is a single string in bianry
def rightshift(binary, num):
    return "0" * num + binary[:-num]


# binary is a list with three items
def addition_mod_2(binary):
    ans = ""
    for x in range(0, len(binary[0])):  # iterates through the binary string
        modulo = 0  # the answer for this charetcer in binary
        for y in range(0, len(binary)):
            modulo += int(binary[y][x])  # adding up each binary charecter
        ans += str(modulo % 2)  # adding the answer to the main
    return (ans)

# Ch in the video
# binary is a list with 3 items
def choose(binary):
    ans = ""
    for x in range(0, len(binary[0])):  # iterates through item 1 of binary list
        # print(binary[0][x])
        if binary[0][x] == "0":
            ans += binary[2][x]  # adds from third item if charecter is 0
        else:
            ans += binary[1][x]  # adds from second item if charecter is 0
    return (ans)


# Maj in the video
# binary is a list with 3 items
# copied the code from the previously written addition mod2 function
# hence variables may not accurately reflect all parts of the code in this function
def majority(binary):
    ans = ""
    for x in range(0, len(binary[0])):  # iterates though one of the items
        modulo = ""
        for y in range(0, len(binary)):  # adds up all the
            modulo += (binary[y][x])  # adds the items in all the lists of the current index into a string
        if modulo.count("1") >= 2:  # checks which charecter is the most common in the string
            ans += "1"  # adds 1 if 1
        else:
            ans += "0"  # adds 0 if 0
    return (ans)

# binary is a string
def lower_sigma0(binary):
    return addition_mod_2([rightrotation(binary, 7), rightrotation(binary, 18), rightshift(binary, 3)])


# binary is a string
def lower_sigma1(binary):
    return addition_mod_2([rightrotation(binary, 17), rightrotation(binary, 19), rightshift(binary, 10)])


# binary is a string
def upper_sigma0(binary):
    return addition_mod_2([rightrotation(binary, 2), rightrotation(binary, 13), rightrotation(binary, 22)])


# binary is a string
def upper_sigma1(binary):
    return addition_mod_2([rightrotation(binary, 6), rightrotation(binary, 11), rightrotation(binary, 25)])


# binary is a list with 64 items each 8 bits long
def split32(binary):
    ans = []
    for x in range(0, 64, 4):  # iterates through the list skipping 4 at a time
        item = ""
        for y in range(0, 4):  # iterates through the numbers 0 to 3
            item += binary[x:x + 4][y]  # combines the strings placing it one after another
        ans.append(item)  # adds the longer answer
    return (ans)


# binary is a list with 8 items which are 16 bits each
def Wlist(binary):
    for x in range(17, 64 + 1):  # creates the rest of the message scheduling lists
        binary.append(
            addition([lower_sigma1(binary[x - 2]), binary[x - 5], lower_sigma0(binary[x - 7]), binary[x - 9]]))
    return (binary)


# this function adds up the binary numbers
# binary is a list with multiple items of binary
def addition(binary):
    total = 0
    for x in range(0, len(binary)):  # iterates through all sublists in the binary list
        total += (int(binary[x], 2))  # adds up the numbers by converting it into integers
    ans = str(bin(total % (2 ** 32)))[2:].zfill(32)  # converts the numbers back to binary
    return (ans)


# w is a list with 32 items
def alphabets(w):  # main hashing answer
    k = [  # constants derived from square rooting prime numbers - stops backdoors
        "01000010100010100010111110011000",
        "01110001001101110100010010010001",
        "10110101110000001111101111001111",
        "11101001101101011101101110100101",
        "00111001010101101100001001011011",
        "01011001111100010001000111110001",
        "10010010001111111000001010100100",
        "10101011000111000101111011010101",
        "11011000000001111010101010011000",
        "00010010100000110101101100000001",
        "00100100001100011000010110111110",
        "01010101000011000111110111000011",
        "01110010101111100101110101110100",
        "10000000110111101011000111111110",
        "10011011110111000000011010100111",
        "11000001100110111111000101110100",
        "11100100100110110110100111000001",
        "11101111101111100100011110000110",
        "00001111110000011001110111000110",
        "00100100000011001010000111001100",
        "00101101111010010010110001101111",
        "01001010011101001000010010101010",
        "01011100101100001010100111011100",
        "01110110111110011000100011011010",
        "10011000001111100101000101010010",
        "10101000001100011100011001101101",
        "10110000000000110010011111001000",
        "10111111010110010111111111000111",
        "11000110111000000000101111110011",
        "11010101101001111001000101000111",
        "00000110110010100110001101010001",
        "00010100001010010010100101100111",
        "10001100110001110000001000001000",
        "10010000101111101111111111111010",
        "10100100010100000110110011101011",
        "10111110111110011010001111110111",
        "11000110011100010111100011110010",
        "11001010001001110011111011001110",
        "11010001100001101011100011000111",
        "11101010110110100111110111010110",
        "11110101011111010100111101111111",
        "00000110111100000110011110101010",
        "00001010011000110111110111000101",
        "00010001001111111001100000000100",
        "00011011011100010000101100110101",
        "00101000110110110111011111110101",
        "00110010110010101010101101111011",
        "00111100100111101011111000001010",
        "01000011000111010110011111000100",
        "01001100110001011101010010111110",
        "01011001011111110010100110011100",
        "01011111110010110110111110101011",
        "01101100010001000001100110001100",
        "01110100100011111000001011101110",
        "01111000101001010110001101101111",
        "10000100110010000111100000010100",
        "10001111000110111111110011011110",
        "10011100011001101110010010101001",
        "10100010101111111110100010100001",
        "10101000000110100110011001001011",
        "11000011110100101110000101000010",
        "11000110101100111101101110100101",
        "11010101010111100011111110001001",
        "11101010110110100111110111010110"
    ]

    h = [  # constants derived from cube rooting prime numbers - stops backdoors
        "01101010000010011110011001100111",
        "10111011011001111010111010000101",
        "00111100011011101111001101110010",
        "10100101010011111111010100111010",
        "01010001000011100101001001111111",
        "10011011000001010110100010001100",
        "00011111100000111101100110101011",
        "01011011111000001100110100011001"
    ]

    for t in range(0, 64):  # iterates through the entire list which I know is going to have a total of 64 elements
        t1 = addition([h[7], upper_sigma1(h[4]), choose([h[4], h[5], h[6]]), k[t],
                       w[t]])  # creates a variable from the previous items + iteration number
        t2 = addition([upper_sigma0(h[0]),
                       majority([h[0], h[1], h[2]])])  # creates a variable from the previous items + iteration number
        h = rotate(h, t1, t2)
    return (h)


# h is a list with 8 items each item is a string of 32 bits
def rotate(h, t1, t2):
    hnew = []

    # appends original list in a different order than normal
    hnew.append(addition([t1, t2]))
    hnew.append(h[0])
    hnew.append(h[1])
    hnew.append(h[2])
    hnew.append(addition([h[3], t1]))
    hnew.append(h[4])
    hnew.append(h[5])
    hnew.append(h[6])

    return hnew


# processing
def process(password):
    binary_list = (binary_conversion(password))  # gets the binary version of password
    extended_list = extending(binary_list)  # extends the binary list tot he appropriate length
    for x in size(binary_conversion(password)):  # gets the size of binary function
        extended_list.append(x)  # adds it to the extended list

    extended_list = (split32(extended_list))  # formats the extended list in the right way
    w32list = Wlist(extended_list)  # does the message scheduling for final hash

    ans = ""
    for x in alphabets(w32list):  # final hash
        ans += x  # adds them up to get it in the correct format instead of a list
    return ans

print(process("hello"))
