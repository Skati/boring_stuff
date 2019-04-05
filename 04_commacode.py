spam = ['apples', 'bananas', 'tofu', 'cats']
def convert(spam):
    a=','.join(spam[:len(spam)-1])+' and '+spam[-1]
    print(a)

convert(spam)
