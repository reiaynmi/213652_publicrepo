#!/usr/bin/env python
# coding: utf-8

# In[25]:


#sample data
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs1 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}


# In[26]:


'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    status = "no relationship"
    following = False
    followedby = False
    try: #try if from_member exists
        if to_member in social_graph[from_member]["following"]:
            following = True
    except: #return error if from_member does not exist
        status = "Error: member(s) not found in social graph"
    try: #try if to_member is in social graph
        if from_member in social_graph[to_member]["following"]:
            followedby = True
    except: #handle error if to_member is not in social graph but is followed by from_member (who has a social graph
        if following == True:
            status = "Following"
    #outcomes
    if following == True and followedby == True:
        status = "friends"
    elif following == True and followedby == False:
        status = "follower"
    elif following == False and followedby == True:
        status = "followed by"
    return status


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #default case
    status = False
    i = 0
    #list of all vertical cases
    vert = [list(x) for x in zip(*board)]
    #diagonal up case ([0][0], [1][1], ... [i], [i]). convert to set to check number of unique elements
    diagonalup_set = set([board[i][i] for i,v in enumerate(board)])
    #diagonal down case ([0][2], [1][1], ... [i], [len(board) - i -1]). convert to set to check numebr of unique elements
    diagonaldown_set = set([board[i][len(board)-i-1] for i,v in enumerate(board)])
    #iterate for a max of len(board) times until true
    while i < len(board):
        hor_set = set(board[i])
        vert_set = set(vert[i])
        #check if tic tac toe is achieved (only one unique element)
        if len(hor_set)== 1:
            for j in hor_set:
                i = len(board)
                return j
        if len(vert_set) == 1:
            for j in vert_set:
                return j
        if len(diagonalup_set) == 1:
            for j in diagonalup_set:
                return j
        if len(diagonaldown_set) == 1:
            for j in diagonaldown_set:
                return j
        else:
            i+=1
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #list of keys
    legs_keys= list(route_map.keys())
    total = 0
    if (first_stop, second_stop) in legs_keys:
        #recursion function, root case
        return route_map[(first_stop, second_stop)]['travel_time_mins']
    else:
        i = 0
        #iterate for a max of len(route_map) times until root case is achieved
        while i < len(route_map):
            if second_stop in legs_keys[i]:
                if legs_keys[i][0] == second_stop: #second_stop has to be the second stop when searching for routes
                    i+=1
                else:
                    intermediary = legs_keys[i][0]
                    total += eta(first_stop, intermediary, route_map) #recursion
                    total += eta(intermediary, second_stop, route_map) #recursion
                    i = len(route_map)
            else: 
                i +=1 
    return total


# In[32]:


tic_tac_toe(board7)


# In[14]:


for i in burger:
    j = i


# In[15]:


j


# In[ ]:




