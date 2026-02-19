from sheets import load_sheet
from operations import find_available_pilots
from agent import extract_search_details

user_message = input("Ask coordinator: ")

skill, location = extract_search_details(user_message)

print("Skill:", skill)
print("Location:", location)

pilots = load_sheet("pilot_roster")
res = find_available_pilots(pilots, skill, location)

print(res)
