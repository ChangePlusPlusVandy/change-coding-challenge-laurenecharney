#File Name: main.py
#Author: Lauren Charney
#Email: laurencharney2020@gmail.com
#Date: 9/22/2020

import tweepy as tw
import random

#information for API
consumer_key = "WLu4GUQV6uxabONTzjCnGJm9e"
consumer_secret = "O2bV9snmYRKgFMqHCk1j7P4hjQ4oRCFWXpuiO7losn7Nqu44Ar"
access_token = "2552795065-RhJ1qLbFOwlsBo997Uo6nqJbxUA67JqjbT7qUwW"
access_token_secret = "730FeB99zdW6t9f8vYkWuQglb3xtFwyb3gddl79xZIv3a"

#Give waiting instruction
print("\nPlease wait for the game to load.")
print("\_(ツ)_/¯")
print("")

#create API authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#get names of user's to play game with
users = ["kanyewest", "elonmusk"]

#filter retweets and urls
search = " -filter:retweets" + "-filter:links"

#add 1600 Kayne tweets and 1600 Elon tweets into a list
tweet_list = []
tweet_count = 0
for user_id in users:
    for tweet in tw.Cursor(api.user_timeline, q=search, id=user_id).items(2000):
        if not tweet.retweeted and ('RT @' not in tweet.text) \
                and "@" not in tweet.text\
                and 'https:/' not in tweet.text \
                and 'http:/' not in tweet.text:
            tweet_list.append(tweet)


#BEGIN GAME!

print("WELCOME TO ELONYE GUESSING GAME")
print("Instrcutions:\nA tweet by either Kanye West or Elon Musk will be presented to you."
      "\nTo get points, you must correctly guess who authored the Tweet.\n")
user_input = input("Ready to play? Y/N\n")

#Stats
games_played = 0
number_correct = 0
number_incorrect = 0

while user_input == "Y":
    #get random tweet
    random_value = random.randint(0, len(tweet_list)-1)
    random_tweet = tweet_list[random_value]
    tweet_author = random_tweet.user.screen_name
    print("Tweet: \""+ random_tweet.text + "\"")

    #check if guess is correct
    user_guess = input("\nIs the author kanyewest or elonmusk?\n")
    if user_guess == tweet_author:
        number_correct+=1
        print("Great job! You guessed the author of the tweet correctly")
    else:
        number_incorrect+=1
        print("Oops, you guessed the incorrect author of the tweet. Better luck next time!")

    #print out game stats
    games_played += 1
    print("Status Update:")
    print("\t Games Played: " + str(games_played))
    print("\t Games Won: " + str(number_correct))
    print("\t Games Lost: " + str(number_incorrect))
    print("\t Overall Win Percentage: " + str(number_correct/games_played*100) + "%")

    #check if user wants to continue playing
    user_input = input("\nPlay again? Y/N\n")
    if user_input == "N":
        break

print("Thank you playing! Please play again soon:)")

