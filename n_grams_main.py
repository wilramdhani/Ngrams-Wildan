import spacy
from ngrams import bigram, trigram, unigram
def main():
    # load English model
    nlp = spacy.load('en_core_web_sm')

    # create a document
    doc = nlp("This is just a great movie! The story is fantastic and engaging. The cinematography is exceptional and really on par with what you would expect from Cameron. I saw the movie in 3D twice and very happy I did.  I originally thought it would be good but it got a hold of me like Avatar did. I tell everyone about it but I have this feeling it is going to have a cult following. I was not familiar with Alita prior to watching this movie but I think if they make more, I will be a long time fan.  I recommend it. There is something for everyone in this movie. CG, Action, Romance, Etc... Definitely sequel worthy.")

    result = bigram(doc)
    result2 = trigram(doc)
    result3 = unigram(doc)

    for element in result2:
        for token in element:
            print(token, end=' ')
        print()

    for element in result:
        for token in element:
            print(token, end=' ')
        print()  # new line

    for element in result3:
        for token in element:
            print(token, end=' ')
        print()  # new line

main()
