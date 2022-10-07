import os
from Inverted_Index import inverted_index_of
from Checker import Checker


"""If you want to change where the Inverted index is stored, change MainPath.
Documents must be stored in the Documents folder in said path"""

MainPath = "./"

"""We check if every file and folder we need is ready, and prepare them if they are not"""
Check = Checker(MainPath)
documents = Check.documents_checker()
Check.IE_File_checker()
Check.Indices_Folder_checker()



for doc in documents:
    if not os.path.isfile(MainPath+"indices/"+doc[0:-3]+"json"):
        print("Inverting and adding:        ",doc[0:-4])
        inverted_index_of(doc, MainPath,0)
    else:
        print("Already inverted, updating:  ",doc[0:-4])
        inverted_index_of(doc, MainPath, 1)


