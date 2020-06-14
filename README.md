# Instagram Engagement Metrics

A personal project for "scraping" Instagram engagement data to analyze.

### Use Case
Many accounts do a "follow for follow" strategy, where they follow accounts so that they follow you back. However, many of those accounts will then mute you (a feature that blocks you from showing up in their feed or story carousel), adding to your follower count, but not your like or comment counts, thus lowering your engagement. For Instagram users hoping to attract brands to work with, a low engagement score is toxic. 

Although Instagram does not allow you to see who has muted you, a strategy for finding "ghost followers" can weed out those who have muted you as well. Ghost followers are accounts that follow you, but don't engage with your posts (through likes or comments). 

Unfortunately, the Instagram API does not provide information on which specific accounts have liked or commented on your posts, so it is impossible to compare a follower list to a list of "likers" solely using the Instagram API. 

### Code Solution

Although the Instagram API does not provide this information, individual users are able to manually view the list of people who have liked a certain post, both in the Instagram app and the Instagram website. 



I tried a variety of methods for pulling this list, from web scrapers, to 

I got the idea to browse the network requests from this video - https://www.youtube.com/watch?v=oLc_-IeZGiE

How to get the follower list file
How to get the following list

What har-parser does 
, parses them then adds accounts to the to-unfollow.txt
white list functionality 


I've included sample data (of following lists, white list, post .har files) for a celebrity's public account (@jenniferaniston).

create a sample data folder
