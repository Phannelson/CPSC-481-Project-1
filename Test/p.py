class Course:
    def __init__(self, name, units, workload, prerequisites, availability, division, prereq_of):
        self.name = name
        self.units = units
        self.workload = workload
        self.prerequisites = prerequisites
        self.availability = availability
        self.division = division
        self.prereq_of = prereq_of
        self.completed = False  

class State:
    def __init__(self, courses, completed_units, semester):
        self.courses = courses 
        self.completed_units = completed_units
        self.semester = semester

def sem_builder(current_state, max_units_per_semester):
    def sem_builder(current_state, max_units_per_semester):
     available_courses = current_state.available_courses
    selected_courses = []

    for course in available_courses:
        if all(prereq in current_state.courses_taken for prereq in course.prerequisites
               and course.name not in current_state.courses_taken):
            selected_courses.append(course)

    return current_state, selected_courses

def sem_evaluator(state, selected_courses):
     max_units_per_semester = 9
     current_units = 0
     sem_evaluator = []

     for course in selected_courses:
        if (
            state.completed_units + course.units <= 120
            and all(prereq in state.courses_taken for prereq in course.prereq)
            and current_units < max_units_per_semester
        ):
            sem_evaluator.append(course)
            current_units += course.units

     return sem_evaluator

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

def is_goal_state(state):
   return state.completed_units == 120

def astar_search(initial_state, max_units_per_semester):
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

available_courses = {
    "math_requirements": 
    [Course("MATH 170A", 3, [], 0),
    Course("MATH 170B", 3, ["MATH 170A"], 1),
    Course("MATH 150A", 4, [], 0),
    Course("MATH 150B", 4, ["MATH 150A"], 1),
    Course("MATH 338", 4, ["MATH 150B"], 1),],

    "upper_division_courses": 
    [Course("CPSC 253", 3, [], 0),
    Course("CPSC GE", 3, [], 0),
    Course("CPSC GE", 3, [], 0),
    Course("CPSC GE", 3, [], 0),
    Course("CPSC GE", 3, [], 0),
    Course("CPSC GE", 3, [], 0),
    Course("CPSC 131", 3, ["CPSC 121"], 1),
    Course("CPSC 223", 3, ["CPSC 131"], 1),
    Course("CPSC 240", 4, ["CPSC 131"], 1),
    Course("CPSC 315", 3, ["CPSC 131"], 1),
    Course("CPSC 323", 3, ["CPSC 131"], 1),
    Course("CPSC 332", 3, ["CPSC 131"], 1),
    Course("CPSC 335", 3, ["CPSC 131"], 1),
    Course("CPSC 351", 4, ["CPSC 131"], 1),
    Course("CPSC 362", 3, ["CPSC 131"], 1),
    Course("CPSC 471", 3, ["CPSC 351"], 1),
    Course("CPSC 481", 3, ["CPSC 335"], 1),
    Course("CPSC 490", 3, ["CPSC 362"], 1),
    Course("CPSC 491", 4, ["CPSC 490"], 1)],

    "available_electives": 
    [Course("CPSC 254", 3, [], 3),
    Course("CPSC 349", 3, [], 3),
    Course("CPSC 352", 3, [], 3),
    Course("CPSC 375", 3, [], 3),
    Course("CPSC 386", 3, [], 3),
    Course("CPSC 411", 3, [], 3),
    Course("CPSC 431", 3, [], 3),
    Course("CPSC 439", 3, [], 3),
    Course("CPSC 440", 3, [], 3),
    Course("CPSC 449", 3, [], 3),
    Course("CPSC 454", 3, [], 3),
    Course("CPSC 455", 3, [], 3),
    Course("CPSC 456", 3, [], 3),
    Course("CPSC 458", 3, [], 3),
    Course("CPSC 459", 3, [], 3),
    Course("CPSC 462", 3, [], 3),
    Course("CPSC 463", 3, [], 3),
    Course("CPSC 464", 3, [], 3),
    Course("CPSC 466", 3, [], 3),
    Course("CPSC 474", 3, [], 3),
    Course("CPSC 479", 3, [], 3),
    Course("CPSC 483", 3, [], 3),
    Course("CPSC 484", 3, [], 3),
    Course("CPSC 485", 3, [], 3),
    Course("CPSC 486", 3, [], 3),
    Course("CPSC 489", 3, [], 3),
    Course("CPSC 499", 3, [], 3),
    Course("CPSC 495", 3, [], 3)
    ],
}

initial_state = State([], 0, 0)
solution = astar_search(initial_state, available_courses)