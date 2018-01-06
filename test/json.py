# Complete the function below.
import json
import urllib2


def getMovieTitles(substr):
    def do(data, title_res):
        for d in data:
            title_res.append(json.load(d)["Title"])

    url = "https://jsonmock.hackerrank.com/api/movies/search?Title=%s&page=%s"
    response = urllib2.urlopen(url % (substr, 1))
    response_json = json.load(response)
    data = response_json["data"]
    total_pages = response_json["total_pages"]

    title_res = []
    do(data, title_res)

    for page in range(1, total_pages + 1):
        response = urllib2.urlopen(url % (substr, 1))
        response_json = json.load(response)
        data = response_json["data"]
        do(data, title_res)
    title_res.sort()

    return title_res
