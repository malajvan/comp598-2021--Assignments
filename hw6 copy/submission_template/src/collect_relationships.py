import argparse,json,bs4
import os,hashlib,requests,re

def cache(celeb,dir): #receive a celeb and a cache dir, cache and/or return a string of absolute path of the html file for celeb
    curdir=os.getcwd()
    hashcel=hashlib.sha1(celeb.encode('UTF-8')).hexdigest()
    if not os.path.exists(dir):
        os.mkdir(dir)
        print('mkdir')
    if hashcel+".html" not in os.listdir(dir):
        print('fetching file for '+celeb)
        link='https://www.whosdatedwho.com/dating/<celeb>'
        headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'malajvan@gmail.com'}
        data = requests.get(link.replace('<celeb>',celeb),headers=headers)

        with open(dir+'/'+hashcel+'.html','w+') as f:
            f.write(data.text)
    else: print(celeb+"'s file already there")
    return (dir+"/"+hashcel+".html")

def collect_relationship(file, celname): #receive a celeb file name and celeb name, return a list of people who has relationship with.
    list=[]
    def add_rela(string):
        try:
            name=(string.replace('https://www.whosdatedwho.com/dating/', ''))
            if (celname not in name) and ("-and-" not in name):
                list.append(name)
        except: pass

    with open(file,'r') as read:
        celeb=bs4.BeautifulSoup(read, 'html.parser')
        c= celeb.find(class_= "ff-dating-history").next_element.next_sibling.find_all("a")
        for e in c:
            add_rela(e.get('href'))
    return list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="config file",action='store',dest="config", type=str)
    parser.add_argument("-o", help="output file",action='store',dest="output", type=str)
    args = parser.parse_args()


    config=json.load(open(args.config,'r'))
    cache_dir= config['cache_dir']
    target_celeb=config['target_people']


    result={}

    for celeb in target_celeb:
        file=cache(celeb,cache_dir)
        relationships = collect_relationship(file,celeb)
        result[celeb]=relationships
    with open (args.output,'w+') as out:
        json.dump(result,out,indent=4)

if __name__=='__main__':
    main()
