def reverse_even_words(sentence):
    words = sentence.split()

    if len(words) >= 4:
        words[1] = words[1][::-1]
        words[3] = words[3][::-1]

    reversed_sentence = " ".join(words)
    return reversed_sentence
    
original_sentence = "The sky is blue"

reversed_sentence = reverse_even_words(original_sentence)

print(reversed_sentence)
