import json,argparse
import pandas as pd
import networkx as nx


def most_by_num(G):
    result=list()
    edges=list(G.degree())
    while len(result)<3:
        m=max(edges,key=lambda tup: tup[1])
        edges.remove(m)
        result.append(m[0])
    return result

def most_by_weight(G):
    result=list()
    weight=list()
    for pony in G.nodes:
        w=0
        for e in G.edges(pony,data=True):
            w+=e[2]['weight']
        weight.append((pony,w))

    while len(result)<3:
        m=max(weight,key=lambda tup: tup[1])
        weight.remove(m)
        result.append(m[0])

    return result

def most_central_between(G):
    a= (nx.betweenness_centrality(G))
    result=list()
    while len(result)<3:
        m=max(a,key=a.get)
        result.append(m)
        a.pop(m)
    return result

    print(result)
def load_graph(file):
    G=nx.Graph()
    with open(file,'r') as count:
        dict=json.load(count)

    for pony in dict:
        for inte in dict[pony]:
            if G.has_edge(pony, inte):
                continue
            else:
                G.add_edge(pony,inte,weight=dict[pony][inte])
    return G

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",help='input',action='store',dest='input',type=str)
    parser.add_argument("-o",help='output',action='store',dest='output',type=str)
    args=parser.parse_args()
    a=dict()
    G=load_graph(args.input)
    a['most_connected_by_num']=most_by_num(G)
    a['most_connected_by_weight']=most_by_weight(G)
    a['most_central_by_betweenness']=most_central_between(G)

    with open(args.output,'w+') as f:
        json.dump(a,f, indent=4)



if __name__ == '__main__':
    main()
