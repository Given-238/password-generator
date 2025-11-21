import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if characters == "":
        raise ValueError("No character type selected!")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def ask_yes_no(question):
    answer = input(question + " (y/n): ").strip().lower()
    return answer == "y"


def main():
    print("=== PASSWORD GENERATOR ===")

    length = int(input("Password length: ").strip())

    use_upper = ask_yes_no("Include uppercase letters?")
    use_lower = ask_yes_no("Include lowercase letters?")
    use_digits = ask_yes_no("Include digits?")
    use_symbols = ask_yes_no("Include symbols?")

    try:
        result = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\nGenerated Password:")
        print(result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()