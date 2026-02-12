goal_state = [  [1,2,3],
                [4,5,6],
                [7,8,0]
            ]

def check_goal_state(state):
    return state == goal_state

def move_0_up(state):
    new_state = [row[:] for row in state]
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
    new_state = [row[:] for row in state]
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
    new_state = [row[:] for row in state]
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
    new_state = [row[:] for row in state]
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

def uniform_cost_queuing_function(nodes, new_nodes):
    for new_node in new_nodes:
        i = 0
        while i < len(nodes) and nodes[i][1] <= new_node[1]:
            i += 1
        nodes.insert(i, new_node)
    
    return nodes

def expand(state):
    expanded_states = []
    up = move_0_up(state[0])
    down = move_0_down(state[0])
    left = move_0_left(state[0])
    right = move_0_right(state[0])
    if up != None:
        expanded_states.append([up, state[1]+1])
    if down != None:
        expanded_states.append([down, state[1]+1])
    if left != None:
        expanded_states.append([left, state[1]+1]) 
    if right != None:
        expanded_states.append([right, state[1]+1])
    return(expanded_states)

def uniform_cost_search(inital_state):
    nodes = []
    distance = 0
    nodes.append([inital_state, distance])
    while True:
        if len(nodes) == 0:
            return -1
        curr_node = nodes.pop(0)
        if check_goal_state(curr_node[0]):
            return curr_node[1]
        nodes = uniform_cost_queuing_function(nodes, expand(curr_node))

def a_star_misplaced_tile(inital_state):
    return

def a_star_manhattan_dsinace(inital_state):
    return