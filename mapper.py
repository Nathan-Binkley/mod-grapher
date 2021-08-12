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

g = Network(height ="100%", width = "100%", notebook=True, bgcolor="#000", font_color="white")
for i, v in enumerate(subs):
    g.add_node(v, label = v, color = "#000099")
for i, v in enumerate(users):
    if v == "awkwardtheturtle":
        g.add_node("u/"+str(v), label = "u/"+str(v), color="#0F0")
    else:
        g.add_node("u/"+str(v), label = "u/"+str(v), color="#FFFFFF")

for i in users:
    for j in users[i]:
        if i == 'awkwardtheturtle':
            g.add_edge("u/"+str(i), j, weight=10, color="#0F0")
        else:
            g.add_edge("u/"+str(i), j, weight=10, color="#F0F")


g.hrepulsion() #Physics solver or something?
g.show("ex.html")