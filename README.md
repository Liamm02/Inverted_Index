# Inverted_Index
Implement an inverted index by passing a collection of documents as parameters.
## Overview 📋
The code performs the following functions:

1- Check if every file and folder we need is ready, and prepare them if they are not.

2- Preprocesses the data in the text collection (stop words removal, stemming, removing punctuations etc.)

3- Create midpoints.

4- Create json file with the results.

## Running the code 🔧
*Python 3, nltk and json are required to run the code*

Ensure all the files from the repo are present in the same directory.

Open the project in any preferred IDE of your choice and run the Inverted_Index.py file, passing as argument several documents, files are recommended to be stored in the Documents folder.

## Detailed List of Functionalities Implemented ⚙️
### In the file Inverted_Index.py
#### 1. Inverted_index_of
This function creates the midpoints and also the Json file with the indexes.
### In the file Document_Normalizer.py
#### 1. Translator
This function gets rid of all the punctuations and special characters,
    it also converts the document to lowercase.
#### 2. StopWords_Deleter
This function removes stopwords from the text file.
### In the file Checker.py
#### 1. Documents_Checker
This functions checks if there are documents to invert index, and returns their names.
#### 2. IE_File_Checker
This functions checks if there is an IE.json file to store our final inverted index.
#### 3. Indices_Folder_Checker
This function checks if there is a folder to store the indices of all the documents.

## Built With 🛠️

* [PyCharm](https://www.jetbrains.com/es-es/pycharm/) - The text editor used.
* [Python 3.9.0](https://www.python.org/downloads/release/python-390/) - The python version used.
## Authors ✒️
* **Javier García**
* **Jesús Matos**
* **Liam Mahmud**
* **Krish Sadhwani**
