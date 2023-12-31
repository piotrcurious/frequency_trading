# frequency_trading
junkbox to brainstorm over frequency trading in 802.11
Created by BingAI 
Sure, I'll try to explain how this code works. Here is a summary:

- The code imports some libraries that are useful for the task, such as numpy, pandas, matplotlib and networkx.
- The code defines some constants that are used throughout the code, such as the number of channels, the number of stations, the bandwidth and latency of each channel, and the thresholds for trading, blacklisting and whitelisting.
- The code creates a network of stations using a random graph model and assigns some attributes to each node, such as bandwidth, latency, whitelist and blacklist.
- The code defines a function to calculate the utility of a trade offer for a station. The utility is the difference between the value and the cost of the trade. The value is the amount of bandwidth gained minus the latency incurred by using a channel. The cost is the amount of bandwidth lost plus the latency incurred by using a channel plus the price paid or received for the trade.
- The code defines a function to update the whitelist and blacklist of a station based on a trade outcome. The whitelist and blacklist are dictionaries that store the ratings of other stations as keys and values. The ratings range from 0 to 1, where 0 means very untrustworthy and 1 means very trustworthy. The function increases or decreases the rating of a trading partner by 0.1 depending on whether the trade was successful or not. It also removes the partner from the opposite list if present.
- The code defines a function to simulate a trade between two stations on a given channel and time slot. The function generates a random price for the trade and creates a trade offer as a tuple. It then calculates the utility of the offer for both stations and checks if they both accept it based on their utility and trade threshold. If they do, it prints a message indicating that the trade was successful and updates their whitelist and blacklist accordingly. It also returns the trade offer as a result. If they don't, it prints a message indicating that the trade was unsuccessful and updates their whitelist and blacklist accordingly. It also returns None as a result.
- The code defines a function to create low latency and bulk bandwidth bands by moving traffic to appropriate channels and negotiable time slots. The function creates an empty list to store the successful trades and loops over all the channels and edges in the network. For each edge, it assigns the sender and receiver of the edge and checks if they are not blacklisted by each other. If they are not, it generates a random time slot for the trade and attempts a trade between them on the channel and time slot using the previous function. If the trade was successful, it appends it to the trades list. It then returns the trades list as a result.
- The code calls the create_bands function and stores the result in a variable called trades. It then prints the number of successful trades.
- The code plots some histograms to show the distribution of trades by channel, time slot and price using matplotlib.

I hope this helps you understand how this code works.
