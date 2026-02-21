# Student Grade Calculator

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A", "Excellent Work! 🌟 Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Nice effort! Try to improve next time! 💪"
    else:
        return "F", "Don't worry! Practice makes perfect! 📚"


# Take student name
name = input("Enter student name: ")

# Validate marks using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))

        if marks >= 0 and marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100. Try again!")

    except:
        print("Invalid input! Please enter numbers only.")

# Call function
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", name.upper())
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)