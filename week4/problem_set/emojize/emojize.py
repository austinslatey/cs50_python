from emoji import emojize

ALIASES_TO_EMOJI = {
    ":earth_asia:": "🌏",
    ":thumbsup:": "👍",
    ":candy: or :ice_cream:?": "🍬 or 🍨"
}

def emojize_text(text):
    emojized_text = emojize(text)
    return emojized_text, text

def main():
    user_input = input("Input: ")

    words = user_input.split()
    emojized = False
    output_text = ""

    for word in words:
        if word in ALIASES_TO_EMOJI:
            output_text += ALIASES_TO_EMOJI[word] + " "
            emojized = True
        else:
            output_text += word + " "

    if emojized:
        print("Output:", output_text.strip())
    else:
        emojized_text, original_text = emojize_text(user_input)
        if emojized_text != original_text:
            print("Output:", emojized_text)
        else:
            print("Input is not a recognized emoji alias")

if __name__ == "__main__":
    main()
