def caesar(direction, text, shift):
    if direction == "decode":
        shift = shift * -1
    result_chars = []
    for char in text:
        if not char.isalpha():
            result_chars.append(char)
            continue
        char_index = alphabet.index(char)
        new_index = (char_index + shift) % 26
        result_chars.append(alphabet[new_index])

    return  "".join(result_chars)


def run_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n").strip())
    print("The {}d text is: {}".format(direction, caesar(direction=direction, text=text, shift=shift)))


def main():   
    keep_running = True
    while keep_running:
        run_cipher()
        answer = input("Continue? ").lower().strip()
        if answer == "no" or answer == "n":
            print("Goodbye")
            keep_running = False


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

if __name__ == "__main__":
    main()
