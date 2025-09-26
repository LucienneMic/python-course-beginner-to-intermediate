# Week 11 Solutions

# Exercise 1
import json
data = {"name":"Alice","age":25}
with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json","r") as f
