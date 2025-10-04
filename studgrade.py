def get_grade(marks):
    if marks >= 90:
        return 'A'
    if marks >= 80:
        return 'B'
    if marks >= 70:
        return 'C'
    if marks >= 60: 
        return 'D'  
    return 'Fail'

def main():
    name = input("Enter student's name: ")
    marks = float(input("Enter marks obtained: "))
    grade = get_grade(marks)
    print(f"Student: {name}, Marks: {marks}, Grade: {grade}")   
    print(f"Student: {name}, Marks: {marks}, Grade 1: {grade}")  
    
if __name__ == "__main__":
    main()
    