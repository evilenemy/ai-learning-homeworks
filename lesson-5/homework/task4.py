# universities = [
#   ["California Institute of Technology", 2175, 37704],
#   ["Harvard", 19627, 39849],
#   ["Massachusetts Institute of Technology", 10566, 40732],
#   ["Princeton", 7802, 37000],
#   ["Rice", 5879, 35551],
#   ["Stanford", 19535, 40569],
#   ["Yale", 11701, 40500],
# ]


# def enrollment_stats(universities: list):
#   return [x[1] for x in universities], [x[2] for x in universities]


# def mean(mean_list: list):
#   return sum(mean_list) / len(mean_list)


# def median(median_list: list):
#   return sorted(median_list)[len(median_list) // 2]


# print(
#   f"******************************\n\
#     Total students: {sum(enrollment_stats(universities)[0]):,}\n\
#     Total tuition: ${sum(enrollment_stats(universities)[1]):,}\n\
#     Student mean: {mean(enrollment_stats(universities)[0]):,.2f}\n\
#     Student median: {median(enrollment_stats(universities)[0]):,}\n\
#     Tuition mean: ${mean(enrollment_stats(universities)[1]):,.2f}\n\
#     Tuition median: ${median(enrollment_stats(universities)[1]):,}\n\
#     ******************************"
# )
