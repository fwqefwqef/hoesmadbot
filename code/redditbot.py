import praw #you probably know what this is
from urllib.request import quote #to turn the parent comment into a link
r = praw.Reddit(user_agent='coolguyscavemember',
                         client_id='NGkDcMpu5kMIgA', client_secret="PBEQv_2-dvZxZ2aD73DJ19zizVI",
                         username='hoesmad345', password="hoesmadhoesmad")
r.read_only = False #no idea if this is required. Kept it to be safe.
subreddit = r.subreddit("CoolGuysCave") #get the subreddit. "all" for all comments
 
   
 
comments = subreddit.stream.comments() # get the comment stream
x = 1 #for the counter
for comment in comments: #for each comment in the comments stream. the current comment being processed is called "comment"
    print("found new comment! processing... (" + str(x) + ")") #the str(x) thing is printing the number of the comment being proccesed
    x += 1 #add 1 to the number
    text = str(comment.body) # Fetch body
    try:
        author = str(comment.author) # Fetch author
    except AttributeError: #check if the author has been deleted
        print("Author has been deleted")
        #author was deleted
        continue

    if text.lower() == "hoes mad" and author != "hoesmad345": #check to see the comment is "!lmgtfy". use if text.lower() == "!lmgtfy".lower() to be non-case sensitive, use if "!lmgtfy" in text if you want the comment to be anywhere
            # Generate a message
            print("Attempting Answer")
            message = "hoes mad"
            #quote() url-ifies the text, self explanatory i hope
            try:
                comment.reply(message) #reply to comment
 
            except praw.exceptions.APIException:
                print("praw apiexception")
                continue
            print("Replied to comment by " + author)
