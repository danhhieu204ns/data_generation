import fitz, nltk
import numpy as np
from pyvi.ViTokenizer import tokenize
import re
# nltk.download('punkt_tab')

def clean_string(s):
    cleaned = re.sub(r'\s+', ' ', s).strip()
    return cleaned

def read_pdf(file_path):
    '''
    read pdf file and return content

    input: path_to_pdf_file
    output: sequence string consist of document content
    '''
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def split_into_sentences(documents):
    '''
    split document content into sentences list

    input: document content
    output: return two numpy array (Vietnamese sequences, sequences split by nltk tool)
    '''
    # sentence_lists = []
    # sentences = nltk.sent_tokenize(documents)
    # for sent in sentences:
    #     if len(sent.split(" ")) > 4: 
    #         tokenizer_sent = tokenize(sent)
    #         sentence_lists.append(tokenizer_sent)
    #     else:
    #         sentences.remove(sent)
    # sentence_lists = np.array(sentence_lists)
    # return sentence_lists, sentences

    sentence_lists = []
    sentences = nltk.sent_tokenize(documents)
    for sent in sentences:
        # cleaned = clean_string(sent)
        # if len(cleaned.split(" ")) > 4: 
        #     sentence_lists.append(cleaned)
        if len(sent.split(" ")) > 4: 
            tokenizer_sent = tokenize(sent)
            sentence_lists.append(tokenizer_sent)
        else:
            sentences.remove(sent)
    sentence_lists = np.array(sentence_lists)
    return sentence_lists