# This is a Pig-Latin Translator. In Pig-Latin, any consonants in the beginning
# of a word places in the end of the word, and it ends each word with -ay.
# If the word starts with a vowel, the word ends with -yay. Like this:
# pig -> igpay
# glove -> oveglay
# apple -> appleyay


while True:

    #get sentence from user
    original = input("Type your sentence here: ").lower().strip()

    #split sentence into words (the .split module splits sentences into individual
    # words by default, and creates a list of strings.)
    words = original.split()

    # loop through words and convert to pig latin
    new_words = []

    for word in words:
        if word[0] in "aeiou":
            new_word = word + "yay"
            new_words.append(new_word)
        else:
            vowel_position = 0
            for letter in word:
                if letter not in "aeiou":
                    vowel_position = vowel_position + 1
                else:
                    break
            consonants = word[:vowel_position]
            the_rest = word[vowel_position:]
            new_word = the_rest + consonants + "ay"
            new_words.append(new_word)

    # stick words back together
    output = " ".join(new_words)

    # output final string
    print(output)
    print(" ")


# footnotes:
# break = breaks the loop and puts us at the beginning of the former expression?
# continue = skips the rest of the loop and goes back to the top of the loop to
# start the loop over again

