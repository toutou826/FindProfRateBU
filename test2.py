from getClass import getClass

result = getClass("cascs330")

sectionsOutput = f'There are {len(result)} sections for cas330.\n'
teacherSet = set()
for section in result:
    teacherSet.add(section.teacher)
    sectionsOutput += f"Section Name: {section.sectionName}, Teacher Name: {section.teacher}, Time: {section.time} \n"
print(sectionsOutput)
