from text_analyser.sentiment import sentiment_score

def test_sentiment_positive():
    assert sentiment_score("I love this") > 0

def test_sentiment_negative():
    assert sentiment_score("I hate this") < 0
