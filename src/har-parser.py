import json
import os


def get_all_accounts_followed():
    """
        Input: None
        Returns: a list of accounts followed
    """
    with open("data/my-following-list.txt", "r", errors="replace") as following_file:
        return [line.strip()[:line.index("'")] for line in following_file.readlines() if "profile picture" in line]


def get_non_passlist_accounts_followed():
    """
        Input: None
        Returns: a list of account followed that are not on the passlist
    """
    with open("data/my-passlist.txt", "r", errors="replace") as passlist_file:
        passlist = [account.strip() for account in passlist_file.readlines()]
    return [account for account in get_all_accounts_followed() if account not in passlist]


def get_accounts_to_unfollow():
    """
        Input: None
        Returns: a list of accounts followed that haven't engaged with recent posts
    """
    potential_accounts_to_unfollow = get_non_passlist_accounts_followed()
    likers_list = []
    for post in os.listdir("data/posts"):
        with open("data/posts/" + post, "r", errors="replace") as post_file:
            for liker in json.loads(post_file.read())["users"]:
                likers_list.append(liker["username"])
    return [account for account in potential_accounts_to_unfollow if account not in likers_list]


get_accounts_to_unfollow()
