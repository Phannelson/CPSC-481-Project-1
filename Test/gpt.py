import heapq

goal = 15
class Course:
    def __init__(self, name, units, prereq, value):
        self.name = name
        self.units = units
        self.prereq = prereq
        self.value = value

class State:
    def __init__(self, completed_units, courses_taken, classes, semester):
        self.completed_units = completed_units
        self.courses_taken = courses_taken  # Dictionary {semester: [list of courses]}
        self.classes = classes  # Number of classes in the current semester
        self.semester = semester




    def __lt__(self, other):
        return self.completed_units < other.completed_units

def is_goal_state(state):
    return state.completed_units == goal

#
def actions(state, available_courses):
    max_units_per_semester = 15
    max_classes = 5
    action = []

    for course in available_courses:
        if (
            state.completed_units + course.units <= goal
            and all(prereq in state.courses_taken[state.semester] for prereq in course.prereq)
            and state.classes < max_classes
            and state.completed_units % max_units_per_semester + course.units <= max_units_per_semester
            and course.name not in state.courses_taken[state.semester]  # Check if the course hasn't been taken in the current semester
        ):
            action.append(course)

    return action


def apply_action(state, action):
    new_state = State(
        state.completed_units + action.units,
        state.courses_taken.copy(),
        state.classes + 1,
        state.semester
    )

    # Copy the list of courses from the current semester to avoid aliasing
    new_state.courses_taken[new_state.semester] = state.courses_taken[new_state.semester][:] 
    new_state.courses_taken[new_state.semester].append(action.name)  # Add the course to the current semester

    # Check if the semester is filled with classes, if so move to the next semester
    if new_state.classes == 5:
        new_state.semester += 1
        new_state.classes = 0
        new_state.courses_taken[new_state.semester] = []  # Initialize the list for the new semester

    return new_state




def heuristic(state):
    return goal - state.completed_units

def astar_search(initial_state, available_courses):
    open_list = []  # Using a list as a priority queue
    heapq.heappush(open_list, (0, initial_state))  # Push a tuple (priority, state)
    visited = set()
    while open_list:
        priority, current_state = heapq.heappop(open_list)  # Pop the state with the lowest priority

        if is_goal_state(current_state):
            return current_state

        if current_state in visited:
            continue

        visited.add(current_state)

        for action in actions(current_state, available_courses):
            new_state = apply_action(current_state, action)
            f_value = new_state.completed_units + heuristic(new_state)
            heapq.heappush(open_list, (f_value, new_state))  # Push the new state with its priority

    return None

available_courses = [
    Course("CPSC 120", 3, [], 0),
    Course("ge", 3, [] , 0),
    Course("CPSC 253", 3, [], 0),
    Course("MATH 170A", 3, [], 0),
    Course("MATH 150A", 4, [], 0),
    Course("CPSC 121", 3, ["CPSC 120"], 1),
    Course("MATH 150B", 4, ["MATH 150A"], 1),
    Course("MATH 170B", 3, ["MATH 170A"], 1),
    Course("CPSC 131", 3, ["CPSC 121"], 1),
    Course("CPSC 240", 4, ["CPSC 131"], 1),
    Course("CPSC 362", 3, ["CPSC 131"], 1),
    Course("CPSC 332", 3, ["CPSC 120"], 1)
]
initial_state = State(0, {1: []}, 0, 1)  # Initialize with the first semester
  # Initializing courses_taken as a dictionary with the first semester as key

solution = astar_search(initial_state, available_courses)

if solution is None:
    print("No solution found.")
else:
    print("Solution found:")
    for semester, courses in solution.courses_taken.items():
        if courses:  # Only print semesters that have courses
            print(f"Semester {semester}: {courses}")



