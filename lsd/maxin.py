def  readgraph(file):
    graph={}
    with open(file,'r') as f:
        graph=dict(eval(f.read()))
    return graph
def maxin(graph,vgraph,hgraph):
    len1=len(graph)
    len2=len(vgraph)
    len3=len(hgraph)
    keylist1=[]
    result=[]
    for key,value in graph.items():
        keylist1.append(key)
    keylist2=[]
    for key,val in vgraph.items():
        keylist2.append(key)
    keylist3=[]
    for key ,val in hgraph.items():
        keylist3.append(key)
    flag=1
    print('keylist1',keylist1,'keylist2',keylist2,'keylist3',keylist3,sep='\n')

    for i in range(0,len1):
        h_i = 0
        v_i = 0
        if graph[keylist1[i]] is not None:
            h_i += 1
            v_i += 1
            hkey = str(graph[keylist1[i]][0])
            vkey = str(graph[keylist1[i]][1])
        while flag:

            if graph.get(hkey) :
                h_i += 1
                hkey = str(graph.get(hkey)[0])
            if graph.get(vkey) :
                v_i += 1
                vkey = str(graph.get(vkey)[1])
            if  graph.get(hkey) is None and  graph.get(vkey) is None:
                flag=0
        result.append([list(eval(keylist1[i])),h_i*v_i])
    print('result:',result)


if __name__ == '__main__':
    graph=readgraph('graph.txt')
    vgraph=readgraph('vgraph.txt')
    hgraph=readgraph('hgraph.txt')
    maxin(graph,vgraph,hgraph)