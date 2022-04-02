import discord
from discord import Client, Intents
import pymongo
from pymongo import MongoClient

client = discord.Client()

cluster = MongoClient("")
db = cluster["Scores"]
collection = db["scoreCounter"]

wordstotestby = [
    "word1",
    "word2"
]

token = open("./botToken", "r").read()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='MongoDB'))

@client.event
async def on_message(ctx): 
    print(f"{ctx.channel}: {ctx.author}: {ctx.author.name}: {ctx.content}")
    myquery = { "_id": ctx.author.id }
    if (collection.count_documents(myquery) == 0):
        if any(x in ctx.content for x in wordstotestby):
            post = {"_id": ctx.author.id, "score": 1}
            collection.insert_one(post)
            print(f"Word detected")
    else:
        if any(x in ctx.content for x in wordstotestby):
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                score = result["score"]
            score = score + 1
            collection.update_one({"_id":ctx.author.id}, {"$set":{"score":score}})
            print(f"Word detected")