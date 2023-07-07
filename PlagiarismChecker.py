from difflib import SequenceMatcher

with open("content.txt") as file1,open("sample.txt") as file2: 
    file1data=file1.read()
    file2data=file2.read()
    PlagiarizedPercent=SequenceMatcher(None,file1data,file2data).ratio()
    print("The Percentage of Plagiarism Done is : ")
    print(PlagiarizedPercent*100)