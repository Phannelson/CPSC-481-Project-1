class Course:
    def __init__(self, name, units, prereq, value):
        self.name = name
        self.units = units
        self.prereq = prereq
        self.value = value

class State:
    def __init__(self, completed_units, courses_taken, semester):
        self.completed_units = completed_units
        self.courses_taken = courses_taken
        self.semester = semester

    def __lt__(self, other):
        return self.completed_units < other.completed_units

def is_goal_state(state):
    return state.completed_units == 120

def actions(state, available_courses):
    max_units_per_semester = 9
    actions = []

    for course in available_courses:
        if (
            state.completed_units + course.units <= 120
            and all(prereq in state.courses_taken for prereq in course.prereq)
        ):
            actions.append(course)

    return actions

def apply_action(state, action):
    new_state = State(
        state.completed_units,
        state.courses_taken.copy(),
        state.semester
    )
    new_state.completed_units += action.units
    new_state.courses_taken.append(action.name)
    new_state.semester += 1  
    return new_state

available_courses = [
    Course("CPSC 120", 3, [], 0),
    Course("CPSC 253", 3, [], 0),
    Course("MATH 170A", 3, [], 0),
    Course("MATH 150A", 4, [], 0),
    Course("CPSC 121", 3, ["CPSC 120"], 1),
    Course("MATH 150B", 4, ["MATH 150A"], 1),
    Course("MATH 170B", 3, ["MATH 170A"], 1),
    Course("CPSC 131", 3, ["CPSC 121"], 1),
    Course("CPSC 240", 4, ["CPSC 131"], 1),
    Course("CPSC 362", 3, ["CPSC 131"], 1),
    Course("CPSC 332", 3, ["CPSC 120"], 1),
    Course("MATH 338", 4, ["MATH 150B"], 1),
    Course("MATH 323", 3, ["CPSC 131"], 1),
    Course("CPSC 335", 3, ["CPSC 131"], 1),
    Course("MATH 351", 4, ["CPSC 131"], 1),
    Course("CPSC 315", 3, ["CPSC 131"], 1),
    Course("CPSC 490", 3, ["CPSC 362"], 1),
    Course("CPSC 491", 4, ["CPSC 490"], 1),
    Course("CPSC 481", 3, ["CPSC 335"], 1),
    Course("CPSC 471", 3, ["CPSC 351"], 1),
    Course("CPSC 254", 3, [], 3),
    Course("CPSC 349", 3, [], 3),
    Course("CPSC 375", 3, [], 3),
    Course("CPSC 449", 3, [], 3),
    Course("CPSC 458", 3, [], 3),
    Course("CPSC 488", 3, [], 3),
]

def heuristic(state):
    return 120 - state.completed_units

def astar_search(initial_state, available_courses):
    open_list = [] 
    open_list.append((0, initial_state)) 
    visited = set() 

    while open_list:
        open_list.sort(key=lambda x: x[0]) 
        priority, current_state = open_list.pop(0)

        if is_goal_state(current_state):
            return current_state 

        if current_state in visited:
            continue

        visited.add(current_state)

        for action in actions(current_state, available_courses):
            new_state = apply_action(current_state, action)
            f_value = new_state.completed_units + heuristic(new_state)
            open_list.append((f_value, new_state)) 

    return State(0, [], -1) 

initial_state = State(0, [], 0) 
solution = astar_search(initial_state, available_courses)

if solution.semester == -1:
    print("No solution found.")
else:
    print("Solution found:")
    for semester, course in enumerate(solution.courses_taken, start=1):
        print(f"Semester {semester}: Take {course}")

