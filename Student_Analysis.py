import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load Excel file
# file_path = "student.xlsx"
# def set_file_path_for(batch=''):
#     global xls
#     xls = pd.ExcelFile(f"C:\\Class\\{batch}.xlsx")


def get_date_range():
    """Asks user for a start and end date and returns them."""
    start_date = input("Enter start date (YYYY_MM_DD): ")
    end_date = input("Enter end date (YYYY_MM_DD): ")
    return start_date, end_date


# Process the Excel file
def process_data(batch='',start_date='', end_date=''):
    student_data = {}
    xls = pd.ExcelFile(f"C:\\Class\\{batch}.xlsx")
    for sheet_name in xls.sheet_names:
        if start_date <= sheet_name <= end_date:
            df = pd.read_excel(xls, sheet_name)
            for _, row in df.iterrows():
                name = row['Name']
                if name not in student_data:
                    student_data[name] = {'Attendance': [], 'HW Status': [], 'Test Score': [], 'Dates': []}
                student_data[name]['Attendance'].append(row.get('Attendance', 0))
                student_data[name]['HW Status'].append(row.get('HW Status') if 'HW Status' in row else None)
                student_data[name]['Test Score'].append(row.get('Test Score') if 'Test Score' in row else None)
                student_data[name]['Dates'].append(sheet_name)
    return student_data


# Plot batch analysis
def plot_batch_analysis(student_data):
    students = list(student_data.keys())
    attendance = [sum(data['Attendance']) / len(data['Attendance']) * 100 for data in student_data.values()]
    hw_status = [sum(filter(None, data['HW Status'])) / len(list(filter(None, data['HW Status']))) * 100 if any(
        data['HW Status']) else 0 for data in student_data.values()]
    marks = [sum(filter(None, data['Test Score'])) / len(list(filter(None, data['Test Score']))) if any(
        data['Test Score']) else 0 for data in student_data.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(students, attendance, color='blue', alpha=0.7, label='Attendance %')
    plt.title('Batch Attendance Analysis')
    plt.ylabel('Attendance %')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(students, hw_status, color='orange', alpha=0.7, label='HW Completion %')
    plt.title('Batch HW Completion Analysis')
    plt.ylabel('HW Completion %')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(students, marks, color='green', alpha=0.7, label='Marks Average')
    plt.title('Batch Marks Analysis')
    plt.ylabel('Marks (%)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()


# Plot individual student analysis
def plot_student_analysis(student_name, student_data):
    if student_name not in student_data:
        print("Student not found!")
        return

    data = student_data[student_name]
    dates = data['Dates']
    attendance = data['Attendance']
    hw_status = [hw if hw is not None else None for hw in data['HW Status']]
    marks = [score if score is not None else None for score in data['Test Score']]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, attendance, marker='o', linestyle='-', color='blue', label='Attendance')
    plt.title(f'{student_name} - Attendance')
    plt.ylabel('Attendance (1=Present, 0=Absent)')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()

    if any(hw_status):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, [hw if hw is not None else float('nan') for hw in hw_status], marker='s', linestyle='-',
                 color='orange', label='HW Completion')
        plt.title(f'{student_name} - HW Completion')
        plt.ylabel('HW Completion (1=Done, 0=Not Done, 0.5=Incomplete)')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()

    if any(marks):
        plt.figure(figsize=(10, 5))
        plt.plot(dates, [score if score is not None else float('nan') for score in marks], marker='d', linestyle='-',
                 color='green', label='Marks')
        plt.title(f'{student_name} - Marks Analysis')
        plt.ylabel('Marks (%)')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()


# Get user inputs
#  start_date, end_date = get_date_range()

# Process data
# student_data = process_data(start_date, end_date)

# Plot batch analysis
# plot_batch_analysis(student_data)

# Plot individual student analysis
# student_name = input("Enter student name for detailed analysis: ")
# plot_student_analysis(student_name, student_data)
