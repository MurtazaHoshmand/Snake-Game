names = ["Ali", "Ahmad", "Murtaza", '']

# for seg_num in range(len(segments) - 1, 0, -1):
#     new_x = segments[seg_num - 1].xcor() 
#     new_y = segments[seg_num - 1].ycor()
#     segments[seg_num].goto(new_x, new_y) 
# 
# segments[0].forward(20)

print(names)

for name in range(len(names) - 1, 0, -1):
    new_name = names[name - 1]
    names[name] = new_name
names[0] = ''
    
print(names)