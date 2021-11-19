import json, argparse,math


def compute_tfidf(w,pony,script):#compute word's tf-idf score for each pony, return float
    with open(script,'r') as file:
        data=json.load(file)
        tf=(data[pony][w])
        df=0
        for p in data:
            if w in data[p]:
                df+=1

        idf=math.log10(6/df)
        return tf*idf


def list_tfidf(pony,script):# return a dict of words with corresponding tfidf score
    with open(script,'r') as file:
        data=json.load(file)
        tf_dict=dict() #dict of all tfidf score
        for word in data[pony]:
            tf_dict[word]=compute_tfidf(word,pony,script)
    return tf_dict

def choose_max_n(dict,n):#given a dict and n, return a list of n-keys of highest values
    list=[]
    while len(list)<n:
        if len(dict)==0:
            break
        m=max(dict,key=dict.get)

        list.append(m)
        dict.pop(m)
    return list

def do_pony_lis(file,num_words):
    output=dict()
    with open(file,'r') as f:
        data=json.load(f)
        for p in ["Twilight Sparkle", "Applejack", "Rarity", "Pinkie Pie", "Rainbow Dash", "Fluttershy"]:
            pony=p.lower()
            output[pony]=choose_max_n(list_tfidf(pony,file),num_words)

    return output

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("-c",help='word counts file',action='store',dest='file',type=str)
    parser.add_argument("-n",help='num words',action='store',dest='num_words',type=int)
    args=parser.parse_args()

    print(json.dumps(do_pony_lis(args.file,args.num_words),indent=4))
if __name__ == '__main__':
    main()
