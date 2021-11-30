import pandas as pd
import networkx as nx
import argparse,json


topchar=list()
def check_valid_name(s):
    if any(x in ['others','all','ponies','and','all'] for x in s.lower().split()):
        return False
    return True

def create_graph(file):
    """todo:
    * create pandas df for script and drop columns
    * add a column where the value is the name of the previous speaker (remember to ignore the first row of each episode)
    * loop through each df row and add edge IF check_valid_edge(curr_name,prev_name)
    * if doesn't check add edge, continue

    return graph(?)
    """
    script=pd.read_csv(file).drop(columns=['writer','dialog'])
    script['shifted_pony']=script['pony'].shift()
    script['shifted_title']=script['title'].shift()

    character_count=script['pony'].value_counts().to_dict()
    while len(topchar)<101:
        if len(character_count)==0:
            break
        m=max(character_count,key=character_count.get)
        if check_valid_name(m):
            topchar.append(m)
        character_count.pop(m)

    G=nx.Graph()
    for i,r in script.iterrows():
        s=r.shifted_pony
        d=r.pony
        if r.title != r.shifted_title : #check episode boundaries
            continue
        if s==d:
            continue
        if s not in topchar or d not in topchar:
            continue
        if check_valid_name(s) and check_valid_name(d):
            if G.has_edge(s,d):
                G[s][d]['weight']+=1
            else:
                G.add_edge(s,d,weight=1)

    return G

def count_interactions(G):
    """remember:
    * edge is undirrected
    * to json lowercase names
    """
    inter=dict()
    for char in topchar:
        indi=dict()
        for edge in (G.edges([char],data='weight')):
            indi[edge[1].lower()]=edge[2]
        inter[char.lower()]=indi
    return inter

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-i",help='input',action='store',dest='input',type=str)
    parser.add_argument("-o",help='output',action='store',dest='output',type=str)
    args=parser.parse_args()
    with open(args.input,'r') as f , open(args.output,'w+') as o:
        json.dump(count_interactions(create_graph(f)),o,indent=4)




if __name__ == '__main__':
    main()
