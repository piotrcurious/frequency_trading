# This is a code block
# This code is for illustrative purposes only and may not be functional or optimal

# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Defining constants
NUM_CHANNELS = 10 # Number of available channels
NUM_STATIONS = 20 # Number of stations in the network
BANDWIDTH = 100 # Bandwidth of each channel in Mbps
LATENCY = 10 # Latency of each channel in ms
TRADE_THRESHOLD = 0.8 # Threshold for accepting a trade offer
BLACKLIST_THRESHOLD = 0.2 # Threshold for blacklisting a station
WHITELIST_THRESHOLD = 0.9 # Threshold for whitelisting a station

# Creating a network of stations
G = nx.erdos_renyi_graph(NUM_STATIONS, 0.5) # Random graph with 50% probability of edge
nx.set_node_attributes(G, BANDWIDTH, 'bandwidth') # Assigning bandwidth attribute to each node
nx.set_node_attributes(G, LATENCY, 'latency') # Assigning latency attribute to each node
nx.set_node_attributes(G, {}, 'whitelist') # Creating an empty whitelist for each node
nx.set_node_attributes(G, {}, 'blacklist') # Creating an empty blacklist for each node

# Defining a function to calculate the utility of a trade offer
def utility(offer):
    # offer is a tuple of (sender, receiver, channel, time_slot, price)
    sender = offer[0]
    receiver = offer[1]
    channel = offer[2]
    time_slot = offer[3]
    price = offer[4]
    # Utility is the difference between the value and the cost of the trade
    value = G.nodes[receiver]['bandwidth'] * time_slot - G.nodes[receiver]['latency'] * channel
    cost = G.nodes[sender]['bandwidth'] * time_slot + G.nodes[sender]['latency'] * channel + price
    return value - cost

# Defining a function to update the whitelist and blacklist of a station based on a trade outcome
def update_lists(station, partner, outcome):
    # station is the node id of the station
    # partner is the node id of the trading partner
    # outcome is a boolean indicating whether the trade was successful or not
    if outcome: # Trade was successful
        # Increase the rating of the partner by 0.1
        G.nodes[station]['whitelist'][partner] = G.nodes[station]['whitelist'].get(partner, 0.5) + 0.1
        # Remove the partner from the blacklist if present
        if partner in G.nodes[station]['blacklist']:
            del G.nodes[station]['blacklist'][partner]
    else: # Trade was unsuccessful
        # Decrease the rating of the partner by 0.1
        G.nodes[station]['blacklist'][partner] = G.nodes[station]['blacklist'].get(partner, 0.5) - 0.1
        # Remove the partner from the whitelist if present
        if partner in G.nodes[station]['whitelist']:
            del G.nodes[station]['whitelist'][partner]

# Defining a function to simulate a trade between two stations on a given channel and time slot
def trade(sender, receiver, channel, time_slot):
    # sender and receiver are node ids of the stations involved in the trade
    # channel and time_slot are integers indicating the channel and time slot of the trade
    # Generating a random price between 0 and 10 Mbps per ms
    price = np.random.randint(0, 11)
    # Creating a trade offer as a tuple
    offer = (sender, receiver, channel, time_slot, price)
    # Calculating the utility of the offer for both stations
    sender_utility = utility(offer)
    receiver_utility = utility(offer) * -1 # Utility for receiver is opposite of utility for sender
    # Checking if both stations accept the offer based on their utility and trade threshold
    if sender_utility >= TRADE_THRESHOLD and receiver_utility >= TRADE_THRESHOLD:
        print(f"Trade successful between station {sender} and station {receiver} on channel {channel} for {time_slot} ms at {price} Mbps per ms")
        # Updating the whitelist and blacklist of both stations based on the trade outcome
        update_lists(sender, receiver, True)
        update_lists(receiver, sender, True)
        # Returning the trade offer as a result
        return offer
    else:
        print(f"Trade failed between station {sender} and station {receiver} on channel {channel} for {time_slot} ms at {price} Mbps per ms")
        # Updating the whitelist and blacklist of both stations based on the trade outcome
        update_lists(sender, receiver, False)
        update_lists(receiver, sender, False)
        # Returning None as a result
        return None

# Defining a function to create low latency and bulk bandwidth bands by moving traffic to appropriate channels and negotiable time slots
def create_bands():
    # Creating an empty list to store the successful trades
    trades = []
    # Looping over all the channels
    for channel in range(NUM_CHANNELS):
        # Looping over all the edges in the network
        for edge in G.edges():
            # Assigning the sender and receiver of the edge
            sender = edge[0]
            receiver = edge[1]
            # Checking if the sender and receiver are not blacklisted by each other
            if sender not in G.nodes[receiver]['blacklist'] and receiver not in G.nodes[sender]['blacklist']:
                # Generating a random time slot between 1 and 10 ms
                time_slot = np.random.randint(1, 11)
                # Attempting a trade between the sender and receiver on the channel and time slot
                result = trade(sender, receiver, channel, time_slot)
                # If the trade was successful, append it to the trades list
                if result is not None:
                    trades.append(result)
    # Returning the trades list as a result
    return trades

# Calling the create_bands function and storing the result in a variable
trades = create_bands()

# Printing the number of successful trades
print(f"Number of successful trades: {len(trades)}")

# Plotting a histogram of the channels used in the trades
plt.hist([trade[2] for trade in trades], bins=NUM_CHANNELS)
plt.xlabel("Channel")
plt.ylabel("Number of trades")
plt.title("Distribution of trades by channel")
plt.show()

# Plotting a histogram of the time slots used in the trades
plt.hist([trade[3] for trade in trades], bins=10)
plt.xlabel("Time slot (ms)")
plt.ylabel("Number of trades")
plt.title("Distribution of trades by time slot")
plt.show()

# Plotting a histogram of the prices used in the trades
plt.hist([trade[4] for trade in trades], bins=11)
plt.xlabel("Price (Mbps per ms)")
plt.ylabel("Number of trades")
plt.title("Distribution of trades by price")
plt.show()
