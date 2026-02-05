"""
COMP 163 - Chapter 3 Assignment: Personal Data Portfolio
Name: Julian Bartlett
Purpose: Practice strings, lists, tuples, sets, and dictionaries.
"""

# ===== 1) PERSONAL INFORMATION (strings) =====
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# ===== 2) ACADEMIC DATA (lists) =====
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

# ===== 3) CONTACT INFO (tuples) =====
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

# ===== 4) INTEREST TRACKING (sets) =====
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# ===== 5) ORGANIZATIONAL MAPPING (dictionaries) =====
course_credits = {
    "COMP 163": 3,
    "MATH 150": 3,
    "ENG 101": 3,
    "HIS 105": 3
}

course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 150": "Dr. Lee",
    "ENG 101": "Dr. Martinez",
    "HIS 105": "Dr. Brown"
}

course_rooms = {
    "COMP 163": "M-Eric 300",
    "MATH 150": "Marteena 201",
    "ENG 101": "Crosby 121",
    "HIS 105": "Crosby 210"
}

monthly_budget = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 125,
    "Transportation": 100
}

study_hours = {
    "Programming": 10,
    "Math": 8,
    "English": 4,
    "History": 3
}

contact_directory = {
    "Mom": "704-555-0199",
    "Roommate": "336-555-7821",
    "Academic Advisor": "336-334-5000"
}

# ===== 6) REQUIRED CALCULATIONS (a–l) =====
# a. Total current credits from credit hours list
total_current_credits = sum(credit_hours)

# b. Cumulative GPA from GPA history list
cumulative_gpa = sum(gpa_history) / len(gpa_history)

# c. Count of completed courses
completed_course_count = len(completed_courses)

# d. Total weekly study hours from study hours dictionary
total_weekly_study_hours = (
    study_hours["Programming"] +
    study_hours["Math"] +
    study_hours["English"] +
    study_hours["History"]
)

# e. Academic load (credits + study hours combined)
academic_load = total_current_credits + total_weekly_study_hours

# f. Monthly budget total from all categories
monthly_budget_total = (
    monthly_budget["Food"] +
    monthly_budget["Entertainment"] +
    monthly_budget["Books"] +
    monthly_budget["Transportation"]
)

# g. Daily food budget (food amount / 30, rounded to 2 decimals)
daily_food_budget = round(monthly_budget["Food"] / 30, 2)

# h. Annual budget projection (monthly total * 12)
annual_budget_projection = monthly_budget_total * 12

# i. Study cost per hour (books budget / total study hours, rounded to 2 decimals)
study_cost_per_hour = round(monthly_budget["Books"] / total_weekly_study_hours, 2)

# j. Total social media followers from platform tuples (tuple indexing only)
total_followers = instagram_info[2] + twitter_info[2]

# k. Skills count comparison (current vs. learning goals)
current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)

# l. Contact directory size analysis
contact_directory_size = len(contact_directory)

# ===== REQUIRED OPERATIONS DEMOS (indexing/key access/sets) =====
first_current_course = current_courses[0]          # list indexing
comp163_credit = course_credits["COMP 163"]        # dictionary key access
instagram_followers = instagram_info[2]            # tuple indexing
all_skills_union = current_skills | skills_to_learn  # set operation

# ===== OUTPUT (professional formatting) =====
print("=== PERSONAL DATA PORTFOLIO ===")
print("Name:", full_name)
print("Email:", student_email)
print("Hometown:", hometown)
print("Graduation:", graduation_semester)
print("Major:", major)

print("\n=== ACADEMICS ===")
print("Current Courses:", current_courses)
print("Completed Courses:", completed_courses)
print("Credit Hours:", credit_hours)
print("GPA History:", gpa_history)
print("Example List Indexing (first course):", first_current_course)

print("\n=== CONTACTS (TUPLES) ===")
print("Emergency Contact:", emergency_contact)
print("Home Address:", home_address)
print("Birthday:", birthday)

print("\n=== SOCIAL MEDIA (TUPLES) ===")
print("Instagram:", instagram_info, "| Followers:", instagram_followers)
print("Twitter:", twitter_info)

print("\n=== SKILLS & INTERESTS (SETS) ===")
print("Current Skills:", current_skills)
print("Skills To Learn:", skills_to_learn)
print("All Skills (Union):", all_skills_union)

print("\n=== ORGANIZATIONAL MAPPING (DICTIONARIES) ===")
print("Course Credits:", course_credits)
print("Course Professors:", course_professors)
print("Course Rooms:", course_rooms)
print("Monthly Budget:", monthly_budget)
print("Study Hours:", study_hours)
print("Contact Directory:", contact_directory)
print("Example Dict Access (COMP 163 credits):", comp163_credit)

print("\n=== REQUIRED CALCULATIONS ===")
print("a) Total current credits:", total_current_credits)
print("b) Cumulative GPA:", round(cumulative_gpa, 2))
print("c) Completed courses count:", completed_course_count)
print("d) Total weekly study hours:", total_weekly_study_hours)
print("e) Academic load (credits + study hours combined):", academic_load)
print("f) Monthly budget total:", monthly_budget_total)
print("g) Daily food budget:", daily_food_budget)
print("h) Annual budget projection:", annual_budget_projection)
print("i) Study cost per hour:", study_cost_per_hour)
print("j) Total social media followers:", total_followers)
print("k) Skills count (current vs. learning goals):", current_skills_count, "vs", skills_to_learn_count)
print("l) Contact directory size:", contact_directory_size)
