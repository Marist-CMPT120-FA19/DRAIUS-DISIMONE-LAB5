##Lab 5 Draius Disimone

def main():  
    sentence = str(input("Please enter a sentence: "))
    wordcount = len(s.split(" "))
    avg = 0
    
    for x in sentence:
        avg = avg + len(x)
    avg = (avg - sentence.count(" "))/wordcount
    print("# of characters:", len(sentence))
    
    print("# of words:",  wordcount)
    
    print("# of letters:", avg)
main()
