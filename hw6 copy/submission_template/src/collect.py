import requests,json
def get_posts (subreddit,outfile): #take 2 strings for subreddit name and outfile path, produce a json file with each reddit post per line
    link='https://www.reddit.com/r/<subred>/new.json?limit=100'
    auth = requests.auth.HTTPBasicAuth('lotCxcmRPBeCjcwc3LHhVQ', 'Ke9QSubeQlcUYFrNtsD9KbokN7d5dg')
    data = {"grant_type": "password", "username": "fake-accvan", "password": "van.mimi"}
    headers = {"User-Agent": "ChangeMeClient/0.1 by fake-accvan"}
    data = requests.get(link.replace("<subred>",subreddit),auth=auth, data=data, headers = {'User-agent': 'your bot 0.1'}).json()
    with open(outfile,'a+') as f:
        for post in data["data"]["children"]:
            f.seek(0)
            d=f.read(100)
            if len(d)>0:
                f.write('\n')
            json.dump(post,f)

def main():
    r_subscriber=["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned"]
    r_post = ["AskReddit", "memes", "politics", "nfl", "nba", "wallstreetbets", "teenagers", "PublicFreakout", "leagueoflegends", "unpopularopinion"]
    for i in r_subscriber:
        get_posts(i,"../sample1.json")
    for a in r_post:
        get_posts(a,"../sample2.json")



if __name__== "__main__":
    main()
