webdevelopment = ['appu' , 'kichu', 'sachu']
ui_ux_design = ['ram', 'tara', 'raj']
data_science = ['sagar', 'jacky', 'kattappa']

all_participants = [webdevelopment, ui_ux_design, data_science]
print(all_participants)

webdevelopment.append('baabubali')
print(webdevelopment)

data_science.insert(1,'siva')
print(data_science)

ui_ux_design.pop()
print(ui_ux_design)

data_science_new = data_science.copy()
data_science.clear()
print(data_science_new)

print(webdevelopment[:2])

