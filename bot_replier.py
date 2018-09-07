import praw
import pdb
import re 
import os 

# Create Reddit instance
reddit = praw.Reddit('bot1')

# Assume the file does not exist 
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
    
# Otherwise, load list of posts that have been replied to
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
