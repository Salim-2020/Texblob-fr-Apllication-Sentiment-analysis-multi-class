import discord
from textblob import TextBlob
import re
from textblob_fr import PatternTagger, PatternAnalyzer
# create discord client, sentiment analyzer and google translater object
client = discord.Client()


def sentiment_analyzer_scores(text):
    blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    obj= blob.sentiment
    pol = obj[0]

    print('______________________SENTIMENT______________________________')
    print("text::", text)
    print(obj)
    print("polarité =", pol)

    if (pol>= -1) and (pol< -0.7):
        print("tres tres mecontent")

    elif (pol >= -0.7) and (pol< -0.4):
        print("tres mecontent")

    elif (pol >= -0.4) and (pol < 0):
        print("mecontent")

    elif  (pol==0):
        print("neutre")

    elif (pol > 0) and (pol < 0.4):
        print("content")

    elif (pol >= 0.4) and (pol < 0.7):
        print("tres content")
    elif (pol >= 0.7) and (pol <= 1):
        print("tres tres content")

#--------------CREAT BOT----------------------------------------#
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('Le client est  ' + str(sentiment))
# run our bot
client.run('< insert your ID >')
#---------------------------------------------------------------------#
