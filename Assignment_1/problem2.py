def caesar(text, k):
    result = ""
    for letter in text:
        ascii_num = ord(letter)
        # Ensure all special characters are kept in the result
        if (ascii_num < 65 or ascii_num > 122 ) or (ascii_num > 90 and ascii_num < 97):
            result = result + letter
            continue
        
        # Condition to keep capitalization of original letter
        if (ascii_num < 97 and (ascii_num + k > 90)):
                next = ascii_num + k - 26 # if above Z, return to A
        elif (ascii_num >=97 and (ascii_num + k > 122)):
                next = ascii_num + k - 26 # if above z, return to a
        else:
            next = ascii_num + k

        result = result + chr(next)
    
    return result

def main():
    print("Enter your birth year:")
    k = input()
    k = int(k[len(k)-1])

    with open("plain.txt", "r") as file:
        text = file.read()

    with open("cipher.txt", "w") as cipher:
        cipher.write(caesar(text, k))

if __name__ == "__main__":
    main()