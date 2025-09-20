# Info
full_name = "Julian Bartlett"
student_email = "jdbartlett@ncat.edu"
hometown = "Brooklyn, NY"
graduation_semester = "Spring 2027"
major = "Computer Science"

current_courses = ["MATH 234", "HIS 274", "ENG 250", "COMP 104"]
credit_hours = [3, 3, 3, 3]
completed_courses = ["MATH", "SCIENCE", "AFRICAN HISTORY"]
gpa_history = [3.7, 3.8, 4.0, 4.2]

emergency_contact = ("Mom", "Sara Hill", "929-222-4444")
home_address = ("123 Letter Street", "Brooklyn", "NY", "32185")
instagram_info = ("Instagram", "@NCATGATOR", 312)
twitter_info = ("Twitter", "@NCATCITY", 127)
birthday = ("Birthday", 8, 9, 2005)

current_skills = {"Python", "HTML", "Time management", "Teamwork"}
skills_to_learn = {"JavaScript", "Data structures", "Lynx", "Math"}
career_interests = {"Software development", "Web Engineer", "IT Analyst"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"Sport", "Basketball"}

course_credits = {"COMP 104": 3, "MATH 234": 3, "ENG 250": 3, "HIS 274": 3}
course_professors = {"COMP 104": "Prof. Rhodes", "MATH 234": "Dr. Lee", "ENG 250": "Dr. Martinez","HIS 274": "Dr. Brown",}
course_rooms = { "COMP 104": "Graham 300", "MATH 234": "Marteena 201", "ENG 250": "Holland 121", "HIS 274": "Crosby 210",}
monthly_budget = {"Food": 120, "Entertainment": 50, "Books": 125, "Transportation": 100}
study_hours = {"COMP": 10, "Math": 8, "English": 4, "History": 3}

total_current_credits = sum(credit_hours)
cumulative_gpa = sum(gpa_history) / len(gpa_history)
completed_courses_count = len(completed_courses)
total_weekly_study_hours = sum(study_hours.values())
academic_load = total_current_credits + total_weekly_study_hours
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget["Food"] / 30, 2)
annual_budget_projection = monthly_budget_total * 12
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 2)


total_followers = instagram_info[2] + twitter_info[2]
current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)
skills_count_difference = current_skills_count - skills_to_learn_count

contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}
contact_directory_size = len(contact_directory)


entertainment_backlog_count = len(entertainment_backlog)
workload_score = academic_load

first_course = current_courses[0]
comp104_room = course_rooms["COMP 104"]
comp104_prof = course_professors["COMP 104"]
emergency_contact_phone = emergency_contact[2]

print("\n-- Personal Information --")
print(f"Name: {full_name}")
print(f"Email: {student_email}")
print(f"Hometown: {hometown}")
print(f"Major: {major}")
print(f"Graduation Semester: {graduation_semester}")
print(f"Birthday (MM/DD/YYYY): {birthday[1]:02}/{birthday[2]:02}/{birthday[3]}")

print("\n-- Academic Overview --")
print(f"Current Courses: {', '.join(current_courses)}")
print(f"Completed Courses Count: {completed_courses_count}")
print(f"Credit Hours: {credit_hours}")
print(f"Total Current Credits: {total_current_credits}")
print(f"GPA History: {gpa_history}")
print(f"Cumulative GPA: {round(cumulative_gpa, 2)}")

print("\n-- Course Logistics --")
print(f"COMP 104 Professor: {comp104_prof}")
print(f"COMP 104 Room: {comp104_room}")
print(f"Emergency contact phone is {emergency_contact_phone}")

print("\n-- Study Plan --")
print(f"Study Hours per week: {study_hours}")
print(f"Total Weekly Study Hours: {total_weekly_study_hours}")
print(f"Academic Load Credits + Study Hours: {academic_load}")

print("\n-- Budget Summary --")
print(f"Monthly Budget Categories: {monthly_budget}")
print(f"Monthly Budget Total: ${monthly_budget_total}")
print(f"Daily Food Budget: ${daily_food_budget}")
print(f"Annual Budget Projection: ${annual_budget_projection}")
print(f"Study Cost per Hour: ${study_cost_per_hour}")

print("\n-- Interests & Analytics --")
print(f"Current Skills Count: {current_skills_count}")
print(f"Skills To Learn Count: {skills_to_learn_count}")
print(f"Skills Count Difference: {skills_count_difference}")
print(f"Career Interests: {', '.join(sorted(career_interests))}")
print(f"Hobbies: {', '.join(sorted(hobbies))}")
print(f"Entertainment Backlog Count: {entertainment_backlog_count}")
print(f"Total Social Media Followers Instagram + Twitter: {total_followers}")
print(f"Contact Directory Size: {contact_directory_size}")
print(f"Academic Workload Assessment Score Credits + Hours: {workload_score}")

print("\nReport complete.\n")
