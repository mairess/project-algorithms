def is_valid_period(permanence_period: list[tuple[int, int]]) -> bool:
    for period in permanence_period:
        if not (
            isinstance(period, tuple)
            and len(period) == 2
            and all(isinstance(item, int) for item in period)
        ):
            return False
    return True


def study_schedule(permanence_period: list[tuple[int, int]], target_time: int):
    if not is_valid_period(permanence_period) or not isinstance(
        target_time, int
    ):
        return None

    present_students = 0
    for period in permanence_period:
        if target_time >= period[0] and target_time <= period[1]:
            present_students += 1

    return present_students
