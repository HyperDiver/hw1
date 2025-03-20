
import sys
path_i="C:\\Users\\Edwar\\Downloads\\oncogene.tsv"
di=dict()
with open(path_i,"r") as infile:
    for line in infile:
        c,l1,l2,n=line.strip().split('\t')
        di[n]=[c,l1,l2]
while 1:
    q=input("Enter gene name to query or 'exit' to quit: ")
    if q=="exit":
        break
    print(f"Gene {q} is at {di[q][0]}:{di[q][1]}-{di[q][2]}")

