import json
import webbrowser

posts = ['2.14.20.json', '11.29.19.json', '11.19.19.json', '11.6.19.json', '11.2.19.json', '10.31.19.json',
         '10.28.19.json', '10.10.19.json', '10.3.19.json', '10.1.19.json', '9.29.19.json', '9.1.19.json',
         '8.25.19.json', '8.15.19.json', '8.6.19.json', '7.23.19.json', '7.7.19.json', '5.31.19.json',
         '5.25.19.json', '5.18.19.json', '5.12.19.json', '5.2.19.json', '4.22.19.json', '4.17.19.json',
         '4.3.19.json', '4.1.19.json', '3.19.19.json', '3.15.19.json', '1.19.19.json', '1.12.19.json',
         '12.31.18.json', '12.24.18.json', '12.22.18.json', '12.2.18.json', '11.9.18.json', '11.3.18.json']

#      '10.31.18.json', '10.16.18.json', '10.6.18.json', '9.30.18.json', '9.24.18.json', '9.17.18.json',
#      '9.6.18.json', '9.4.18.json', '8.28.18.json', '8.26.18.json', '8.24.18.json', '8.23.18.json',
#      '8.20.18.json', '8.16.18.json', '8.15.18.json', '8.6.18.json', '8.4.18.json', '8.1.18.json',
#      '7.30.18.json', '7.29.18.json', '7.24.18.json', '7.21.18.json', '7.18.18.json', '7.10.18.json',
#      '7.4.18.json', '7.2.18.json', '6.30.18.json', '6.28.18.json', '6.22.18.json', '6.21.18.json',
#      '6.17.18.json', '6.15.18.json', '6.12.18.json', '6.10.18.json', '6.6.18.json', '6.3.18.json',
#      '5.29.18.json', '5.26.18.json', '5.23.18.json']

f = open('following-list.txt')
following_file = f.readlines()
f.close()

g = open('whitelist.txt')
whitelist_orig = g.readlines()
whitelist = []
for account in whitelist_orig:
    whitelist.append(account.strip())
g.close()


def har_parser(post_list):
    likers = []

    for post in post_list:
        with open('posts-data/' + post) as f:
            data = json.load(f)

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


def compare_lists(likers, following):
    to_unfollow = []
    for account in following:
        if (account not in likers) and (account not in whitelist):
            to_unfollow.append(account)

    return to_unfollow


def generate_file(post_list, following_list):
    data = compare_lists(har_parser(post_list), following_list_parser(following_list))
    g = open('to-unfollow.txt', 'w')
    for account in data:
        g.write(account)
        g.write("\n")
    g.close()


def open_account_tabs(file_name):
    h = open(file_name)
    data = h.readlines()
    for account in data:
        webbrowser.open('https://www.instagram.com/' + account)


generate_file(posts, following_file)
# print(whitelist)
# open_account_tabs('to-unfollow.txt')
