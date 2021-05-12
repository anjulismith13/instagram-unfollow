import json
import webbrowser
import random
import time
from os import listdir

# load posts network requests data
posts = listdir("sample-data/posts-data")

# load passlist data
g = open('sample-data/passlist.txt')
passlist_orig = g.readlines()
passlist = []
for account in passlist_orig:
    passlist.append(account.strip())
g.close()


# parse post network request data for likers
def har_parser(post_list):
    likers = []

    for post in post_list:
        with open('sample-data/posts-data/' + post, encoding='utf8', errors='ignore') as k:
            data = json.load(k)

        query_responses = []

        for entry in data["log"]["entries"]:
            if 'query' in entry["request"]["url"]:
                if 'edge_liked_by' in entry["response"]["content"]["text"]:
                    query_responses.append(entry)

        for queryResponse in query_responses:
            for edge in \
                    json.loads(queryResponse["response"]
                               ["content"]
                               ["text"])["data"]["shortcode_media"][
                        "edge_liked_by"][
                        "edges"]:
                if edge["node"]["username"] not in likers:
                    likers.append(edge["node"]["username"])

    return likers


# parse data on people I follow
def following_list_parser():
    following = []

    with open('sample-data/following-list.txt', encoding='utf8') as following_list:
        for line in following_list:
            if 'profile picture' in line:
                following.append(next(following_list).strip())

    return following


# compare likers to following list and create file of accounts to unfollow
def create_list(post_list, open_tabs=False):
    likers = har_parser(post_list)
    following = following_list_parser()

    filename = 'sample-data/to-unfollow-' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    with open(filename, 'w') as to_unfollow:
        for acc in following:
            if (acc not in likers) and (acc not in passlist):
                to_unfollow.write(acc)
                to_unfollow.write("\n")
        to_unfollow.close()

    if open_tabs:
        h = open(filename)
        data = h.readlines()
        for account_name in data:
            webbrowser.open('https://www.instagram.com/' + account_name)
            time.sleep(random.randrange(0, 2))


create_list(posts, open_tabs=True)
