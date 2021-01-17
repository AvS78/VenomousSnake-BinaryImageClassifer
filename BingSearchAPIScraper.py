
# imports

from requests import exceptions
import argparse
import requests
import os
import cv2


# argument parser for command line interaction for search queries 
ap = argparse.ArgumentParser()
# image search query to the Bing Search API e.g. venemous snakes
ap.add_argument("-q","--query", 
                required=True, 
                help="search query to search Bing Image API for")
# Image output directory. important so that labelling later is easier
ap.add_argument("-o","--output",
                required=True,
                help="path to output directory of images")

args = vars(ap.parse_args())

# Global variables declaration

# API_KEY = Bing search API key
API_KEY = "0825c6bb857242de8e7e597000c5f7ee"

# max num of results for a given keyword search
MAX_RESULTS = 250

# group size for results
GROUP_SIZE = 50 

#set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

#Exceptions list
EXCEPTIONS = set([IOError,FileNotFoundError,
                exceptions.RequestException,exceptions.HTTPError,
                exceptions.ConnectionError,exceptions.Timeout])


# Make the search now!! 

#building information for query send to BingSearchAPI

term = args["query"]
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}

#Make the search 
print("[INFO] searching Bing API for '{}'".format(term))
search = requests.get(URL,headers=headers,params=params)
search.raise_for_status()

#Capture the results coming from the BingSearch API
results=search.json()
estNumResults = min(results["totalEstimatedMatches"],MAX_RESULTS)
print("[INFO] {} total results for '{}'".format(estNumResults,term))

#init total number of images downloaded thus far
total = 0

#Loop over the estimated number of results in "GROUP_SIZE" size of groups
for offset in range(0, estNumResults,GROUP_SIZE):
    print("[INFO] making request for group {}--{} of {}...".format(
        offset, offset + GROUP_SIZE, estNumResults))
    params["offset"]=offset
    search=requests.get(URL, headers=headers, params=params)
    search.raise_for_status()
    results = search.json()
    print("[INFO] saving images for group {}-{} of {}...".format(offset, offset+GROUP_SIZE, estNumResults))
    
    #now loop over the results of a given group GROUP_SIZE
    for v in results["value"]:
        try:
            #make a request to downlaod the image
            print("[INFO] fetching: {}".format(v["contentUrl"]))
            r = requests.get(v["contentUrl"],timeout=30)
            # output image path  
            ext = v["contentUrl"][v["contentUrl"].rfind("."):]
            p = os.path.sep.join([args["output"],"{}{}".format(str(total).zfill(8),ext)])
            # write image to local storage
            f = open(p,"wb")
            f.write(r.content)
            f.close()
        except Exception as e:
            if type(e) in EXCEPTIONS:
                print("[INFO] skipping: {}".format(v["contentUrl"]))
                continue
        
        image = cv2.imread(p)
        
        if image is None:
            print("[INFO] deleting: {}".format(p))
            #os.remove(p)
            continue
        #counter++
        total +=1

    



