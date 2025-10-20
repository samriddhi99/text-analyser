from text_analyser.analyser import word_count, char_count, most_common_words

def test_word_count():
    assert word_count("Hello world!") == 2

def test_char_count():
    assert char_count("abc") == 3

def test_common_words():
    text = "cat cat dog"
    assert most_common_words(text, 1)[0][0] == "cat"
