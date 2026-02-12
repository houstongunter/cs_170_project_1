import copy

goal_state = [  [1,2,3],
                [4,5,6],
                [7,8,0]
            ]

nodes_expanded = 0
max_queue_size = 0

def check_goal_state(state):
    return state == goal_state

def print_state(state):
    for i in range(len(state)):
        row_str = ""
        for j in range(len(state[i])):
            row_str += str(state[i][j]) + " "
        print("Row " + str(i + 1) + ": " + row_str.strip())

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
    global nodes_expanded
    expanded_states = []
    up = move_0_up(state[0])
    down = move_0_down(state[0])
    left = move_0_left(state[0])
    right = move_0_right(state[0])
    
    if heuristic == "uniform cost":
        if up != None:
            nodes_expanded += 1
            expanded_states.append([up, state[1]+1, 0])
        if down != None:
            nodes_expanded += 1
            expanded_states.append([down, state[1]+1, 0])
        if left != None:
            nodes_expanded += 1
            expanded_states.append([left, state[1]+1, 0]) 
        if right != None:
            nodes_expanded += 1
            expanded_states.append([right, state[1]+1, 0])
    elif heuristic == "manhattan distance":
        if up != None:
            nodes_expanded += 1
            dist_to_goal = manhattan_distance_heuristic(up)
            expanded_states.append([up, state[1]+1, dist_to_goal])
        if down != None:
            nodes_expanded += 1
            dist_to_goal = manhattan_distance_heuristic(down)
            expanded_states.append([down, state[1]+1, dist_to_goal])
        if left != None:
            nodes_expanded += 1
            dist_to_goal = manhattan_distance_heuristic(left)
            expanded_states.append([left, state[1]+1, dist_to_goal])
        if right != None:
            nodes_expanded += 1
            dist_to_goal = manhattan_distance_heuristic(right)
            expanded_states.append([right, state[1]+1, dist_to_goal])
    elif heuristic == "misplaced tile":
        if up != None:
            nodes_expanded += 1
            dist_to_goal = misplaced_tile_heuristic(up)
            expanded_states.append([up, state[1]+1, dist_to_goal])
        if down != None:
            nodes_expanded += 1
            dist_to_goal = misplaced_tile_heuristic(down)
            expanded_states.append([down, state[1]+1, dist_to_goal])
        if left != None:
            nodes_expanded += 1
            dist_to_goal = misplaced_tile_heuristic(left)
            expanded_states.append([left, state[1]+1, dist_to_goal])
        if right != None:
            nodes_expanded += 1
            dist_to_goal = misplaced_tile_heuristic(right)
            expanded_states.append([right, state[1]+1, dist_to_goal])
    return expanded_states

def a_star(inital_state, heuristic):
    global max_queue_size
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
            print("Goal state found")
            
            return curr_node[1]
        print("Best node to expand is: ")
        print_state(curr_node[0])
        print("Depth of this node is " + str(curr_node[1]))
        print("Heuristic of this node is " + str(curr_node[2]))
        nodes = queuing_function(nodes, expand(curr_node, heuristic))
        if len(nodes) > max_queue_size:
            max_queue_size = len(nodes)
        
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

test_cases = [
    test_state_0,
    test_state_1,
    test_state_2,
    test_state_3,
    test_state_4,
    test_state_5,
    test_state_6,
    test_state_7,
]

def test_algorithm():
    user_reponse = input(("Hello, welcome to 8-Puzzle solver. Enter '1' to choose a default puzzle and '2' for a custom puzzle\n"))
    if user_reponse == "1":
        for i, state in enumerate(test_cases):
            print(f"Test Case {i}:")
            print_state(state)
            print('\n')

        choice = input("Enter the number of the puzzle you want to solve: ")
        custom_state = test_cases[int(choice)]
    
    elif user_reponse == "2":
        print("Enter your custom puzzle:")
        row1 = input("Enter row 1 (3 numbers separated by spaces): ").split()
        row2 = input("Enter row 2 (3 numbers separated by spaces): ").split()
        row3 = input("Enter row 3 (3 numbers separated by spaces): ").split()
        custom_state =  [
                         [int(row1[0]), int(row1[1]), int(row1[2])],
                         [int(row2[0]), int(row2[1]), int(row2[2])],
                         [int(row3[0]), int(row3[1]), int(row3[2])]
                        ]
    else:
        print("Invalid input!")
        return
    
    
    algorithm = input("Enter '1' for Uniform Cost Search, '2' for A* with Misplaced Tile Heuristic, or '3' for A* with Manhattan Distance Heuristic\n")
    
    if algorithm == "1":
        heuristic = "uniform cost"
    elif algorithm == "2":
        heuristic = "misplaced tile"
    elif algorithm == "3":
        heuristic = "manhattan distance"
    else:
        print("Invalid algorithm choice!")
        return

    result = a_star(custom_state, heuristic)
    
    if result == -1:
        print("No solution")
    else:
        global nodes_expanded
        global max_queue_size
        print("Nodes expanded: " + str(nodes_expanded))
        print("Max queue size: " + str(max_queue_size))
        print(f"Solution found at depth {result}")

test_algorithm()