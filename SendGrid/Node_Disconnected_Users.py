#!usr/bin/env python
'''
URL: https://py.checkio.org/en/mission/node-disconnected-users2/

Preface:
All nodes of GridLand are connected so one node can
send emails between the connected nodes. In such a
way, no matter how big the city is all users can
send messages to each other as long as all of the
nodes are connected.

When one of city nodes gets crushed it may leave
the citizens of this node district disconnected
from these emergency emails. It may also leave
districts around the crushed node disconnected if
their nodes do not have other ways to connect.

To resolve this occurrence, the Mayor uses mail-pigeons
– an old method of sending mail that was invented
before the global internal network. All of the
citizens still connected to the network receive
the emergency emails, but the disconnected citizens
receive their messages from these pigeons.

Input:
4 args
- network structure showing connections (list)
- users of each node (dict)
- name of node that sends email
- crashed nodes (list)

Output:
Number of users who won't get an email
'''

def disconnected_users(net, users, source, crushes):
    next_branches = []
    finished_nodes = []
    crushes_reached = 0
    total_connected_users = users.get(source)
    total_users = 0
    for k, v in users.items():
        total_users += v

    # check if source is a crush
    if source in crushes:
        return total_users

    # get initial connections from source
    for connection in net:
        if source in connection:
            if connection[0] != source and connection[0] not in crushes:
                total_connected_users += users.get(connection[0])
                next_branches.append(connection[0])
                finished_nodes.append(source)
            elif connection[1] != source and connection[1] not in crushes:
                total_connected_users += users.get(connection[1])
                next_branches.append(connection[1])
                finished_nodes.append(source)

    finished_nodes = list(set(finished_nodes))

    # find paths from branches
    while True:
        finished_nodes = list(set(finished_nodes))
        crushes_reached = 0
        no_new_additions = 0
        for node in next_branches:
            for connection in net:
                if node in connection:
                    if connection[0] in finished_nodes or connection[1] in finished_nodes:
                        no_new_additions += 1
                        continue
                    elif connection[0] in crushes or connection[1] in crushes:
                        crushes_reached += 1
                    else:
                        if connection[0] != node:
                            total_connected_users += users.get(connection[0])
                            next_branches.append(connection[0])
                            finished_nodes.append(node)
                        elif connection[1] != node:
                            total_connected_users += users.get(connection[1])
                            next_branches.append(connection[1])
                            finished_nodes.append(node)
                            for node in finished_nodes:
                                if node in next_branches:
                                    try:
                                        next_branches.remove(node)
                                    except ValueError:
                                        continue
        if crushes_reached == len(next_branches):
            return total_users - total_connected_users
        if no_new_additions == len(next_branches):
            return total_users - total_connected_users

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"
    assert disconnected_users([
        ["A","B"],
        ["A","C"],
        ["A","D"],
        ["A","E"],
        ["A","F"]
    ], {
        "A":10,
        "C":10,
        "B":10,
        "E":10,
        "D":10,
        "F":10
    },
        "A",["B","C"]) == 20, 'Fourth'
    print('Done. Try to check now. There are a lot of other tests')
