import csv, pandas as pd
from csv import DictReader


#1. Data Collection
line_count=0
raw=open('IRAhandle_tweets_1.csv')
fil=open('fildat.tsv','a+')
for row in csv.reader(raw,delimiter=','):
    if line_count == 10001:                                            # looking at the first 10000 tweets only, includes header
        break
    if line_count == 0 or (row[4]=='English' and ('?' not in row[2])): # check if row has question or is not English
        csv.writer(fil,delimiter='\t').writerow(row)                   # convert csv to tsv line and write to a new tsv file
    line_count += 1
raw.close()
fil.close()



#2. Data Annotation
filread=open('fildat.tsv','r')
datwrite=open('trumpbol.tsv', 'w+')
reader=csv.reader(filread, delimiter='\t')
writer=csv.writer(datwrite,delimiter='\t')
newcol=[]
line=next(reader)
line.append('trump_mention')
newcol.append(line)                 # append the new trump_mention field to the file


def findall(p, s):                  # helper function to find all occurence of 'Trump' tweet, return list of all first index 'Trump'
    i = s.find(p)
    result=[i]
    while i != -1:
        i = s.find(p, i+5)
        if i != -1:
            result.append(i)
    return result

def trump_mention(n):               # function to check if 'Trump' of desired criteria is in tweet and return True/False
    o=findall('Trump',n)
    if o[0]==-1:
        return False
    for i in o:
        mention=frontcheck=backcheck=False
        if i==0 and i+4 == -1:
            return True
        if i>0:                     # check front of Trump
            frontcheck = not (n[i-1].isalnum())
        elif i==0:
            frontcheck == True
        if (i+4)!= -1:              # check back of Trump
            backcheck = not (n[i+5].isalnum())
        elif i+4 == -1:
            backcheck==True

        mention= frontcheck and backcheck
        if o.index(i)==-1 or mention==True:
            return mention
    return mention #return true/false for if Trump is mentioned correctly

for line in reader:                 # new trump_mention column included
    line.append(trump_mention(line[2]))
    newcol.append(line)
writer.writerows(newcol)            # write new rows with new field trump_mention to a new file
filread.close()
datwrite.close()

datread=open('trumpbol.tsv','r')
datasetwrite=open('data.tsv','a+')
dictread=csv.DictReader(datread, delimiter='\t')
dictwrite=csv.DictWriter(datasetwrite, delimiter='\t',fieldnames=['tweet_id', 'publish_date', 'content','trump_mention'], extrasaction='ignore')
dictwrite.writeheader()             # choose only the required fields
for l in dictread:
    dictwrite.writerow(l)        # print the required fields and values to dataset.tsv
datread.close()
# I actually had to include this pandas part because I did the whole assignment without using Pandas(couldn't figure out Pandas on Apple's new M1 at first) but then had to do this to pass unittest. I should have rewrote the code using pandas entirely but didn't have enough time.
df_dat=pd.read_csv("data.tsv",delimiter='\t', keep_default_na=False)
df_dat.to_csv('dataset.tsv',sep='\t',index=False)
datasetwrite.close()




#3. Analysis
datasetread=open('dataset.tsv','r')
a1 = [row["trump_mention"] for row in DictReader(datasetread, delimiter='\t')] #list all trump_mention bool in a list for calculation
frac_trump_mentions = round(a1.count('True')/len(a1), 3)                       #compute ratio

resultswrite=open('results.tsv','a+')                                          #create results.tsv file
csv.writer(resultswrite,delimiter='\t').writerow(['result', 'value'])          #insert header
csv.writer(resultswrite,delimiter='\t').writerow(['frac-trump-mentions',frac_trump_mentions]) #insert frac_trump_menitons

"""
todo:
* need to index=false using pd for dataset.tsv. Maybe change name of old dataset.tsv and write old dataset.tsv to new same file with pd and index=False, comment that i didnt have enouggh time
* submission

"""
