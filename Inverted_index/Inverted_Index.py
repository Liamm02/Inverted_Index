import json
from Document_normalizer import Translator,StopWords_deleter

def inverted_index_of(doc, MainPath, indexed=0):
    """The indexed parameter is used to tell the function that the midpoint of the document was already created"""
    path = MainPath + "/indices/"
    Document_path = MainPath + "/Documents/" + doc
    if indexed == 0:

        file = open(Document_path, encoding="UTF-8")
        f = file.read()
        file.seek(0)

        f = Translator(f)

        text = f.split("\n")

        Dictiorary = StopWords_deleter(text)


        """We save the midpoint file of the document in the indices folder"""
        with open(path + doc[0:-4] + '.json', 'w', encoding="UTF-8") as fp:
            json.dump(Dictiorary, fp, ensure_ascii=False)
    else:
        with open(path + doc[0:-4] + '.json', 'r', encoding="UTF-8") as di:
            content = di.read()
            Dictiorary = json.loads(content)


    """Now we edit the main Inverted Index"""
    with open(MainPath+"/IE.json", "r", encoding="UTF-8") as ie:
        content = ie.read()
        try:
            """Here we try to load the json file into jn. If the IE file is empty it will raise an error"""
            jn = json.loads(content)
            with open(MainPath+"/IE.json", "w", encoding="UTF-8") as ie2:
                """Since it didn't raise an error it means that the file already has words stored in it,
                so we check for those that are already stored to add the document information.
                We also do this for those words who are not stored in the IE.json file."""
                for k, v in zip(Dictiorary, Dictiorary.values()):
                    if k in jn:
                        jn[k].update({doc: v})
                    else:
                        jn.update({k: {doc: v}})
                json.dump(jn, ie2, ensure_ascii=False)
        except json.decoder.JSONDecodeError:
            """If the json file is empty it will just write in it without checking for existing words"""
            with open(MainPath+"/IE.json", "w", encoding="UTF-8") as ie2:
                t = {}
                for k, v in zip(Dictiorary, Dictiorary.values()):
                    t[k] = {doc: v}
                json.dump(t, ie2, ensure_ascii=False)

