import pandas as pd
import argparse,json



def counter (inp,out):
    ano_file=pd.read_csv(inp,sep='\t')
    count=ano_file['coding'].value_counts()
    for i in ['c','f','r','o']:
        if i not in count:
            count[i]=0
    dict={'course-related': int(count['c']), 'food-related': int(count['f']), 'residence-related': int(count['r']), 'other': int(count['o'])}
    js=json.dumps(dict,indent=4)
    if out==None:
        print(js)
    else:
        with open(out,'w+') as out:
            out.write(js)

            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file",action='store',dest="input", type=str)
    parser.add_argument("-o", help="output",action='store',dest="output", type=str)
    args = parser.parse_args()
    counter(args.input,args.output)

if __name__ == '__main__':
    main()
