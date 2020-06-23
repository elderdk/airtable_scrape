import os
import glob
from bs4 import BeautifulSoup
import re
import string


def make_label_list(html):
    
    chars = re.escape(string.punctuation)
    label_list = []

    soup = BeautifulSoup(html, 'html.parser')
    labels = soup.select(".labelCellPair .labelContainer")
    for i in labels:
        raw_text = i.get_text()
        refined_text = re.sub(r'[' + chars + ']', '', raw_text)
        label_list.append(refined_text)
        
    return label_list

def make_data(html):

    # with open(test_file_path, 'r', encoding='UTF-8') as html:
    data = {}
    strings = []
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.select('div.labelCellPair > div.cellContainer > div > div')
    for i in divs:
        num_value = i.select_one('input[value]')
        if num_value:
            value = num_value.get_text()
        else:
            value = i.select_one('div > div').get_text()

        strings.append(value)

    a = 0
    labels = make_label_list(html)
    for label in labels:
        data[label] = strings[a]
        a += 1

    return data, labels