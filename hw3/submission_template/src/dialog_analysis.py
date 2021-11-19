import json, sys,csv,re
dialog_file = sys.argv[3]       #read command line for input file
out_file = sys.argv[2]          #read command line for output file


ts_count=aj_count=rr_count=pp_count=rd_count=fs_count=0
with open (dialog_file, 'r') as dialog:
    for l in csv.reader(dialog, delimiter=','):                 #compute count for each pony's line
        if re.search("twilight sparkle", l[2], re.IGNORECASE):
            ts_count+=1
        if re.search("applejack", l[2], re.IGNORECASE):
            aj_count+=1
        if re.search("rarity", l[2], re.IGNORECASE):
            rr_count+=1
        if re.search("pinkie pie", l[2], re.IGNORECASE):
            pp_count+=1
        if re.search("rainbow dash", l[2], re.IGNORECASE):
            rd_count+=1
        if re.search("fluttershy", l[2], re.IGNORECASE):
            fs_count+=1

pon_sum= ts_count+aj_count+rr_count+pp_count+rd_count+fs_count # find sum of six ponies' lines
ts_ver = round(ts_count/pon_sum,2)
aj_ver = round(aj_count/pon_sum,2)
rr_ver = round(rr_count/pon_sum,2)
pp_ver = round(pp_count/pon_sum,2)
rd_ver = round(rd_count/pon_sum,2)
fs_ver = round(fs_count/pon_sum,2)

dict={
    "count": {
        "twilight sparkle": ts_count,
        "applejack": aj_count,
        "rarity":rr_count,
        "pinkie pie": pp_count,
        "rainbow dash": rd_count,
        "fluttershy": fs_count
        },
    "verbosity":{
        "twilight sparkle": ts_ver,
        "applejack": aj_ver,
        "rarity":rr_ver,
        "pinkie pie": pp_ver,
        "rainbow dash": rd_ver,
        "fluttershy": fs_ver

        }
    }
json.dump(dict, open(out_file,'w'), indent=3)
"""
TO DO:

    1) analyze clean_dialog --> finish
        * count part:
            - find each names, then count. if else? one loop
            - append to each count if find name
        * verbosity part:
            - while append to each, append to final sum
            - divide each by final sum for verbosity
    2) print to json
"""
