```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class AutoSummarizer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stopWords = set(stopwords.words("english"))

    def generate_summary(self, text):
        words = word_tokenize(text)
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in self.stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]

        average = int(sumValues / len(sentenceValue))

        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        return summary
```