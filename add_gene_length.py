import sys
path_i=sys.argv[1]
path_o=sys.argv[2]
with open(path_i,"r") as infile,open(path_o,"w") as outfile:
    for line in infile:
        c,l1,l2,n=line.strip().split('\t')
        len=int(l2)-int(l1)
        outfile.write(f"{c}\t{l1}\t{l2}\t{n}\t{len}\n")
    


