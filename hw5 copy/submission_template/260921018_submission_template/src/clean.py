import json,argparse
from datetime import datetime,timezone
import pytz

def clean_json(i,s):
    try:
        post=json.loads(i)
        if ("title" not in post) and ("title_text" not in post): #1
            return s
        if "title_text" in post: #2
            post["title"]=post.pop("title_text")
        if "createdAt" in post: #34
            format = "%Y-%m-%dT%H:%M:%S%z"
            u = datetime.strptime(post["createdAt"],format).astimezone(pytz.timezone("utc")).strftime("%Y-%m-%dT%H:%M:%S%z")
            post['createdAt'] = u
        if (not post["author"]) or post["author"]=="N/A" or post["author"]=="null": #6
            return s
        if "total_count" in post: #78
            post['total_count']=int(float(post["total_count"]))
        if "tags" in post: #9
            for i in range(len(post["tags"])):
                x=post["tags"][i].split()
                if len(x)>1:
                    post["tags"].pop(i)
                    i-=1
                    for tag in x:
                        post["tags"].append(tag)
        s=post
        return s
    except: return s



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="input file",action='store',dest="input", type=str)
    parser.add_argument("-o", help="output file",action='store',dest="output", type=str)
    args = parser.parse_args()

    readin= open(args.input,'r').readlines()
    for i in readin:
        a=clean_json(i,"")
        if a == "":
            continue
        with open(args.output,'a+') as out:
            out.seek(0)
            data=out.read(100)
            if len(data)>0:
                out.write('\n')
            json.dump(a,out)




if __name__ == "__main__" :
    main()
