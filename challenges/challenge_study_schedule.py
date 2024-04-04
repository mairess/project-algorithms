from decorators.validate_permanence_period import is_valid_period


@is_valid_period
def study_schedule(permanence_period: list[tuple[int, int]], target_time: int):
    present_students = 0
    for period in permanence_period:
        if target_time >= period[0] and target_time <= period[1]:
            present_students += 1

    return present_students
