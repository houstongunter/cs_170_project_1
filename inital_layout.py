goal_state = [  [1,2,3],
                [4,5,6],
                [7,8,0]
            ]

def check_goal_state(state):
    return state == goal_state

def move_0_up(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in the top row, then you can't move it up
                if i == 0:
                    return
                temp = state[i-1][j]
                state[i-1].pop(j)
                state[i-1].insert(j, 0)
                state[i].pop(j)
                state[i].insert(j, temp)
                return state        

def move_0_down(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in bottom row, then you can't move it down
                if i == (len(state) - 1):
                    return
                temp = state[i+1][j]
                state[i+1].pop(j)
                state[i+1].insert(j, 0)
                state[i].pop(j)
                state[i].insert(j, temp)
                return state


def move_0_left(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in very left column, then you can't move it left
                if j == 0:
                    return
                temp = state[i][j-1]
                state[i].pop(j-1)
                state[i].insert(j-1, 0)
                state[i].pop(j)
                state[i].insert(j, temp)
                return state
                

def move_0_right(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                # if 0 is in very right column, then you cannot move it right
                if j == (len(state[i]) - 1):
                    return
                temp = state[i][j+1]
                state[i].pop(j+1)
                state[i].insert(j+1, 0)
                state[i].pop(j)
                state[i].insert(j, temp)
                return state
            
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

def uniform_cost_search(inital_state):
    return

def a_star_misplaced_tile(inital_state):
    return

def a_star_manhattan_dsinace(inital_state):
    return