# Complete the function below.
from collections import defaultdict

import re

import operator


def polygon(a, b, c, d):
    def getshape(a, b, c, d):
        if 0 >= min(a, b, c, d):
            return 0
        elif a == b and b == c and c == d:
            return 2
        elif a == c and b == d:
            return 1
        else:
            return 0

    return getshape(a, b, c, d)


# Complete the function below.

def delta_encode(array):
    p = array[0]
    res = [p]
    for i in range(1, len(array)):
        d = array[i] - p
        if abs(d) > 127:
            res.append(-128)
        res.append(d)
        p = array[i]

    return res


def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    def hotel_booking(arrive, depart, k):
        arrive.sort()
        depart.sort()
        i = j = 0
        req = 0
        gb = 0
        while i < len(arrive) or j < len(depart):

            if i < len(arrive) and (j == len(depart) or arrive[i] < depart[j]):
                i += 1
                req += 1
            elif j < len(depart) and (i == len(arrive) or depart[j] < arrive[i]):
                j += 1
                req -= 1
            else:
                i += 1
                j += 1
            gb = max(gb, req)
        return gb - k

    arrive = [call[0] for call in callsTimes]
    depart = [call[1] for call in callsTimes]

    return hotel_booking(arrive, depart, noOfCurrentAgents)


# print howManyAgentsToAdd(1, [[22000, 22020], [22000, 22040], [22030, 22035]])
# Complete the function below.

def sort_hotels(keywords, hotel_ids, reviews):
    from collections import defaultdict
    import re
    def do(keywords, hotel_ids, reviews):
        keywords_set = set(keywords.split(' '))
        hotel_measure = defaultdict(int)

        for i in range(len(hotel_ids)):
            for word in reviews[i].split(' '):
                word = re.sub("[$,.!?]", "", word).lower()
                # word = word.replace("[$,.!?]", "").lower()
                if word in keywords_set:
                    print word
                    hotel_measure[hotel_ids[i]] += 1
            print hotel_measure
        return hotel_measure

    hotel_measure = do(keywords, hotel_ids, reviews)
    hotel_measure_sorted = sorted(hotel_measure.items(), key=lambda x: x[1], reverse=True)
    return [int(i[0]) for i in hotel_measure_sorted]

# def sort_hotels():
#     def do(keywords, hotel_ids, reviews):
#         keywords_set = set(keywords.split(' '))
#         hotel_measure = defaultdict(int)
#
#         for i in range(len(hotel_ids)):
#             for word in reviews[i].split(' '):
#                 word = re.sub("[$,.!?]", "", word).lower()
#                 # word = word.replace("[$,.!?]", "").lower()
#                 if word in keywords_set:
#                     print word
#                     hotel_measure[hotel_ids[i]] += 1
#             print hotel_measure
#         return hotel_measure
#
#     reviews = ["This hotel has a nice view of the citycenter. The location is perfect.",
#                "The breakfast is ok. Regarding the location, it is quite far from citycenter but price is cheap so it is worth.",
#                "Location is excellent, 5 minutes from citycenter. There is also a metro station very close to the hotel.",
#                "They said I could't take my dog and there were other guests with dogs! That is not fair!",
#                "Very friendly staff and goof cost-benefit ratio. Its location is a bit far from citycenter."]
#     keywords = "breakfast beach citycenter location metro view staff price"
#
#     hotel_measure = do(keywords, [1, 2, 1, 1, 2], reviews)
#
#     hotel_measure_sorted = sorted(hotel_measure.items(), key=lambda x: x[1], reverse=True)
#     print [int(i[0]) for i in hotel_measure_sorted]
#
#
# sort_hotels()
