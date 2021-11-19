import csv,json
import argparse,sys
import random

def gen_randpost (file,n):#take file and numpost to take and return a list of n random posts
    posts=[]
    file_length=range(sum(1 for line in open(file)))
    if len(file_length)>n:
        to_read=random.sample(file_length, n)
        with open(file) as file:
            for i, line in enumerate(file):
                if i in to_read:
                    posts.append(line.strip())
    else:
        with open(file) as file:
            for i, line in enumerate(file):
                posts.append(line.strip())
    return posts

def to_tsv(tsv_file,posts): #receive file to output and a list of posts, dump corresponding to a tsv file
    with open(tsv_file,'a+') as file:
        tsv_writer = csv.writer(file, delimiter='\t')
        for i in posts:
            j=json.loads(i)
            tsv_writer.writerow(list((j['data']['name'],j['data']['title'])))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output file",action='store',dest="output", type=str)
    parser.add_argument(help="json file",action='store',dest="json", type=str)
    parser.add_argument(help="json file",action='store',dest="numpost", type=int)
    args = parser.parse_args()

    post=(gen_randpost(args.json,args.numpost))
    with open (args.output,'a+') as file:
        tsv_writer = csv.writer(file, delimiter='\t')
        tsv_writer.writerow(['Name','title','coding'])
    to_tsv(args.output,post)


if __name__== "__main__":
    main()
