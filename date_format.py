import re

# data of date
DATE = ["2020/01/05",
        "2020/1/5",
        "2020年1月5日",
        "2020-1-5",
        "2020/1/5",
        "2020.1.5",
        "2020/20/20",
        "2020 1 5",
        "2020 01 05",
        "1995w44w47",
        "Thank you",
        "1998/33/52",
        "3020/1/1",
        ]

def pattern_math(date):
    date_type = re.compile(r"""(
        (^\d{4})        # First 4 digits number
        (\D)            # Something other than numbers
        (\d{1,2})       # 1 or 2 digits number
        (\D)            # Something other than numbers
        (\d{1,2})       # 1 or 2 digits number
        )""",re.VERBOSE)

    try:
        hit_date = date_type.search(date)
        bool_value = bool(hit_date)
        if bool_value is True:
            split = hit_date.groups()

            # Tuple unpacking
            year, month, day = int(split[1]),int(split[3]),int(split[5])

        if year>3000 or month >12 or day > 31:
            return False
        else:
            if month <= 9:
                month = '0' + str(month)
            if day <= 9:
                day = '0' + str(day)
            return [str(year), str(month), str(day)]
    except:
        return False

print(pattern_math("22"))