import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta


# Generate random student data
def generate_random_data():
    students = [
        "Alice Johnson", "Bob Smith", "Charlie Brown", "David Williams", "Emma Davis",
        "Frank Miller", "Grace Wilson", "Hannah Moore", "Isaac Taylor", "Jack Anderson"
    ]

    start_date = datetime(2024, 12, 1)
    end_date = datetime(2025, 1, 31)
    days = (end_date - start_date).days + 1

    with pd.ExcelWriter("student.xlsx") as writer:
        for i in range(days):
            date = start_date + timedelta(days=i)
            sheet_name = date.strftime("%Y_%B_%d")

            data_format = random.choice([
                ['Name', 'Attendance', 'HW Status', 'Test Score'],
                ['Name', 'Attendance'],
                ['Name', 'Attendance', 'HW Status'],
                ['Name', 'Attendance', 'Test Score']
            ])

            data = []
            for student in students:
                row = {"Name": student}
                if 'Attendance' in data_format:
                    row['Attendance'] = random.choice([0, 1])  # 0 for absent, 1 for present
                if 'HW Status' in data_format:
                    row['HW Status'] = random.choice([0, 0.5, 1])  # 0=Not Done, 0.5=Incomplete, 1=Completed
                if 'Test Score' in data_format:
                    row['Test Score'] = random.randint(50, 100)
                data.append(row)

            df = pd.DataFrame(data, columns=data_format)
            df.to_excel(writer, sheet_name=sheet_name, index=False)


# Generate and save random data
generate_random_data()
print("Excel file 'student.xlsx' created successfully!")
