def is_valid_period(func):

    def validate(permanence_period, target_time):
        if target_time is None:
            return None
        for period in permanence_period:
            if not (
                isinstance(period, tuple)
                and len(period) == 2
                and all(isinstance(item, int) for item in period)
            ):
                return None
        return func(permanence_period, target_time)

    return validate
