def is_valid_entry(entry: tuple[int, int]) -> bool:
    return (
        isinstance(entry, tuple)
        and len(entry) == 2
        and all(isinstance(item, int) for item in entry)
    )


def study_schedule(permanence_period, target_time):
    if any(
        not is_valid_entry(entry) for entry in permanence_period
    ) or not isinstance(target_time, int):
        return None

    present_students = 0
    for student_time in permanence_period:
        if target_time >= student_time[0] and target_time <= student_time[1]:
            present_students += 1

    return present_students
