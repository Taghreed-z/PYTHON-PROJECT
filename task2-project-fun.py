


def np_dup(sentence):
    not_duplicat=[]
    for word in sentence.split(' '):
        if word not in not_duplicat :
            not_duplicat.append(word)
    print(len(not_duplicat))



sentence=input('Enter your sentence :')
np_dup(sentence)
