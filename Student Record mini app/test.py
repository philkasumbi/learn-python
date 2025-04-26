name = input("Enter your name: ")

subject1 = input("Enter subject 1 name: ")
marks1 = int(input(f"Enter marks for {subject1} /100: ")) 
subject2 = input("Enter subject 2 name: ")
marks2 = int(input(f"Enter marks for {subject2} /100: ")) 
subject3 = input("Enter subject 3 name: ")
marks3 = int(input(f"Enter marks for {subject3} /100: ")) 


Report_card = {}

Report_card["name"] = name
Report_card[subject1] = marks1
Report_card[subject2] = marks2
Report_card[subject3] = marks3

print("""---Report Card---""")

for key,value in Report_card.items():
    print(f"{key}:{value}")

average_marks = float((marks1 + marks2 + marks3)/3)
print(f"Average marks: {average_marks}")
if average_marks >= 80:
    print("Remarks: Excellent")
elif average_marks >= 60:
    print("Remarks: good Job")
else:
    print("Remarks: Need improvement")





