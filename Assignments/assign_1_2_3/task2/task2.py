from sets import Set

# read the parse file generated by standford parser
f = open('output_task2_PARSE.txt', 'r')
if(f!=None):
    str1=f.read().splitlines()
    arr=""
    for line in str1:
        arr+=line
    ar=arr.replace('','')
else:
    print "error opening the file"

# parse the file to populate trees
CFG_TREE=[]
DEP_TREE=[]
itr=0
while(ar.find("(. .)))")!=-1):
    itr+=1
    if(itr!=1):
        tmp=num1
    num1=ar.find("(ROOT  (")
    if(itr!=1):
        DEP_TREE.append(ar[(ar[:num1].find(". .)))")+6):num1])
    num2=ar.find("(. .)))")
    temp1=ar[num1:num2]
    CFG_TREE.append(temp1)
    ar=ar[num2+1:len(ar)]
DEP_TREE.append(ar[(ar[:num1].find(". .)))")+6):])

edges=[{},{}]
# make the Phase structure tree
def phase_graph(string,senNo):
    global edges
    curr=0
    mylst=['MYROOT']			
    spt=string.split('(')
    for line in spt:
    	if(line!=''):
            l=line.split(')')
            for s in l:
                if(s==''):
                    mylst.pop()
                    curr-=1
                elif(s.isspace()):
                    mylst.pop()
                    curr-=1
                else:
                    s=s.strip()
                    if(len(s.split())==1):
                        if mylst[curr]+"$"+s not in edges[senNo]:
                            edges[senNo][mylst[curr]+"$"+s]=1
                        else:
                            edges[senNo][mylst[curr]+"$"+s]+=1
                        mylst.append(s)
                        curr+=1
                    else:
                        if mylst[curr]+"$"+s.split()[0] not in edges[senNo]:
                            edges[senNo][mylst[curr]+"$"+s.split()[0]]=1
                        else:
                            edges[senNo][mylst[curr]+"$"+s.split()[0]]+=1
                        mylst.append(s.split()[0])
                        curr+=1


phase_graph(CFG_TREE[0],0)
phase_graph(CFG_TREE[1],1)
commonEdge=0
for common in Set(edges[0].keys()).intersection(Set(edges[1].keys())):
    if('MYROOT' in common):
        continue
    if(edges[0][common]>=edges[1][common]):
        commonEdge+=edges[1][common]
    else:
        commonEdge+=edges[0][common]
        
print "Number of common edges in phrase structure tree are :",commonEdge    
    
list1=[{},{}] 
# make the dependency tree   
def depgraph(string,senNo):
    for i  in string.split(')'):
        if(i!=''):
            relation=i.split('(')[0]
            if relation in list1[senNo]:
                list1[senNo][relation]+=1
            else:
                list1[senNo][relation]=1   
            first=i.split('(')[1].split(',')[0]
            second=i.split('(')[1].split(',')[1]


depgraph(DEP_TREE[0],0)
depgraph(DEP_TREE[1],1)
commonEdge=0
for common in Set(list1[0].keys()).intersection(Set(list1[1].keys())):
    if(list1[0][common]>=list1[1][common]):
        commonEdge+=list1[1][common]
    else:
        commonEdge+=list1[0][common]

print "Number of common edges in dependency tree are :",commonEdge        
            