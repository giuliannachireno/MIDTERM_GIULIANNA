def count_pattern(text):
    """
    Finds all the occurrences of a certain pattern, that starts with “C” has unlimited number of letters and ends with “jeb”
    :param text: The text in which to search for the pattern.
    :return: An integer representing the number of matches.
    """
    words = text.split() #we use the spacing in order for the text to split and count individual words
    count = 0 #start count at 0
    for word in words: #use for loops to iterate the list
        if word.startswith("C") and word.endswith("jeb"): #using commands we learned in class see if word starts with C or ends with jeb
            count += 1 #if so + 1
    return count
word_bank = (
    "Cjeb Cabcjeb CXYZjeb Ctestjeb Csupercooljeb "  # These should match
    "cjab Cabj CHellojebs DJeb Chej Cj eb "          # These should NOT match
    "AnotherWord NotMatching "                      # Not matching
    "Cmatchjeb Cevenmorejeb Extra"                  # These two match, Extra does not
)

matches = count_pattern(word_bank)
print("Number of matches:", matches)

#used chatgpt to create a word bank to see if code worked! and it did!