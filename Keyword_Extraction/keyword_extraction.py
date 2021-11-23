# Write a program to find keywords for Vietnamese documents using LSA

    
import sys
import os.path
import re
from gensim import corpora
from gensim.models import LsiModel
from underthesea import word_tokenize
from nltk.stem.porter import PorterStemmer


inFile = sys.argv[2]
outFile = sys.argv[4]

def load_data():
    documents_list = []
    titles=[]
    # read file
    with open(inFile,'r') as fin:
        for line in fin.readlines():
            text = line.strip()
            documents_list.append(text)
    
    # get number of topics
    number_of_topics = len(documents_list)
    return documents_list,number_of_topics


def preprocess_data(doc_set):
    # create VietNam stop words list
    with open('vietnamStopWords','r') as vn:
        vi_stop_words = vn.read().splitlines()
    # list for tokenized documents in loop
    texts = []
    # loop through document list
    for i in doc_set:
        # lowercase
        raw = i.lower()
        # remove punctuation from each token
        res = re.sub(r'[^\w\s]', '', raw)
        # clean and tokenize document string
        tokens = word_tokenize(res)
        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in vi_stop_words]
        # add tokens to list
        texts.append(stopped_tokens)
    return texts

def prepare_corpus(doc_clean):
    # Creating the term dictionary of our courpus, where every unique term is assigned an index. dictionary = corpora.Dictionary(doc_clean)
    dictionary = corpora.Dictionary(doc_clean)
    # Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
    # generate LSA model
    return dictionary,doc_term_matrix


def create_gensim_lsa_model(doc_clean,number_of_topics,words):
    dictionary,doc_term_matrix=prepare_corpus(doc_clean)
    # generate LSA model
    lsamodel = LsiModel(doc_term_matrix, num_topics=number_of_topics, id2word = dictionary)  # train model
    # print the top words for each topic
    with open(outFile,'w') as o:
        for i in range(number_of_topics):
            # Delete number because it is not a keyword and i don't want to print it - It is the percentage of occurrence
            delete_number = re.sub('[0-9\n]', '', str(lsamodel.show_topic(i,words)))
            # Delete regex punctuation because it is not a keyword
            delete_punc = re.sub(r'[^\w\s]', '', delete_number)
            # Result 
            result = str('Topic ') + str(i+1) +  ': ' + delete_punc
            o.write(str(result))
            o.write('\n')

def keyword_extraction():
    document_list,number_of_topics=load_data()
    clean_text=preprocess_data(document_list)
    create_gensim_lsa_model(clean_text,number_of_topics,7)

keyword_extraction();



