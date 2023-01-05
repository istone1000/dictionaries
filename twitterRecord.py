#Irene Stone
#Nov 2022
#Twitter Record

twitterRecord = {}
# Build up a twitter record
handle = input("Enter twitter handle :")
twitterRecord['twitterID'] = handle
name = input("Enter name : ")
twitterRecord['name'] = name
tweets = int(input("Enter number of tweets : "))
twitterRecord['tweets'] = tweets
following = int(input("Enter number for following : "))
twitterRecord['following'] = following
followers = int(input("Enter number of followers : "))
twitterRecord['followers'] = followers

print(twitterRecord)
print(twitterRecord[twitterID])