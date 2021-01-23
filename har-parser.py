import json
import webbrowser
import random
import time
from os import listdir

posts = listdir("../posts-data")

f = open('following-list.txt')
following_file = f.readlines()
f.close()

g = open('passlist.txt')
passlist_orig = g.readlines()
passlist = []
for account in passlist_orig:
    passlist.append(account.strip())
g.close()


def har_parser(post_list):
    likers = []

    for post in post_list:
        with open('posts-data/' + post) as k:
            data = json.load(k)

        query_responses = []

        for entry in data["log"]["entries"]:
            if 'query' in entry["request"]["url"]:
                query_responses.append(entry)

        for queryResponse in query_responses:
            for edge in \
                    json.loads(queryResponse["response"]["content"]["text"])["data"]["shortcode_media"][
                        "edge_liked_by"][
                        "edges"]:
                if edge["node"]["username"] not in likers:
                    likers.append(edge["node"]["username"])

    return likers


def following_list_parser(following_list):
    following = []

    for line in following_list:
        if 'profile picture' in line:
            end_index = line.find("'")
            following.append(line[:end_index])

    return following


def compare_lists(post_list, following_list):
    likers = har_parser(post_list)
    following = following_list_parser(following_list)

    filename = time.strftime("%Y%m%d-%H%M%S")
    h = open(filename, 'w')

    for acc in following:
        if (acc not in likers) and (acc not in passlist):
            h.write(acc)
            h.write("\n")
        h.close()

    # to_unfollow = []
    # for account in following:
    #     if (account not in likers) and (account not in passlist):
    #         to_unfollow.append(account)
    #
    # return to_unfollow


# def generate_file(post_list, following_list):
#     data = compare_lists(har_parser(post_list), following_list_parser(following_list))
#     g = open('to-unfollow.txt', 'w')
#     for account in data:
#         g.write(account)
#         g.write("\n")
#     g.close()


def open_account_tabs(file_name):
    h = open(file_name)
    data = h.readlines()
    for account_name in data:
        webbrowser.open('https://www.instagram.com/' + account_name)
        time.sleep(random.randrange(0, 2))

compare_lists(posts, following_file)
compare_lists(posts, following_file)
# open_account_tabs('to-unfollow.txt')
