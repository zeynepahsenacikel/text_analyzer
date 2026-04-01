import locale
import sys

locale.setlocale(locale.LC_ALL, "en_US")

from sys import argv
text=open(argv[1], "r")  #open and read input file
text=text.read()

def word_counter(text):  #count the number of word in text
    return len(text.split())

def sentence_counter(text):  #count the number of sentences
    a=0
    b=0
    c=0
    i=0
    while i<len(text):
        if i+2<len(text) and text[i]=="." and text[i+1]=="." and text[i+2]==".":
            a=a+1  #number of "..."
            i=i+3
        elif text[i]==".":
            b=b+1  #number of "."
            i=i+1
        elif text[i]=="!" or text[i]=="?":
            c=c+1  #number of "!" and "?"
            i=i+1
        else:
            i=i+1
    return a+b+c

def average(text):  #calculates the average number of words per sentences
    num_of_sentence = sentence_counter(text)
    num_of_word = word_counter(text)
    avg = num_of_word / num_of_sentence
    return avg

def num_of_characters(text):  #number of total characters
    return len(text)

def num_of_characters_v2(text):  #number of characters in words only(not spaces, new lines or punctuation
    p = 0
    y = text.count("\n")
    punctuation = "!#$%&()*+,./:;<=>?@[]\^_{|}~"

    for i in text:
        if i in punctuation:
            p = p + 1  #number of punctuation

    for word in text.split():  #get rid of the punctuation at the end of the word
        if word[-1] in punctuation:
            word = word[:-1]
    b=0
    for a in text.split():
        if a[-1]== "'":
            b=b+1

    def without_space(text):  #num of characters excluding spaces
        c = 0
        for z in text:
            if z != " ":
                c = c + 1
        return c

    s = without_space(text)
    return s - p - y - b

def length_calculator(text):  #find the shortest-longest words and their frequencies and sort them according to frequency and alphabetical order
    punctuation = "!#$%&'()*+,-./:;<=>?@[]\\^_`{|}~"
    word_list = []  #list for words without punctuations
    for w in text.split():
        if w[-3:] == "...":
            word = w[:-3]
        elif w[-1] in punctuation:
            word = w[:-1]
        else:
            word = w
        word_list.append(word.lower())

    shortests=[]  #list for shortest word/words
    longests=[]  #list for longest word/words
    sorted_list = sorted(word_list, key=len)
    short_len=len(sorted_list[0])
    long_len=len(sorted_list[-1])
    for a in sorted_list:
        if len(a) == short_len:
            shortests.append(a)
        elif len(a) == long_len:
            longests.append(a)
        else:
            continue
    u=len(word_list)
    s_freq=[(word, word_list.count(word)/u) for word in set(shortests)]
    l_freq=[(word, word_list.count(word)/u) for word in set(longests)]
    s_freq=sorted(s_freq, key=lambda x: (-x[1], x[0]))
    l_freq=sorted(l_freq, key=lambda x: (-x[1], x[0]))
    x = ""  #calculation for output design
    if len(s_freq) ==1:
       x +=f"{'The Shortest Word':<24}: {s_freq[0][0]:<24} ({s_freq[0][1]:.4f})"
       x += "\n"
    else:
       x += f"{'The Shortest Words':<24}:\n"
       for word, freq in s_freq:
           x += f"{word:<24} ({freq:.4f})\n"
    if len(l_freq) ==1:
       x += f"{'The Longest Word':<24}: {l_freq[0][0]:<24} ({l_freq[0][1]:.4f})\n"
    else:
       x += f"{'The Longest Words':<24}:\n"
       for word, freq in l_freq:
           x += f"{word:<24} ({freq:.4f})\n"
    return x

def word_frequencies(text):  #calculate frequencies for all words in text
    punctuation = "!#$%&'()*+,-./:;<=>?@[]\^_`{|}~"
    list1=[]
    for w in text.split():
        if len(w) >=3 and w[-3:]=="...":
            word=w[:-3]
        else:
            word=w.strip(punctuation)
        list1.append(word.lower())
    single_words=list(set(list1))  #calculate frequencies
    mylist=[]
    c=len(text.split())
    for a in single_words :
        b=list1.count(a)
        mylist.append((a,b))
    f=[(a,b/c) for a,b in mylist]
    list2=sorted(f, key=lambda x: (-x[1], x[0]))

    r=[]  #formatting output
    for a,freq in list2:
        r.append(f"{a:<24}: {freq:.4f}")
    return r

def main():  #function to call previous functions
    input = argv[1]  #input file name
    output = argv[2]  #output file name
    with open(input, "r") as text_file:
        text = text_file.read()

    with open(output, "w") as output:  #write  the output file with formatting version
        output.write(f"Statistics about {input:<7}:\n")
        output.write(f"{'#Words':<24}: {word_counter(text):<24}\n")
        output.write(f"{'#Sentences':<24}: {sentence_counter(text)}\n")
        output.write(f"{'#Words/#Sentences':<24}: {average(text):.2f}\n")
        output.write(f"{'#Characters':<24}: {num_of_characters(text)}\n")
        output.write(f"{'#Characters (Just Words)':<24}: {num_of_characters_v2(text)}\n")
        output.write(length_calculator(text))
        output.write("Words and Frequencies   :\n")
        w_freq = word_frequencies(text)
        output.write("\n".join(w_freq))

if __name__ == "__main__":  #execute the main function
    main()