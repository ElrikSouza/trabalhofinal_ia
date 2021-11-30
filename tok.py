import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Formata um csv para um formato utlizavel pelo keras

dir_name = input("nome do diretorio ")
flag = input("criar diretorio [y/n]? ")

if flag == "y":
    os.system(f"mkdir {dir_name}")
    os.system(f"mkdir {dir_name}/train")
    os.system(f"mkdir {dir_name}/train/0")
    os.system(f"mkdir {dir_name}/train/1")
    os.system(f"mkdir {dir_name}/test")
    os.system(f"mkdir {dir_name}/test/0")
    os.system(f"mkdir {dir_name}/test/1")

csv = input("nome do csv ")
texts = pd.read_csv(csv, sep=";")

x = [num for num in range(texts.shape[0])]
train_x, test_x, _, _ = train_test_split(
    x, texts["class"], random_state=67, stratify=texts["class"], test_size=0.2)

count = 0


def get_cmd(text, className, train_test, count):
    return f'echo "{text}" > {dir_name}/{train_test}/{className}/{className}-{count}.txt'


for _, row in texts.iterrows():
    className = row['class']
    text = row['text']

    if count in train_x:
        os.system(get_cmd(text, className, "train", count))
    else:
        os.system(get_cmd(text, className, "test", count))

    count += 1
