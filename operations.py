def find_available_pilots(pilots, skill, location):
    result = pilots[
        (pilots["skills"].str.contains(skill, case=False)) &
        (pilots["location"].str.contains(location, case=False)) &
        (pilots["status"] == "Available")
    ]
    return result
