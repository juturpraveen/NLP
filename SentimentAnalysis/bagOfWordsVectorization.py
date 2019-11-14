from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from keras_preprocessing.text import Tokenizer
from collections import Counter
import re, string

filePathNeg = "/Users/praveenjutur/ml/100/day10/nlp/txt_sentoken/neg"
filePathPos = "/Users/praveenjutur/ml/100/day10/nlp/txt_sentoken/pos"

def load_file(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


def preprocess_data(text):
    #Split the file at spaces
    text = text.split( )      

    #Remove punctuation
    re_punc = re.compile('[%s]' % re.escape(string.punctuation)) 
    tokens = [re_punc.sub('', w) for w in text]

    #Remove tokens that are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]

    #Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    #Filter out short tokens
    tokens = [word for word in tokens if len(word) > 2]
    return tokens    

def file_to_list(filename, vocab):
    text = load_file(filename)
    cleanData = preprocess_data(text)
    vocabData = [token for token in cleanData if token in vocab]
    return ' '.join(vocabData)

def process_directory_files(directory,vocab,is_train):
    lists = []
    for file in listdir(directory):
        if is_train and file.startswith("cv9"):
            continue
        if not is_train and not file.startswith("cv9"):
            continue
        path = directory + '/' + file
        oneList = file_to_list(path, vocab)
        lists.append(oneList)
    return lists

def get_ready_data(vocab, is_train):
    negative = process_directory_files(filePathNeg, vocab, is_train)
    positive = process_directory_files(filePathPos, vocab, is_train)
    docs = negative + positive
    labels = [0 for _ in range(len(negative))] + [1 for _ in range(len(positive))]
    return docs, labels

def read_vocab():
    file = open('vocab.txt', 'r')
    text = file.read()
    file.close()
    text = text.split( )
    return text

def build_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer

def saveFile(tokens,filename):
    # text = '\n'.join(tokens)
    file = open(filename,'w')
    file.write(tokens)
    file.close()


#Read the vocab
vocab = read_vocab()
# vocab = set(vocab)
trainDocs, trainLabels = get_ready_data(vocab, True)
testDocs, testLabels = get_ready_data(vocab, False)
tokenizer = build_tokenizer(trainDocs)
Xtrain = tokenizer.texts_to_matrix(trainDocs,'freq')
Xtest = tokenizer.texts_to_matrix(testDocs,'freq')
print(Xtrain.shape, Xtest.shape)
n_words = Xtrain.shape[1]

# def build_model(n_words):
    
