def study_schedule(
    permanence_period: list[tuple[int, int]], target_time: int
) -> int | None:
    if not permanence_period or target_time is None:
        return None

    for start, end in permanence_period:
        if (
            not isinstance(start, int)
            or not isinstance(end, int)
            or start > end
        ):
            return None

    return sum(start <= target_time <= end for start, end in permanence_period)
