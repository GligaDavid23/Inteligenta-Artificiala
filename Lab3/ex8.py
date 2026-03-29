data = "2023-04-24 09:03:32.744178"

get_date = lambda s: s.split(" ")[0]
get_time = lambda s: s.split(" ")[1]
get_year = lambda s: s.split("-")[0]
get_month = lambda s: s.split("-")[1]
get_day = lambda s: s.split("-")[2]

date_part = get_date(data)

print(get_year(date_part))
print(get_month(date_part))
print(get_day(date_part))
print(get_time(data))
