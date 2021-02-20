# Setup your slack account with a token:
# Make token as following:
    # https://api.slack.com/apps?new_app=1
    # https://api.slack.com/methods
    # https://api.slack.com/apps/A01NF30677W/oauth?
    # https://api.slack.com/scopes
#   1. https://api.slack.com/custom-integrations/legacy-tokens
#   2. Scroll down a bit untill you see 'create token'
#   3. Click on 'create token'

# %%
# import slacki as slacki
# print(dir(slacki))
# print(slacki.__version__)

# %%
from slacki import slacki
# token='xoxp-123234234235-123234234235-123234234235-adedce74748c3844747aed48499bb'

# from key import slack_token
from key import slack_token
token = slack_token['key']

# %%
# Initialize for channel
sc = slacki(channel='test', token=token)

# Get some info about the channels
channels = sc.get_channels()

# Get some info about the users
users = sc.get_users()

 # Send messages
queries=['message 1','message 2']
sc.post(queries)

# Snoozing
sc.snooze(minutes=1)

# Post file
file='./data/slack.png'
file = 'D://REPOS/slacki/slacki/data/slack.png'
sc.post_file(file=file, title='Nu ook met figuren uploaden :)')

# listen (retrieve only last message)
out = sc.retrieve_posts(n=3, retrieve_names=True)
out = sc.retrieve_posts(n=3, retrieve_names=False)

# %% listen (retrieve only last message)
todo = sc.listen()


# %% NEW VERSION
import os
from slackclient import SlackClient

# from dotenv import load_dotenv
# load_dotenv()

from key import slack_token
sc = SlackClient(slack_token['key'])


sc.api_call("chat.postMessage", channel="botte_bot", text="Bericht!!!! :parrot:")

user_messages = [m['user'] for m in sc.api_call("conversations.history", channel="G01NLAYR4UU", count=10)['messages']][::-1]
user_messages = [m['user'] for m in self.sc.api_call("conversations.list")['messages']][::-1]

sc.api_call("conversations.list", channel="G01NLAYR4UU", count=10)


channels = [m['name'] for m in sc.api_call("conversations.list")['channels']]


conversations.list

from collections import Counter
count_user = Counter(user_messages)

users = sc.api_call("users.list", channel="G01NLAYR4UU")
user_dict = {m['id']:m['profile']['real_name'] for m in users['members']} # real name or display name?

sc.api_call("conversations.create", name="hedylogos", is_private=False)

self.sc.api_call("users.list")['members'][4]



print("The top users that needs the most messages is:")
for user_id, cnt in count_user.items():
    print(f'\t{user_dict[user_id]} with {cnt} messages')


