import keys
import praw
import json

empty = ""

covered_mods = {}
covered_subs = {}

reddit = praw.Reddit(
    client_id=keys.client_id,
    client_secret=keys.client_secret,
    user_agent=keys.user_agent,
    username = keys.username,
    password = keys.password
)

turtle = reddit.redditor("awkwardtheturtle")
#get list of subs they moderate
mod = turtle.moderated()
for i in mod:
    #get other mods on that sub
    try:
        other_mod = reddit.subreddit(i.display_name).moderator()
        covered_subs[i.display_name] = []
        for j in other_mod:
            covered_subs[i.display_name].append(j.name)
            try:
                covered_mods[j.name].append(i.display_name)
            except:
                covered_mods[j.name] = [i.display_name]
    except Exception as e:
        print(e)

with open("data/users.json", "w") as f:
    json.dump(covered_mods, f)
    
with open("data/subs.json", "w") as f:
    json.dump(covered_subs, f)