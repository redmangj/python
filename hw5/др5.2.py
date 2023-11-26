students = {'bob': {'jakson': ['Python', 'Java']}, 'bill': {'smit': ['FrontEnd', 'FullStack']}, 'jack': {'wels': ['FrontEnd']}, 'Ann': {'Kalahan': ['Java']}}
for s_name in students.values():
    for group in s_name.values():
        if len(group) > 1:
            print(f"Студенти які займаються більш ніж в одному класі:", list(s_name))
for s_name in students.values():
    for group in s_name.values():
        if group.count('FrontEnd') <= 0:
            print(f"Студенти яку не навчяються на курсі FrontEnd ", list(s_name))
for s_name in students.values():
    for group in s_name.values():
        if group.count('Python') > 0 or group.count('Java') > 0:
            print(f"Студенти які вчатся в класі Python чи Java ", list(s_name))