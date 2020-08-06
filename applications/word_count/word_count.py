import re
cache = {}

def word_count(s):
    # Replace invalid chars   
    name= s.replace('"','').replace(':','').replace(';','').replace(',','').replace('.','').replace('-','').replace('+','').replace('=','').replace('/','').replace("|",'').replace('[','').replace(']','').replace('{','').replace('}','').replace('(','').replace(')','').replace('*','').replace('^','').replace('&','').replace('\\','')
    split = name.lower().split()
    words_number = {i:split.count(i) for i in split}
    print(words_number)
    return words_number



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))