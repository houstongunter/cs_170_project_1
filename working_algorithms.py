import copy

goal_state = [  [1,2,3],
                [4,5,6],
                [7,8,0]
            ]

def check_goal_state(state):
    return state == goal_state

def move_0_up(state):
    new_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in the top row, then you can't move it up
                if i == 0:
                    return
                temp = state[i-1][j]
                new_state[i-1].pop(j)
                new_state[i-1].insert(j, 0)
                new_state[i].pop(j)
                new_state[i].insert(j, temp)
                return new_state        

def move_0_down(state):
    new_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in bottom row, then you can't move it down
                if i == (len(state) - 1):
                    return
                temp = state[i+1][j]
                new_state[i+1].pop(j)
                new_state[i+1].insert(j, 0)
                new_state[i].pop(j)
                new_state[i].insert(j, temp)
                return new_state


def move_0_left(state):
    new_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in very left column, then you can't move it left
                if j == 0:
                    return
                temp = state[i][j-1]
                new_state[i].pop(j-1)
                new_state[i].insert(j-1, 0)
                new_state[i].pop(j)
                new_state[i].insert(j, temp)
                return new_state
                

def move_0_right(state):
    new_state = copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in very right column, then you cannot move it right
                if j == (len(state[i]) - 1):
                    return
                temp = state[i][j+1]
                new_state[i].pop(j+1)
                new_state[i].insert(j+1, 0)
                new_state[i].pop(j)
                new_state[i].insert(j, temp)
                return new_state

def misplaced_tile_heuristic(state):
    misplaced_tiles = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            # we skip the empty space
            if state[i][j] == 0:
                continue
            if state[i][j] != goal_state[i][j]:
                misplaced_tiles += 1
    return misplaced_tiles


def manhattan_distance_heuristic(state):
    curr_num = 1
    total_manhattan_distance = 0
    goal_state_x = 0
    goal_state_y = 0
    while curr_num <= 8:
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == curr_num:
                    x = abs(i - goal_state_x)
                    y = abs(j - goal_state_y)
                    total_manhattan_distance = total_manhattan_distance + x + y
                    curr_num += 1
                    if goal_state_y < 2:
                        goal_state_y += 1
                    else:
                        goal_state_y = 0
                        goal_state_x += 1

    return total_manhattan_distance

def queuing_function(nodes, new_nodes):
    for new_node in new_nodes:
        i = 0
        while i < len(nodes) and nodes[i][1] + nodes[i][2] <= new_node[1] + new_node[2]:
            i += 1
        nodes.insert(i, new_node)
    
    return nodes

def compare_states(state1, state2):
    for i in range(len(state1)):
        for j in range(len(state1[i])):
            if state1[i][j] != state2[i][j]:
                return False
    return True

def expand(state, heuristic):
    expanded_states = []
    up = move_0_up(state[0])
    down = move_0_down(state[0])
    left = move_0_left(state[0])
    right = move_0_right(state[0])
    
    if heuristic == "uniform cost":
        if up != None:
            expanded_states.append([up, state[1]+1, 0])
        if down != None:
            expanded_states.append([down, state[1]+1, 0])
        if left != None:
            expanded_states.append([left, state[1]+1, 0]) 
        if right != None:
            expanded_states.append([right, state[1]+1, 0])
    elif heuristic == "manhattan distance":
        if up != None:
            dist_to_goal = manhattan_distance_heuristic(up)
            expanded_states.append([up, state[1]+1, dist_to_goal])
        if down != None:
            dist_to_goal = manhattan_distance_heuristic(down)
            expanded_states.append([down, state[1]+1, dist_to_goal])
        if left != None:
            dist_to_goal = manhattan_distance_heuristic(left)
            expanded_states.append([left, state[1]+1, dist_to_goal])
        if right != None:
            dist_to_goal = manhattan_distance_heuristic(right)
            expanded_states.append([right, state[1]+1, dist_to_goal])
    elif heuristic == "misplaced tile":
        if up != None:
            dist_to_goal = misplaced_tile_heuristic(up)
            expanded_states.append([up, state[1]+1, dist_to_goal])
        if down != None:
            dist_to_goal = misplaced_tile_heuristic(down)
            expanded_states.append([down, state[1]+1, dist_to_goal])
        if left != None:
            dist_to_goal = misplaced_tile_heuristic(left)
            expanded_states.append([left, state[1]+1, dist_to_goal])
        if right != None:
            dist_to_goal = misplaced_tile_heuristic(right)
            expanded_states.append([right, state[1]+1, dist_to_goal])
    return expanded_states

