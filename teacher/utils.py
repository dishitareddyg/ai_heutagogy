
def generate_roadmap(course_outcomes, num_classes, class_duration, class_size):
    roadmap = []

    # Time allocations (example heuristic)
    lecture_time = int(class_duration * 0.5)
    activity_time = int(class_duration * 0.3)
    discussion_time = int(class_duration * 0.2)

    for i in range(1, num_classes + 1):
        roadmap.append({
            "class_number": i,
            "outcome_focus": f"Focus on outcome: {course_outcomes[:50]}...",
            "time_allocation": {
                "Lecture": lecture_time,
                "Activity": activity_time,
                "Discussion": discussion_time,
            },
            "suggested_activity": f"Group task for class size {class_size}",
        })

    return roadmap
