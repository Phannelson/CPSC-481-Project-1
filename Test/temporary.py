goal = 30
class Course:
    def __init__(self, name, units, prereq, value):
        self.name = name
        self.units = units
        self.prereq = prereq
        self.value = value
def semester_scheduling(state, available_courses):
    max_units_per_semester = 15
    max_classes = 5
    action = []
        
    for course in available_courses:
        if (
            state.completed_units + course.units <= goal
            and all(prereq in state.courses_taken for prereq in course.prereq)
            and state.classes < max_classes
            and state.completed_units % max_units_per_semester + course.units <= max_units_per_semester
            and course.name not in state.courses_taken  # Check if the course hasn't been taken
        ):
            action.append(course)

    return action