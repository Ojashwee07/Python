def count_words(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        if word != "":
            count += 1
        else:
            # This else block is just for demonstration; it won't be triggered here
            pass
    return count
sentence = "i am a good boy"
word_count = count_words(sentence)
print(f"The sentence contains {word_count} words.")
