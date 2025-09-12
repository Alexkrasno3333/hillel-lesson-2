import string

text = "Should, I. subscribe? Yes! "
hashtag = ""

for i in text:
    if i not in string.punctuation:
        hashtag += i
hashtag = hashtag.title()
hashtag = hashtag.replace(" ","")
hashtag = hashtag[:140]
hashtag = "#" + hashtag
print(hashtag)



























