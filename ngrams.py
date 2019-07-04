def unigram(doc):
    # create a list for the result
    result = list()
    # create a list that contains no punctuation
    sentence = list()
    # parse through the document to add all tokens that are words to the sentence list
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 1):
        first_word = sentence[word]
        if first_word.tag_ == "NN"   :
            element = [first_word.tag_]
            result.append(element)
            #pattern 10
        
        if first_word.tag_ == "VB"   :
            element = [first_word.tag_]
            result.append(element) 
            #pattern 11

    return result
def bigram(doc):
    # create a list for the result
    result = list()
    # create a list that contains no punctuation
    sentence = list()
    # parse through the document to add all tokens that are words to the sentence list
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 1):
        first_word = sentence[word]
        second_word = sentence[word + 1]
        if first_word.tag_ == "JJ" and (second_word.tag_ =="NN" or second_word.tag_ =="NNS")  :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 1

        if first_word.tag_ == "RB" and second_word.tag_ =="JJ"  :
            element = [first_word.tag_, second_word.tag_]
            result.append(element)
            #pattern 3 
        
        if first_word.tag_ == "RB" and (second_word.tag_ =="VBN" or second_word.tag_ =="VBD")  :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 5
        
        if (first_word.tag_ == "VBN" or first_word.tag_ =="VBD") and (second_word.tag_ =="NN" or second_word.tag_ =="NNS")  :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 7

        if (first_word.tag_ == "VBN" or first_word.tag_ =="VBD") and (second_word.tag_ =="RB" or second_word.tag_ =="RBR" or second_word.tag_ =="RBS")  :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 8        

        if (first_word.tag_ == "NN" or first_word.tag_ =="NNS") and second_word.tag_ =="JJ" :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 9

        if first_word.tag_ == "VB" and second_word.tag_ =="RP" :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 12
        
        if first_word.tag_ == "DT" and second_word.tag_ =="NN" :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 13
        
        if first_word.tag_ == "NN" and second_word.tag_ =="NN" :
            element = [first_word.tag_, second_word.tag_]
            result.append(element) 
            #pattern 14
        
    return result

def trigram(doc):
    # create a list for the result
    result = list()
    # create a list that contains no punctuation
    sentence = list()
    # parse through the document to add all tokens that are words to the sentence list
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 2):
        first_word = sentence[word]
        second_word = sentence[word + 1]
        third_word = sentence[word + 2]
        if first_word.tag_ == "JJ" and (second_word.tag_ =="NN" or second_word.tag_ =="NNS") and (third_word.tag_ =="NN" or third_word.tag_ =="NNS")  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 2

        if first_word.tag_ == "RB" and (second_word.tag_ =="JJ" or second_word.tag_ =="RBR") and (third_word.tag_ =="NN" or third_word.tag_ =="NNS")  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 4
        
        if first_word.tag_ == "RB" and (second_word.tag_ =="RB" or second_word.tag_ =="RBS") and third_word.tag_ =="JJ" :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 6
        
        if first_word.tag_ == "JJ" and second_word.tag_ =="VB" and third_word.tag_ =="NN"  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 15
        
        if first_word.tag_ == "JJ" and second_word.tag_ =="VB" and third_word.tag_ =="NN"  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 16
        
        if first_word.tag_ == "NN" and second_word.tag_ =="IN" and third_word.tag_ =="NN"  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 17
        
        if first_word.tag_ == "NN" and second_word.tag_ =="NN" and third_word.tag_ =="NN"  :
            element = [first_word.tag_, second_word.tag_,third_word.tag_]
            result.append(element) 
            #pattern 18

    return result

