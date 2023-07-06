from difflib import SequenceMatcher                   #difflib is a library
with open("one.txt") as file1, open("two.txt") as file2:
    fileonedata = file1.read()
    filetwodata = file2.read()
    similarity=SequenceMatcher(none,fileonedata,filetwodata).ratio()
    print(similarity*100)

   #COSINE ALGORITHMS
                           