def a_star(inital_state, heuristic):
    nodes = []
    depth = 0
    dist_to_goal = 0 # we can do this because the inital state is going to be the first node expanded anyways
    nodes.append([inital_state, depth, dist_to_goal])
    visited_nodes = []
    while True:
        if len(nodes) == 0:
            return -1
        curr_node = nodes.pop(0)
        # make sure we haven't already visited this node
        visited = False
        for state in visited_nodes:
            if compare_states(state, curr_node[0]):
                visited = True
                break
        if visited == True:
            continue
        visited_nodes.append(curr_node[0])
        if check_goal_state(curr_node[0]):
            return curr_node[1]
        nodes = queuing_function(nodes, expand(curr_node, heuristic))

test_state_0 = [    [1,2,3],
                    [4,5,6],
                    [7,8,0]
                ]

test_state_1 = [    [1,2,3],
                    [4,5,6],
                    [0,7,8]
                ]

test_state_2 = [    [1,2,3],
                    [5,0,6],
                    [4,7,8]
                ]

test_state_3 = [    [1,3,6],
                    [5,0,2],
                    [4,7,8]
                ]

test_state_4 = [    [1,3,6],
                    [5,0,7],
                    [4,8,2]
                ]

test_state_5 = [    [1,6,7],
                    [5,0,3],
                    [4,8,2]
                ]

test_state_6 = [    [7,1,2],
                    [4,8,5],
                    [6,3,0]
                ]

test_state_7 = [    [0,7,2],
                    [4,6,1],
                    [3,5,8]
                ]
# uniform cost test cases
print("uniform cost test case 0: " + str(a_star(test_state_0, "uniform cost")))
print("uniform cost test case 1: " + str(a_star(test_state_1, "uniform cost")))
#print("uniform cost test case 2: " + str(a_star(test_state_2, "uniform cost")))
#print("uniform cost test case 3: " + str(a_star(test_state_3, "uniform cost")))
#print("uniform cost test case 4: " + str(a_star(test_state_4, "uniform cost")))
#print("uniform cost test case 5: " + str(a_star(test_state_5, "uniform cost")))
#print("uniform cost test case 6: " + str(a_star(test_state_6, "uniform cost")))
#print("uniform cost test case 7: " + str(a_star(test_state_7, "uniform cost")))

# misplaced tile test cases
print("misplaced tile test case 0: " + str(a_star(test_state_0, "misplaced tile")))
print("misplaced tile test case 1: " + str(a_star(test_state_1, "misplaced tile")))
# print("misplaced tile test case 2: " + str(a_star(test_state_2, "misplaced tile")))
# print("misplaced tile test case 3: " + str(a_star(test_state_3, "misplaced tile")))
# print("misplaced tile test case 4: " + str(a_star(test_state_4, "misplaced tile")))
# print("misplaced tile test case 5: " + str(a_star(test_state_5, "misplaced tile")))
# print("misplaced tile test case 6: " + str(a_star(test_state_6, "misplaced tile")))
# print("misplaced tile test case 7: " + str(a_star(test_state_7, "misplaced tile")))

# manhattan distance test cases
# print("manhattan distance test case 0: " + str(a_star(test_state_0, "manhattan distance")))
# print("manhattan distance test case 1: " + str(a_star(test_state_1, "manhattan distance")))
# print("manhattan distance test case 2: " + str(a_star(test_state_2, "manhattan distance")))
# print("manhattan distance test case 3: " + str(a_star(test_state_3, "manhattan distance")))
# print("manhattan distance test case 4: " + str(a_star(test_state_4, "manhattan distance")))
# print("manhattan distance test case 5: " + str(a_star(test_state_5, "manhattan distance")))
# print("manhattan distance test case 6: " + str(a_star(test_state_6, "manhattan distance")))
print("manhattan distance test case 7: " + str(a_star(test_state_7, "manhattan distance")))