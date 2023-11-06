import getData




token = input("Enter in OAuth Token: ")

sorted_assignments = getData.getUpcomingAssignments(token)
sorted_events = getData.getUpcomingEvents(token)

# for item in sorted_assignments:
#     print(item)

for item in sorted_events:
    print(item)




