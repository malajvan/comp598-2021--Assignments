import json, os, sys
def compute_average_title_length (input):
    p=open(input,'r+').readlines()
    post_num=0
    length=0
    for i in p:
        post=json.loads(i)
        try:
            length+=len(post['data']['title'])
        except TypeError: length+=0
        post_num+=1
    return (round(length/post_num,2))
def main():
    input = sys.argv[1]
    print(compute_average_title_length(input))

if __name__=='__main__':
    main()
