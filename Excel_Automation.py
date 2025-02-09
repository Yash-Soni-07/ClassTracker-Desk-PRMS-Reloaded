from openpyxl import Workbook, load_workbook
def Update_In_Excel(batch_='', report_list=[], possibility_=1, date_='',total=100):
    global hw,test
    #Globalizing some variables
    global yes_HW_given, yes_T_taken, call_again, yes_num,Temporary_Storage, Test_Score, yes_num
    #Loading Excel File
    wb = load_workbook(f"C:/Class/{batch_}.xlsx")#Loading the workbook
    ws = wb.create_sheet(f"{date_}")
    #---Heading---#
    if possibility_==1:
        ws.append(['Name','Attendance'])
        for report in report_list:
            ws.append([report[0],1 if report[1]=='Present' else 0])

    elif possibility_==2:
        ws.append(['Name','Attendance','Homework', 'Test Score'])
        for report in report_list:
            if(report[2]=='Complete'):
                hw=1
            elif(report[2]=='Incomplete'):
                hw=0.5
            elif(report[2]=='---'):
                hw=0
            else:
                hw=0
            if (report[3] == '---'):
                test = 0
            elif str(type(eval(report[3]))) == "<class 'int'>" or str(type(eval(report[3]))) == "<class 'float'>":
                test = round((eval(report[3])/total)*100,2)
            else:
                test=report[3]
            ws.append([report[0], 1 if report[1] == 'Present' else 0,hw,test])
    elif possibility_==3:
        ws.append(['Name','Attendance','Homework'])
        for report in report_list:
            if (report[2] == 'Complete'):
                hw = 1
            elif (report[2] == 'Incomplete'):
                hw = 0.5
            elif (report[2] == '---'):
                hw = 0
            else:
                hw = 0
            ws.append([report[0], 1 if report[1] == 'Present' else 0,hw])
    elif possibility_==4:
        ws.append(['Name', 'Attendance','Test Score'])
        for report in report_list:
            if (report[2] == '---'):
                test = 0
            elif str(type(eval(report[2]))) == "<class 'int'>" or str(type(eval(report[2]))) == "<class 'float'>":
                test = round((eval(report[2])/total)*100, 2)
            else:
                test = report[2]
            ws.append([report[0], 1 if report[1] == 'Present' else 0,test])



    wb.save(f"C:/Class/{batch_}.xlsx")
print([type(eval('100'))])
# print(type(eval('13.5')))
# print(type(eval('ns')))