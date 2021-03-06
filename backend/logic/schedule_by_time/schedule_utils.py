
# join string to make response to user
def make_pretty_string(schedule):
    pretty_string = ''
    for item in schedule:
        text_extracted, subjects = item
        pretty_string += (text_extracted + ':\n')
        if len(subjects) == 0:
            pretty_string += 'Không có môn học nào!'
        elif (len(subjects) == 1) and (subjects[0]['semester'] == None):
            pretty_string += 'Không thuộc vào kì học này!'
        else:
            for subject in subjects:
                pretty_string += "|".join([subject['semester'], subject['time'], subject['classroom'], subject['subject_name']]) + '\n'
        pretty_string += '\n'
    return pretty_string


# get array of week of subject
def get_weeks_of_subject(subject_schedule):

    weeks = subject_schedule['weeks']
    if len(weeks.split(',')) == 2:  # 28-35,37-44
        week_A_start = int(weeks.split(',')[0].split('-')[0])
        week_A_end = int(weeks.split(',')[0].split('-')[1])
        week_B_start = int(weeks.split(',')[1].split('-')[0])
        week_B_end = int(weeks.split(',')[1].split('-')[1])

        weeks = list(range(week_A_start, week_A_end + 1))
        weeks.extend(list(range(week_B_start, week_B_end + 1)))
    else:                           # 33,35,38,40,42,44
        weeks = weeks.split(",")
    return weeks


# extract time_str from time_entity
def get_time_str(time_entity):
    type = time_entity['additional_info']['type']
    if (type == 'value'):
        return time_entity['value']
    else:
        return time_entity['value']['from']
