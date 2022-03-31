
LOOKUP_WORDS = {
    "terprocesszor": "space-processor",
    "ter processzor": "space-processor",
    "ter-processzor": "space-processor",
    "kristalyprocesszor": "crystal-processor",
    "kristaly-processzor": "crystal-processor",
    "kristaly processzor": "crystal-processor",
    "terkurt": "space-horn",
    "ter-kurt": "space-horn",
    "ter kurt": "space-horn",
    "robotkar": "robot-arm",
}


def translate_buzzwords(txt):

    filteredwords = str(txt)
    for word, repl_word in LOOKUP_WORDS.items():
        filteredwords = filteredwords.replace(word, repl_word)

    return filteredwords
