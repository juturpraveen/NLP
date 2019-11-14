from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from keras_preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model
from collections import Counter
from pandas import DataFrame
from matplotlib import pyplot
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

def build_model(n_words):
    # Network
    model = Sequential()
    model.add(Dense(50, input_shape=(n_words,), activation='relu'))
    model.add(Dense(1,activation='sigmoid'))
    
    #Compile network
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    plot_model(model, to_file='model.png', show_shapes=True)
    return model

def prepare_for_training(training_data, testing_data, scoringMode):
    tokenizer = build_tokenizer(training_data)
    tokenizer.fit_on_texts(training_data)
    xTrain = tokenizer.texts_to_matrix(training_data, scoringMode)
    xTest = tokenizer.texts_to_matrix(testing_data, scoringMode)
    return xTrain, xTest

def evaluate_model(Xtrain, Xtest, trainLabels, testLabels):
    scores = []
    n_repeats = 10
    n_words = Xtrain.shape[1]
    for i in range(n_repeats):
        model = build_model(n_words)
        model.fit(Xtrain, trainLabels, epochs=10,verbose=0)
        _, acc = model.evaluate(Xtest, testLabels, verbose=0)
        scores.append(acc)
        print('%d accuracy: %s' % ((i+1), acc))
    return scores

#Read the vocab
# vocab = read_vocab()
# trainDocs, trainLabels = get_ready_data(vocab, True)
# testDocs, testLabels = get_ready_data(vocab, False)
# modes = ['freq', 'binary', 'count', 'tfidf']
# results = DataFrame()
# for eachScoringMode in modes:
#     Xtrain, Xtest = prepare_for_training(trainDocs, testDocs, eachScoringMode)
#     results[eachScoringMode] = evaluate_model(Xtrain, Xtest, trainLabels, testLabels)
# print(results.describe())
# results.boxplot()
# pyplot.show()

#Prediction:
def predict_sentiment(review, vocab, tokenizer, model):
    tokens = preprocess_data(review)
    tokens = [w for w in tokens if w in vocab]
    line = ' '.join(tokens)
    encoded = tokenizer.texts_to_matrix([line], 'binary')
    print(encoded.shape)
    preds = model.predict(encoded, verbose=0)
    print('PREDS shape:', preds.shape)
    print('PREDS:', preds)
    percent_pos = preds[0, 0]
    if round(percent_pos) == 0:
        return (1-percent_pos), 'NEGATIVE' 
    return percent_pos, 'POSITIVE'

#Pre-processing data
vocab = read_vocab()
trainDocs, trainLabels = get_ready_data(vocab, True)
testDocs, testLabels = get_ready_data(vocab, False)

#Vectorization
tokenizer = build_tokenizer(trainDocs)
XtrainBinary = tokenizer.texts_to_matrix(trainDocs, 'binary')
XtestBinary = tokenizer.texts_to_matrix(testDocs, 'binary')

#Modelling
n_words = XtrainBinary.shape[1]
print(XtrainBinary.shape)
model = build_model(n_words)
model.fit(XtrainBinary, trainLabels, epochs=10, verbose=2)

#Positive test
reviewText01 = "This is a great movie."
percent, sentiment = predict_sentiment(reviewText01, vocab, tokenizer, model)
print('Review: [%s]\nSentiment: %s (%.3f%%)' % (reviewText01, sentiment, percent*100))

#Negative test
reviewText02 = "This movies is not good, boring."
percent, sentiment = predict_sentiment(reviewText02, vocab, tokenizer, model)
print('Review: [%s]\nSentiment: %s (%.3f%%)' % (reviewText02, sentiment, percent*100))
