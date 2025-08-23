EMOJI = {
    "sad": "😢",
    "happy": "😊",
    "angry": "😠",
}

user_sentence = input("Please type your message and press Enter: ")

final_message = user_sentence

lower_sentence = user_sentence.lower()
words = lower_sentence.split()

for word in words:
    clean_word = word.strip(",.!?")
    if clean_word in EMOJI:
        emoji = EMOJI[clean_word]
        final_message = f"{emoji} {user_sentence}"
        break

print(final_message)