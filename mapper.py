from graph_tools import *
import json

from pyvis.network import Network
import networkx as nx

users = {}
subs = {}

def getData():
    global users, subs
    with open("data/subs.json", "r") as f:
        subs = json.load(f)
    with open("data/users.json", "r") as f:
        users = json.load(f)

getData()

g = Network(height = 800, width = 1080, notebook=True)
for i, v in enumerate(subs):
    g.add_node(v, label = v, color = "#000099")
for i, v in enumerate(users):
    g.add_node("u/"+str(v), label = v, color="#FFFFFF")

for i in users:
    for j in users[i]:
        g.add_edge("u/"+str(i), j, weight=10)

g.barnes_hut() #Physics solver or something?
g.show("ex.html")