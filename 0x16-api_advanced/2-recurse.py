import requests

def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        return hot_list

    for post in posts:
        hot_list.append(post["data"]["title"])

    after = data.get("data", {}).get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list

# Example usage
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    result = recurse(subreddit)
    if result is not None:
        print("Number of hot articles:", len(result))
        for title in result:
            print(title)
    else:
        print("None")

