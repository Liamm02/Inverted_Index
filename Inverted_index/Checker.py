import os

class Checker:

    def __init__(self, path="./"):
        self.path = path


    def documents_checker(self):
        """This functions checks if there are documents to invert index, and returns their names."""
        documents = []

        # Iterate directory
        for path in os.listdir(self.path + "Documents/"):
            # check if current path is a file
            if os.path.isfile(os.path.join(self.path + "Documents/", path)):
                documents.append(path)
        if len(documents) == 0:
            print("There are no Documents to index, please add them to the Documents folder")
            return 0
        return documents

    def IE_File_checker(self):
        """This functions checks if there is an IE.json file so store our final inverted index"""
        if not os.path.isfile(self.path+"IE.json"):
            f = open(self.path+"IE.json", "w+", encoding="utf-8-sig")
            f.close()

    def Indices_Folder_checker(self):
        """This function checks if there is a folder to store the indices of all the documents"""
        path = self.path + "indices/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
