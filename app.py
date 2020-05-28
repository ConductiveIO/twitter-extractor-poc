import os

import click
import tweepy

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


@click.group()
def twitter():
    pass

@twitter.command()
def auth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    verifier = rawinput("poop")

if __name__ == "__main__":
    twitter()
