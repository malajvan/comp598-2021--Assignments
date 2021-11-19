import requests,json
import argparse
def get_posts (subreddit,outfile): #take 2 strings for subreddit name and outfile path, produce a json file with each reddit post per line
    link='https://www.reddit.com<subred>/new.json?limit=100'
    auth = requests.auth.HTTPBasicAuth('lotCxcmRPBeCjcwc3LHhVQ', 'Ke9QSubeQlcUYFrNtsD9KbokN7d5dg')
    data = {"grant_type": "password", "username": "fake-accvan", "password": "van.mimi"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by fake-accvan"}
    data = requests.get(link.replace("<subred>",subreddit),auth=auth, data=data, headers = headers).json()
    with open(outfile,'a+') as f:
        for post in data["data"]["children"]:
            f.seek(0)
            d=f.read(100)
            if len(d)>0:
                f.write('\n')
            json.dump(post,f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="output file",action='store',dest="output", type=str)
    parser.add_argument("-s", help="subreddit",action='store',dest="subreddit", type=str)
    args = parser.parse_args()
    get_posts(args.subreddit,args.output)


if __name__== "__main__":
    main()
