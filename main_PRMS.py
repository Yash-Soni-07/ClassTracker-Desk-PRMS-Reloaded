from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Profile
chrome_profile_path = "C:\\User Data"

#serv = Service(executable_path="chromedriver.exe")

# Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")

# Initialize the Chrome browser with the configured options
driver = webdriver.Chrome(options=chrome_options)
whats_url = "https://web.whatsapp.com"

def send_whatsapp_messages(messages=["Test Message"], phone_nums=[1235512345]):
    global i
    for i in range(0, len(phone_nums)):
        driver.get(whats_url+f"/send?phone={phone_nums[i]}")

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "_ak1l")))
        entry_field = driver.find_element(By.CLASS_NAME, "_ak1l")

        message = messages[i].split('\n')
        print(message)
        for msg in message:
            entry_field.send_keys(msg)
            entry_field.send_keys(Keys.SHIFT+Keys.ENTER)
        entry_field.send_keys(Keys.ENTER)
        time.sleep(2)

def send_whatsapp_message(body="",num=""):
    driver.get(whats_url+f"/send?phone={num}")

    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "_ak1l")))
    entry_field = driver.find_element(By.CLASS_NAME, "_ak1l")
    message = body.split('\n')
    for msg in message:
        entry_field.send_keys(msg)
        entry_field.send_keys(Keys.SHIFT+Keys.ENTER)
    entry_field.send_keys(Keys.ENTER)
    time.sleep(2)

###########################################################################################



import tkinter as tk
from tkinter import ttk
from datetime import date, datetime
from tkinter import messagebox
import time

import Excel_Automation

''' Locally Modified Packages'''
import DateConfig
import Name_List_Selection
#import Selenium_1

print(type(13))
a=14.5
if str(type(14.5))=="<class 'float'>":
    print("yes float value")

# main window
window = tk.Tk()
window.title('Progress Report Management System')
window.geometry('800x550')
#window.minsize(800, 600)

''' ---------- FUNCTIONS ---------- '''

def att_radio1_func():
    global absent
    if attendance_var.get()=='Present':
        attendance_entry.grid_forget()
        att_entry_var.set(value='Null')
        if absent==1:
            if ask_hw_radio_var.get()=='yes_hw_given':
                reset_progress_update_subframe_3()
            if ask_test_radio_var.get()=='yes_test_taken':
                reset_progress_update_subframe_4()
            absent=0

absent=0
def att_radio2_func():
    global absent
    if attendance_var.get()=='Absent':
        attendance_entry.grid_forget()
        att_entry_var.set(value='Null')

        if ask_hw_radio_var.get()=='yes_hw_given':
            hw_status_radio1.grid_forget()
            hw_status_radio2.grid_forget()
            hw_status_radio3.grid(column=1, row=0, rowspan=3, sticky='nsew')
            hw_status_entry.grid(column=2, row=0, rowspan=3, sticky='ew')
            hw_status_entry_var.set(value='---')
            hw_status_var.set(value='hw_status_other')

        if ask_test_radio_var.get()=='yes_test_taken':
            test_score_entry.grid_forget()
            test_out_of_label.grid_forget()
            test_other_radio.grid(column=1, row=0, rowspan=2, sticky='nsew')
            test_other_entry.grid(column=2, row=0, rowspan=2, sticky='ew')
            test_other_entry_var.set(value='---')
            test_other_radio_var.set(value='test_score_other')

        absent=1
def att_radio3_func():
    global absent
    attendance_entry.grid(column=2, row=2, sticky='we')
    if absent == 1:
        if ask_hw_radio_var.get() == 'yes_hw_given':
            reset_progress_update_subframe_3()
        if ask_test_radio_var.get() == 'yes_test_taken':
            reset_progress_update_subframe_4()
        absent = 0

def hw_status_radio_1_func():
    if hw_status_var.get()=='Complete':
        hw_status_entry.grid_forget()
        hw_status_entry_var.set(value='Null')
def hw_status_radio_2_func():
    if hw_status_var.get()=='Incomplete':
        hw_status_entry.grid_forget()
        hw_status_entry_var.set(value='Null')
def hw_status_radio_3_func():
    global absent
    if absent==0:
        hw_status_entry.grid(column=2, row=2, sticky='ew')

def test_other_radio_func():
    global absent
    if absent==0:
        test_other_entry.grid(column=2, row=1, sticky='ew')
        test_score_var.set(value='Enter marks here')

def progress_update_frame_grid_configure():
    if ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
        progress_update_frame.columnconfigure(0, weight=1, uniform='yes_hw_yes_test')
        progress_update_frame.rowconfigure(0, weight=1, uniform='yes_hw_yes_test')
        progress_update_frame.rowconfigure((1, 2, 3), weight=2, uniform='yes_hw_yes_test')
        progress_update_frame.rowconfigure(4, weight=1, uniform='yes_hw_yes_test')
    elif ask_hw_radio_var.get()=='no_hw_given' and ask_test_radio_var.get()=='no_test_taken':
        progress_update_frame.columnconfigure(0, weight=1, uniform='no_hw_no_test')
        progress_update_frame.rowconfigure(0, weight=1, uniform='no_hw_no_test')
        progress_update_frame.rowconfigure(1, weight=6, uniform='no_hw_no_test')
        progress_update_frame.rowconfigure(2, weight=1, uniform='no_hw_no_test')
    elif ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='no_test_taken':
        progress_update_frame.columnconfigure(0, weight=1, uniform='yes_hw_no_test')
        progress_update_frame.rowconfigure(0, weight=1, uniform='yes_hw_no_test')
        progress_update_frame.rowconfigure((1,2), weight=4, uniform='yes_hw_no_test')
        progress_update_frame.rowconfigure(3, weight=1, uniform='yes_hw_no_test')
    elif ask_hw_radio_var.get()=='no_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
        progress_update_frame.columnconfigure(0, weight=1, uniform='no_hw_yes_test')
        progress_update_frame.rowconfigure(0, weight=1, uniform='no_hw_yes_test')
        progress_update_frame.rowconfigure((1, 2), weight=4, uniform='no_hw_yes_test')
        progress_update_frame.rowconfigure(3, weight=1, uniform='no_hw_yes_test')

def set_progress_update_subframe_1(c, r, st):
    progress_update_subframe_1.grid(column=c, row=r, sticky=st)

    #progress_update_subframe_1.grid(column=0, row=0, sticky='nsew')
    progress_update_subframe_1.columnconfigure(0, weight=1, uniform='sub_frame1')
    progress_update_subframe_1.rowconfigure(0, weight=1, uniform='sub_frame1')

    name_label.grid(column=0, row=0, sticky='ns')
def set_progress_update_subframe_2(c, r, st):
    progress_update_subframe_2.grid(column=c, row=r, sticky=st)

    progress_update_subframe_2.columnconfigure((0, 1, 2), weight=1, uniform='abcd2')
    progress_update_subframe_2.rowconfigure((0, 1, 2), weight=1, uniform='abcd2')

    attendance_label.grid(column=0, row=0, rowspan=3, sticky='ew')

    attendance_radio1.grid(column=1, row=0, sticky='nsew')
    attendance_radio2.grid(column=1, row=1, sticky='nsew')
    attendance_radio3.grid(column=1, row=2, sticky='nsew')
def set_progress_update_subframe_3(c, r, st):
    progress_update_subframe_3.grid(column=c, row=r, sticky=st)

    progress_update_subframe_3.columnconfigure((0, 1, 2), weight=1, uniform='abcd3')
    progress_update_subframe_3.rowconfigure((0, 1, 2), weight=1, uniform='abcd3')

    hw_status_label.grid(column=0, row=0, rowspan=3, sticky='nsew')

    hw_status_radio1.grid(column=1, row=0, sticky='nsew')
    hw_status_radio2.grid(column=1, row=1, sticky='nsew')
    hw_status_radio3.grid(column=1, row=2, sticky='nsew')
def set_progress_update_subframe_4(c, r, st):
    progress_update_subframe_4.grid(column=c, row=r, sticky=st)

    progress_update_subframe_4.columnconfigure((0, 1, 2), weight=1, uniform='abcd4')
    progress_update_subframe_4.rowconfigure((0, 1), weight=1, uniform='abcd4')

    test_score_label.grid(column=0, row=0, rowspan=2, sticky='nsew')
    test_score_entry.grid(column=1, row=0, sticky='ew')
    test_out_of_label.grid(column=2, row=0, sticky='nsew')
    test_other_radio.grid(column=1, row=1, sticky='nsew')

    test_out_of_label_var.set(value=f"out of {str(marks_entry_var.get())}")
def set_progress_update_subframe_5(c, r, st):
    progress_update_subframe_5.grid(column=c, row=r, sticky=st)

    progress_update_subframe_5.columnconfigure((0, 1, 2), weight=1, uniform='abcd5')
    progress_update_subframe_5.rowconfigure(0, weight=1, uniform='abcd5')

    save_n_continue.grid(column=2, row=0, sticky='nsew')

def reset_progress_update_subframe_1(clear=False):
    print("RESET PROGRESS UPDATE SUBFRAME 1")
    '''Resetting widgets variable'''
    name_var.set("Report of 'Student Name'")
    '''Resetting widgets'''
    name_label.grid(column=0, row=0, sticky='ns')
    '''Clearing widgets'''
    if clear==True:
        name_label.grid_forget()

def reset_progress_update_subframe_2(clear=False):
    global absent
    print("RESET PROGRESS UPDATE SUBFRAME 2")
    '''Resetting widgets variable'''
    absent=0
    attendance_var.set(value="Present")
    att_entry_var.set(value="Null")
    '''Resetting widgets'''
    attendance_radio1.grid(column=1, row=0, sticky='nsew')
    attendance_radio2.grid(column=1, row=1, sticky='nsew')
    attendance_radio3.grid(column=1, row=2, sticky='nsew')
    '''Clearing widgets'''
    if clear==True:
        attendance_label.grid_forget()

        attendance_radio1.grid_forget()
        attendance_radio2.grid_forget()
        attendance_radio3.grid_forget()

    attendance_entry.grid_forget()


def reset_progress_update_subframe_3(clear=False):
    print("RESET PROGRESS UPDATE SUBFRAME 3")
    '''Resetting widgets variable'''
    hw_status_var.set(value='Complete')
    hw_status_entry_var.set(value='Null')
    '''Resetting widgets'''
    hw_status_radio1.grid(column=1, row=0, sticky='nsew')
    hw_status_radio2.grid(column=1, row=1, sticky='nsew')
    hw_status_radio3.grid(column=1, row=2, sticky='nsew')
    '''Clearing widgets'''
    if clear==True:
        hw_status_label.grid_forget()

        hw_status_radio1.grid_forget()
        hw_status_radio2.grid_forget()
        hw_status_radio3.grid_forget()

    hw_status_entry.grid_forget()

def reset_progress_update_subframe_4(clear=False):
    print("RESET PROGRESS UPDATE SUBFRAME 4")
    '''Resetting widgets variable'''
    test_score_var.set(value='Enter marks here')
    test_other_radio_var.set(value='Null')
    test_other_entry_var.set(value='Null')
    test_out_of_label_var.set(value=f"out of {str(marks_entry_var.get())}")
    '''Resetting widgets'''
    test_score_entry.grid(column=1, row=0, sticky='ew')
    test_out_of_label.grid(column=2, row=0, sticky='nsew')
    test_other_radio.grid(column=1, row=1, sticky='nsew')
    '''Clearing widgets'''
    if clear==True:
        test_score_label.grid_forget()

        test_score_entry.grid_forget()
        test_out_of_label.grid_forget()
        test_other_radio.grid_forget()
    test_other_entry.grid_forget()

def reset_progress_update_subframe_5(clear=False):
    print("RESET PROGRESS UPDATE SUBFRAME 5")
    global progress_bar_int_var, progress_bar_for_reports, save_n_conti_press
    save_n_continue.configure(text='Save & Continue')
    '''Resetting '''
    if save_n_conti_press>0:
        progress_bar_int_var.set(value=0)
        print("PROGRESS VAR RESET")
    if clear==True:
        save_n_continue.grid_forget()
        if save_n_conti_press>0:
            back_button.grid_forget()
            progress_bar_for_reports.grid_forget()
            print("PROGRESS & BACK BUTTON GRID FORGET")

'''Possible Combinations for the Session'''
possibility=0
'''Possiblity 1'''
def no_hw_no_test():
    global possibility
    possibility = 1
    print("NO H.W. NO TEST")
    '''Subframe_1 layout'''
    set_progress_update_subframe_1(c=0, r=0, st='nsew')

    '''Subframe_2 layout'''
    set_progress_update_subframe_2(c=0, r=1, st='nsew')

    '''Subframe_5 Layout'''
    set_progress_update_subframe_5(c=0, r=2, st='nsew')
def undo_no_hw_no_test():
    print("UNDO: NO H.W. NO TEST")
    '''Resetting subframe_1'''
    reset_progress_update_subframe_1()

    '''Resetting subframe_2'''
    reset_progress_update_subframe_2()

    '''Resetting subframe_5'''
    reset_progress_update_subframe_5()

'''Possiblity 2'''
def yes_hw_yes_test():
    global possibility
    possibility = 2
    print("YES H.W. YES TEST")
    '''Subframe_1 Layout'''
    set_progress_update_subframe_1(c=0, r=0, st='nsew')

    '''Subframe_2 Layout'''
    set_progress_update_subframe_2(c=0, r=1, st='nsew')

    '''Subframe_3 Layout'''
    set_progress_update_subframe_3(c=0, r=2, st='nsew')

    '''Subframe_4 Layout'''
    set_progress_update_subframe_4(c=0, r=3, st='nsew')

    '''Subframe_5 Layout'''
    set_progress_update_subframe_5(c=0, r=4, st='nsew')

'''Possibility 3'''
def yes_hw_no_test():
    global possibility
    possibility = 3
    print("YES H.W. NO TEST")
    '''Subframe_1 Layout'''
    set_progress_update_subframe_1(c=0, r=0, st='nsew')

    '''Subframe_2 Layout'''
    set_progress_update_subframe_2(c=0, r=1, st='nsew')

    '''Subframe_3 Layout'''
    set_progress_update_subframe_3(c=0, r=2, st='nsew')

    '''Subframe_5 Layout'''
    set_progress_update_subframe_5(c=0, r=3, st='nsew')

'''Possibility 4'''
def no_hw_yes_test():
    global possibility
    possibility = 4
    print("NO H.W. YES TEST")
    '''Subframe_1 Layout'''
    set_progress_update_subframe_1(c=0, r=0, st='nsew')

    '''Subframe_2 Layout'''
    set_progress_update_subframe_2(c=0, r=1, st='nsew')

    '''Subframe_4 Layout'''
    set_progress_update_subframe_4(c=0, r=2, st='nsew')

    '''Subframe_5 Layout'''
    set_progress_update_subframe_5(c=0, r=3, st='nsew')

def retrieve_realtime_student_report():
    global name_list, possibility, att, hw, test_score, report, save_n_conti_press, name_index
    if possibility in [1, 2, 3, 4]:
        if attendance_var.get() in ['Present', 'Absent']:
            att = attendance_var.get()
        elif attendance_var.get()=='attendance_other':
            att = att_entry_var.get()
    if possibility==2:
        if hw_status_var.get() in ['Complete', 'Incomplete']:
            hw=hw_status_var.get()
        elif hw_status_var.get()=='hw_status_other':
            hw=hw_status_entry_var.get()
        if test_other_radio_var.get()=='Null':
            test_score=str(test_score_var.get())
        elif test_other_radio_var.get()=='test_score_other':
            test_score=test_other_entry_var.get()
    if possibility==3:
        if hw_status_var.get() in ['Complete', 'Incomplete']:
            hw=hw_status_var.get()
        elif hw_status_var.get()=='hw_status_other':
            hw=hw_status_entry_var.get()
    if possibility==4:
        if test_other_radio_var.get()=='Null':
            test_score=str(test_score_var.get())
        elif test_other_radio_var.get()=='test_score_other':
            test_score=test_other_entry_var.get()

def show_previous_reports():
    global NAME, ATT, HW, TEST, possibility
    if possibility==1:
        '''NAME'''
        name_var.set(value=f"Report of {NAME}")
        '''ATTENDANCE'''
        attendance_var.set(value=ATT)
        if ATT not in ['Present', 'Absent']:
            attendance_var.set(value='attendance_other')
            att_entry_var.set(value=ATT)
            attendance_entry.grid(column=2, row=2, sticky='we')
    elif possibility==2:
        '''NAME'''
        name_var.set(value=f"Report of {NAME}")
        '''ATTENDANCE'''
        if ATT not in ['Present', 'Absent']:
            attendance_var.set(value='attendance_other')
            att_entry_var.set(value=ATT)
            attendance_entry.grid(column=2, row=2, sticky='we')
        else:
            attendance_var.set(value=ATT)
        '''HOMEWORK'''
        if HW not in ['Complete', 'Incomplete']:
            hw_status_var.set(value='hw_status_other')
            hw_status_entry_var.set(value=HW)
            hw_status_entry.grid(column=2, row=2, sticky='ew')
        else:
            hw_status_var.set(value=HW)
        '''TEST'''
        if str(TEST).isdigit() or type(TEST)=="<class 'float'>":
            test_score_var.set(value=TEST)
        else:
            test_other_radio_var.set(value='test_score_other')
            test_other_entry_var.set(value=TEST)
            test_other_entry.grid(column=2, row=1, sticky='we')
    elif possibility==3:
        '''NAME'''
        name_var.set(value=f"Report of {NAME}")
        '''ATTENDANCE'''
        if ATT not in ['Present', 'Absent']:
            attendance_var.set(value='attendance_other')
            att_entry_var.set(value=ATT)
            attendance_entry.grid(column=2, row=2, sticky='we')
        else:
            attendance_var.set(value=ATT)
        '''HOMEWORK'''
        if HW not in ['Complete', 'Incomplete']:
            hw_status_var.set(value='hw_status_other')
            hw_entry_var.set(value=HW)
            hw_status_entry.grid(column=2, row=2, sticky='ew')
        else:
            hw_status_var.set(value=HW)
    elif possibility==4:
        '''NAME'''
        name_var.set(value=f"Report of {NAME}")
        '''ATTENDANCE'''
        if ATT not in ['Present', 'Absent']:
            attendance_var.set(value='attendance_other')
            att_entry_var.set(value=ATT)
            attendance_entry.grid(column=2, row=2, sticky='we')
        else:
            attendance_var.set(value=ATT)
        '''TEST'''
        if str(TEST).isdigit() or type(TEST) == "<class 'float'>":
            test_score_var.set(value=TEST)
        else:
            test_other_radio_var.set(value='test_score_other')
            test_other_entry_var.set(value=TEST)
            test_other_entry.grid(column=2, row=1, sticky='we')

it_is_num=False
def check_isnum(num=''):
    global it_is_num
    num_new = num.replace('.', '1')
    if num_new.isdigit():
        it_is_num=True
    else:
        it_is_num=False

reports_sent=False
def send_reports_in_whatsapp():
    global reports, absent_students, student_absent,number_list, possibility, report_sender_progress_bar_var, reports_sent, it_is_num
    j=0
    absent_students=[]
    msgs=[]
    student_absent=False
    if possibility==1:
        if reports_sent==False:
            line1 = line1_entry_var.get()
            line2 = line2_entry_var.get()
            for report in reports:
                if report[1]=='Absent':
                    absent_students.append(report[0])
                    student_absent=True
                Name = report[0]
                Att = report[1]
                body = f"{line1} {Name}\n\n{line2} {Att}"
                msgs.append(body)
                j += 1
                #report_sender_progress_bar_var.set(value=j)
                #time.sleep(1)
            reports_sent=True
    elif possibility==2:
        line1 = line1_entry_var.get()
        line2 = line2_entry_var.get()
        line3 = line3_entry_var.get()
        line4 = line4_entry_var.get()
        for report in reports:
            if report[1]=='Absent':
                absent_students.append(report[0])
                student_absent=True
            Name = report[0]
            Att = report[1]
            Hw = report[2]
            check_isnum(num=report[3])
            if it_is_num==True:
                Test_status = f"{report[3]}/{str(marks_entry_var.get())}"
                it_is_num=False
            else:
                Test_status = report[3]
            body = f"{line1} {Name}\n\n{line2} {Att}\n\n{line3} {Hw}\n\n{line4} {Test_status}"
            msgs.append(body)
            #send_whatsapp_message(msg=body)
            j += 1
            #report_sender_progress_bar_var.set(value=j)
            #time.sleep(1)
    elif possibility==3:
        line1 = line1_entry_var.get()
        line2 = line2_entry_var.get()
        line3 = line3_entry_var.get()
        for report in reports:
            if report[1]=='Absent':
                absent_students.append(report[0])
                student_absent=True
            Name = report[0]
            Att = report[1]
            Hw = report[2]
            body = f"{line1} {Name}\n\n{line2} {Att}\n\n{line3} {Hw}"
            msgs.append(body)
            #send_whatsapp_message(msg=body)
            j += 1
            #report_sender_progress_bar_var.set(value=j)
            #time.sleep(1)
    elif possibility==4:
        line1 = line1_entry_var.get()
        line2 = line2_entry_var.get()
        line3 = line4_entry_var.get()
        for report in reports:
            if report[1]=='Absent':
                absent_students.append(report[0])
                student_absent=True
            Name = report[0]
            Att = report[1]
            check_isnum(num=report[2])
            if it_is_num==True:
                Test_status = f"{report[2]}/{str(marks_entry_var.get())}"
                it_is_num=False
            else:
                Test_status = report[2]
            body = f"{line1} {Name}\n\n{line2} {Att}\n\n{line3} {Test_status}"
            msgs.append(body)
            #send_whatsapp_message(msg=body)
            j += 1
            #report_sender_progress_bar_var.set(value=j)
            #time.sleep(1)
    send_whatsapp_messages(messages=msgs, phone_nums=number_list)
    if student_absent==True:
        body="*Absent Students in Today's Session :*"
        i=1
        for student in absent_students:
            body+=f"\n{student}"
            i+=1
        body+=f"\n*Content missed by these students :* {session_content_var.get()}"
        send_whatsapp_message(body=f"{body}",num="7874015674")
        #send_whatsapp_message(msg=body)
        j+=1

    if j==len(name_list) or j==len(name_list)+1:
        msg = messagebox.showinfo("INFO", "All the Reports are Successfully sent!")
        reports_sent=True


reports=[]
name_index=1
report_index=0
save_n_conti_press=0
def save_and_continue():
    global report, reports, name_index, report_index, name_list,number_list, save_n_conti_press, att, hw, test_score,\
        back_press, progress_bar_max_value, progress_bar_int_var, progress_bar_for_reports
    report=[]

    name_list,number_list = Name_List_Selection.select_for(batch=batch_radio_var.get())
    num_of_reports = len(name_list)

    if save_n_conti_press==0:
        progress_bar_int_var = tk.IntVar(value=0)
        progress_bar_max_value = num_of_reports
        progress_bar_for_reports = ttk.Progressbar(progress_update_subframe_5,
                                                   variable=progress_bar_int_var,
                                                   maximum=progress_bar_max_value,
                                                   orient='horizontal',)
        progress_bar_for_reports.grid(column=1, row=0, sticky='ew')

    print(name_list)
    print("No.of Reports:",num_of_reports)

    if report_index<num_of_reports:
        try:
            name_var.set(f"Report of {name_list[name_index]}")
        except:
            messagebox.showinfo('Info', "All Reports are Updated")

        retrieve_realtime_student_report()
        name = name_list[save_n_conti_press]

        if possibility==1:
            report = [name, att]
            if report_index!=num_of_reports-1:
                reset_progress_update_subframe_2()

        elif possibility==2:
            report = [name, att, hw, test_score]
            if report_index!=num_of_reports-1:
                reset_progress_update_subframe_2()
                reset_progress_update_subframe_3()
                reset_progress_update_subframe_4()

        elif possibility==3:
            report = [name, att, hw]
            if report_index!=num_of_reports-1:
                reset_progress_update_subframe_2()
                reset_progress_update_subframe_3()

        elif possibility==4:
            report = [name, att, test_score]
            if report_index!=num_of_reports-1:
                reset_progress_update_subframe_2()
                reset_progress_update_subframe_4()

        reports.append(report)
        name_index+=1
        report_index+=1
        save_n_conti_press+=1
        progress_bar_int_var.set(value=save_n_conti_press)
    else:
        messagebox.showinfo('INFO', 'All reports updated')
    '''elif save_n_conti_press==len(name_list):
        send_reports_in_whatsapp()==========================================================='''

    print(reports)

    print("len(reports): ",len(reports))
    print("save_n_conti_press = ", save_n_conti_press)
    print("back_press = ", back_press)
    print("name_index = ", name_index)
    print("report_index = ", report_index)

    if save_n_conti_press==1:
        back_button.grid(column=0, row=0, sticky='nsew')

back_press = 0
def back_button_func():
    pass
    '''
    global report, reports, name_index, report_index, save_n_conti_press, back_press, possibility, NAME, ATT, HW, TEST, progress_bar_int_var
    if save_n_conti_press==1:
        Report = reports[0]
        Name = Report[0]
        name_var.set(value=f'Report of {Name}')

        back_button.grid_forget()
        save_n_conti_press-=1
        name_index-=1
        report_index-=1

    elif save_n_conti_press>1:
        i=save_n_conti_press-1
        Report = reports[i]
        if possibility==1:
            NAME = Report[0]
            ATT = Report[1]
        if possibility==2:
            NAME = Report[0]
            ATT = Report[1]
            HW = Report[2]
            TEST = Report[3]
        if possibility==3:
            NAME = Report[0]
            ATT = Report[1]
            HW = Report[2]
        if possibility==4:
            NAME = Report[0]
            ATT = Report[1]
            TEST = Report[2]
        show_previous_reports()
        save_n_conti_press-=1
        name_index-=1
        report_index-=1
    progress_bar_int_var.set(value=save_n_conti_press)
    print('back_press = ', back_press)
    print('save_n_conti_press = ', save_n_conti_press)
    '''

def Show_empty_Reports():

    print(ask_hw_radio_var.get())
    print(ask_test_radio_var.get())

    '''Configuring Grid layout for progress_update_frame'''
    progress_update_frame_grid_configure()

    '''Configuring widgets in progress_update_frame'''
    if ask_hw_radio_var.get()=='no_hw_given' and ask_test_radio_var.get()=='no_test_taken':
        no_hw_no_test()
    elif ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
        yes_hw_yes_test()
    elif ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='no_test_taken':
        yes_hw_no_test()
    elif ask_hw_radio_var.get()=='no_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
        no_hw_yes_test()

def reset_session_details_frame():
    if ask_hw_radio_var.get() == 'yes_hw_given':
        hw_label.grid_forget()
        hw_entry.grid_forget()
    if ask_test_radio_var.get() == 'yes_test_taken':
        test_marks_label.grid_forget()
        test_marks_entry.grid_forget()
        test_topic_label.grid_forget()
        test_topic_entry.grid_forget()
    ask_hw_radio_var.set(value='NULL')
    hw_entry_var.set(value='Enter H.W. Details')

    ask_test_radio_var.set(value='NULL')
    marks_entry_var.set(value=15)
    test_entry_var.set(value='Enter Test Topic')

    session_content_var.set(value='Enter Session Content')

def reset_progress_update_frame():
    global name_index, reports, save_n_conti_press, possibility, report_index, back_press
    if possibility==1:
        reset_progress_update_subframe_1(clear=True)
        reset_progress_update_subframe_2(clear=True)
        reset_progress_update_subframe_5(clear=True)
    elif possibility==2:
        reset_progress_update_subframe_1(clear=True)
        reset_progress_update_subframe_2(clear=True)
        reset_progress_update_subframe_3(clear=True)
        reset_progress_update_subframe_4(clear=True)
        reset_progress_update_subframe_5(clear=True)
    elif possibility==3:
        reset_progress_update_subframe_1(clear=True)
        reset_progress_update_subframe_2(clear=True)
        reset_progress_update_subframe_3(clear=True)
        reset_progress_update_subframe_5(clear=True)
    elif possibility==4:
        reset_progress_update_subframe_1(clear=True)
        reset_progress_update_subframe_2(clear=True)
        reset_progress_update_subframe_4(clear=True)
        reset_progress_update_subframe_5(clear=True)
    name_index=1
    report_index=0
    save_n_conti_press=0
    back_press=0
    reports=[]

def set_report_sender_frame_grid():
    global possibility
    report_sender_frame.columnconfigure(0, weight=1, uniform="RSF")
    report_sender_frame.columnconfigure(1, weight=2, uniform="RSF")
    report_sender_frame.columnconfigure(2, weight=1, uniform="RSF")
    if possibility==1:
        report_sender_frame.rowconfigure(0, weight=1, uniform="RSF")
        report_sender_frame.rowconfigure((1, 2), weight=2, uniform="RSF")
        report_sender_frame.rowconfigure(3, weight=1, uniform="RSF")
    elif possibility==2:
        report_sender_frame.rowconfigure(0, weight=1, uniform="RSF")
        report_sender_frame.rowconfigure((1, 2, 3, 4), weight=2, uniform="RSF")
        report_sender_frame.rowconfigure(5, weight=1, uniform="RSF")
    elif possibility==3 or possibility==4:
        report_sender_frame.rowconfigure(0, weight=1, uniform="RSF")
        report_sender_frame.rowconfigure((1, 2, 3), weight=2, uniform="RSF")
        report_sender_frame.rowconfigure(4, weight=1, uniform="RSF")

def set_report_sender_frame_widgets():
    global possibility
    '''Setting Heading'''
    report_sender_frame_head_label.grid(column=0, row=0, columnspan=3, sticky='ns')
    '''Setting Line 1 for the Message'''
    line1_label.grid(column=0, row=1, sticky='ns')
    line1_entry.grid(column=1, row=1, sticky='ew')
    line1_name_label.grid(column=2, row=1, sticky='ns')
    '''Setting Line 2 for the Message'''
    line2_label.grid(column=0, row=2, sticky='ns')
    line2_entry.grid(column=1, row=2, sticky='ew')
    line2_att_label.grid(column=2, row=2, sticky='ns')
    if possibility==1:
        '''Setting Report Sender Button'''
        send_reports_button.grid(column=1, row=3)
    elif possibility==2:
        '''Setting Line 3 for the Message'''
        line3_label.grid(column=0, row=3, sticky='ns')
        line3_entry.grid(column=1, row=3, sticky='ew')
        line3_hw_label.grid(column=2, row=3, sticky='ns')
        '''Setting Line 4 for the Message'''
        line4_label.grid(column=0, row=4, sticky='ns')
        line4_entry.grid(column=1, row=4, sticky='ew')
        line4_test_label.grid(column=2, row=4, sticky='ns')
        '''Setting Report Sender Button'''
        send_reports_button.grid(column=1, row=5)
    elif possibility==3:
        '''Setting Line 3 for the Message'''
        line3_label.grid(column=0, row=3, sticky='ns')
        line3_entry.grid(column=1, row=3, sticky='ew')
        line3_hw_label.grid(column=2, row=3, sticky='ns')
        '''Setting Report Sender Button'''
        send_reports_button.grid(column=1, row=4)
    elif possibility==4:
        '''Setting Line 4 for the Message'''
        line3_label.grid(column=0, row=3, sticky='ns')
        line4_entry.grid(column=1, row=3, sticky='ew')
        line4_test_label.grid(column=2, row=3, sticky='ns')
        '''Setting Report Sender Button'''
        send_reports_button.grid(column=1, row=4)

def reset_report_sender_frame():
    global possibility
    '''Resetting Heading'''
    report_sender_frame_head_label.grid_forget()
    '''Resetting Line 1 for the Message'''
    line1_label.grid_forget()
    line1_entry.grid_forget()
    line1_name_label.grid_forget()
    line1_entry_var.set(value="*Today's Session Report of :*")
    '''Resetting Line 2 for the Message'''
    line2_label.grid_forget()
    line2_entry.grid_forget()
    line2_att_label.grid_forget()
    line2_entry_var.set(value="*Attendance Status :*")
    if possibility==1:
        pass
    elif possibility==2:
        '''Resetting Line 3 for the Message'''
        line3_label.grid_forget()
        line3_entry.grid_forget()
        line3_hw_label.grid_forget()
        line3_entry_var.set(value="*Homework Status :*")
        '''Resetting Line 4 for the Message'''
        line4_label.grid_forget()
        line4_entry.grid_forget()
        line4_test_label.grid_forget()
        line4_entry_var.set(value="*Test Score :*")
    elif possibility==3:
        '''Resetting Line 3 for the Message'''
        line3_label.grid_forget()
        line3_entry.grid_forget()
        line3_hw_label.grid_forget()
        line3_entry_var.set(value="*Homework Status :*")
    elif possibility==4:
        '''Setting Line 4 for the Message'''
        line3_label.grid_forget()
        line4_entry.grid_forget()
        line4_test_label.grid_forget()
        line4_entry_var.set(value="*Test Score :*")

    send_reports_button.grid_forget()

report_sender_progress_bar_var = tk.IntVar(value=0)
def set_report_sender_progress_bar(c=0, r=0, st='ew', Max=5, cspan=2):
    global report_sender_progess_bar_var
    report_sender_progress_bar = ttk.Progressbar(report_sender_frame, orient='horizontal',
                                                 variable=report_sender_progress_bar_var, maximum=Max, mode='determinate')
    report_sender_progress_bar.grid(column=c, row=r, columnspan=cspan, sticky=st)

send_reports=False
times_report_sent=0
def send_reports_btn_func():
    global possibility, name_list, send_reports, times_report_sent, reports_sent
    print(name_list)
    print(len(name_list))
    confirm_msg = messagebox.askyesno("Confirmation", "Are you Sure,\nDo you want to Proceed?")
    print(confirm_msg)
    '''
    if confirm_msg==True:
        if possibility==1:
            send_reports_button.grid(column=0, row=3)
            report_sender_progess_label.grid(column=1, row=3, sticky='ns')
            set_report_sender_progress_bar(c=2, r=3, cspan=1, st='ew', Max=len(name_list))
            send_reports=True
        elif possibility==2:
            send_reports_button.grid(column=0, row=5)
            report_sender_progess_label.grid(column=1, row=5, sticky='ns')
            set_report_sender_progress_bar(c=2, r=5, cspan=1, st='ew', Max=len(name_list))
            send_reports=True
        elif possibility==3:
            send_reports_button.grid(column=0, row=4)
            report_sender_progess_label.grid(column=1, row=4, sticky='ns')
            set_report_sender_progress_bar(c=2, r=4, cspan=1, st='ew', Max=len(name_list))
            send_reports=True
        elif possibility==4:
            send_reports_button.grid(column=0, row=4)
            report_sender_progess_label.grid(column=1, row=4, sticky='ns')
            set_report_sender_progress_bar(c=2, r=4, cspan=1, st='ew', Max=len(name_list))
            send_reports=True
    '''
    if confirm_msg==True:
        if reports_sent==False:
            send_reports_in_whatsapp()
            times_report_sent+=1
        elif reports_sent==True:
            msg = messagebox.askyesno("INFO", "You have already sent all the reports!\nAre you sure, you want to send again?")
            if msg==True:
                reports_sent=False
                send_reports_in_whatsapp()
                times_report_sent+=1

times_updated_in_excel=0
def up_in_excel_btn_func():
    global possibility, reports, date_final, times_updated_in_excel
    if times_updated_in_excel==0:
        Excel_Automation.Update_In_Excel(batch_=batch_radio_var.get(), possibility_=possibility, report_list=reports, date_=date_final)
        times_updated_in_excel+=1
        messagebox.showinfo("INFO", "All the reports Successfully Updated in Excel!")
    elif times_updated_in_excel>=1:
        messagebox.showerror("Error", "Reports Already Updated!\nYou have already updated the Reports in the Excel file.")

next_press=0
marks_entry_caused_error = False
hw_entry_caused_error = False
test_topic_entry_caused_error = False
session_content_entry_caused_error = False
session_details_radio_caused_error = False
all_details_set = False
def UpdateNextButton():
    global next_press, name_list, all_details_set, marks_entry_caused_error, \
        hw_entry_caused_error, test_topic_entry_caused_error, session_content_entry_caused_error, session_details_radio_caused_error, reports_sent
    if batch_radio_var.get() == 'NULL':
        messagebox.showerror('Error', 'You have not selected any Batch!\nKindly select the required Batch.')

    elif next_press==0:
        ok_cancel = messagebox.askokcancel('Batch Selcted', f'BATCH SELECTED: {batch_radio_var.get()}')
        '''print(ok_cancel)'''
        if ok_cancel == True:
            session_details_frame.lift()
            update_top_frame_var.set(f"ENTER SESSION DETAILS[{batch_radio_var.get()}]")
            update_previous_button.grid(column=0, row=0, sticky='nsew')
            name_list,number_list = Name_List_Selection.select_for(batch=batch_radio_var.get())
            next_press+=1

    elif next_press==1:
        if ask_hw_radio_var.get()=='NULL' or ask_test_radio_var.get()=='NULL':
            messagebox.showerror('ERROR', 'Data Insufficient,\nKindly Fill All the Details')
            session_details_radio_caused_error=True
        else:
            session_details_radio_caused_error=False

        if ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
            if hw_entry_var.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient!\nPLease enter HW details!')
                hw_entry_caused_error=True
            else:
                hw_entry_caused_error=False
            try:
                if str(type(marks_entry_var.get())) not in ["<class 'int'>"]:
                    messagebox.showinfo('INFO', 'Maximum Marks should be an Integer!!')
                    marks_entry_caused_error=True
                else:
                    marks_entry_caused_error=False
            except:
                marks_entry_caused_error=True
                marks_entry_var.set(value=15)
                messagebox.showerror('Error', 'Maximum Marks should be a number!!')
            if test_topic_entry.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient!\nPLease enter Test Topic!')
                test_topic_entry_caused_error=True
            else:
                test_topic_entry_caused_error=False
            if session_content_var.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient,\nPLease enter Session Content Details!')
                session_content_entry_caused_error=True
            else:
                session_content_entry_caused_error=False

        elif ask_hw_radio_var.get()=='yes_hw_given' and ask_test_radio_var.get()=='no_test_taken':
            if hw_entry_var.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient!\nPLease enter HW details!')
                hw_entry_caused_error=True
            else:
                hw_entry_caused_error=False
            if session_content_var.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient,\nPLease enter Session Content Details!')
                session_content_entry_caused_error=True
            else:
                session_content_entry_caused_error=False

        elif ask_hw_radio_var.get()=='no_hw_given' and ask_test_radio_var.get()=='yes_test_taken':
            try:
                if str(type(marks_entry_var.get())) not in ["<class 'int'>"]:
                    messagebox.showinfo('INFO', 'Maximum Marks should be an Integer!!')
                    marks_entry_caused_error=True
                else:
                    marks_entry_caused_error=False
            except:
                marks_entry_caused_error=True
                marks_entry_var.set(value=15)
                messagebox.showerror('Error', 'Maximum Marks should be a number!!')
            if test_topic_entry.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient!\nPLease enter Test Topic!')
                test_topic_entry_caused_error=True
            else:
                test_topic_entry_caused_error=False
            if session_content_var.get()=='':
                messagebox.showerror('ERROR', 'Data Insufficient,\nPLease enter Session Content Details!')
                session_content_entry_caused_error=True
            else:
                session_content_entry_caused_error=False

        if marks_entry_caused_error==False and test_topic_entry_caused_error==False and \
                hw_entry_caused_error==False and session_content_entry_caused_error==False and session_details_radio_caused_error==False:
            all_details_set=True
        else:
            all_details_set=False

        if all_details_set==True:
            update_top_frame_var.set(f"UPDATE STUDENT REPORTS[{batch_radio_var.get()}]")
            progress_update_frame.lift()
            Show_empty_Reports()
            next_press+=1
            name_var.set(f"Report of {name_list[0]}")

    elif next_press==2:
        if save_n_conti_press==len(name_list):
            report_sender_frame.lift()
            set_report_sender_frame_grid()
            set_report_sender_frame_widgets()
            next_press+=1

    elif next_press==3:
        if reports_sent==True:
            update_in_excel_frame.lift()
            next_press+=1

    print(next_press)


previous_press=0
def UpdatePreviousButton():
    global next_press, name_list, times_updated_in_excel
    prev_msg_box=False
    if next_press==1:
        prev_msg_box = messagebox.askyesno('PREVIOUS', 'The Data will NOT be Saved.\nDo you want to Go Back?')
        if prev_msg_box==True:
            reset_session_details_frame()
            update_previous_button.grid_forget()
            update_top_frame_var.set("BATCH SELECTION")
            batch_selection_frame.lift()
            name_list=[]
            next_press-=1

    elif next_press==2:
        prev_msg_box = messagebox.askyesno('PREVIOUS', 'The Data will NOT be Saved.\nDo you want to Go Back?')
        if prev_msg_box==True:
            update_top_frame_var.set(f"ENTER SESSION DETAILS[{batch_radio_var.get()}]")
            reset_progress_update_frame()
            session_details_frame.lift()
            times_updated_in_excel=0
            next_press-=1

    elif next_press==3:
        prev_msg_box = messagebox.askyesno("PREVIOUS", "Are you Sure, you want to Go Back?")
        if prev_msg_box==True:
            reset_report_sender_frame()
            progress_update_frame.lift()
            next_press-=1
    elif next_press==4:
        prev_msg_box = messagebox.askyesno("PREVIOUS", "Are you Sure, you want to Go Back?")
        if prev_msg_box==True:
            report_sender_frame.lift()
            next_press-=1
    else:
        pass

def yes_hw_radio():
    hw_label.grid(column=1, row=1, sticky='ew')
    hw_entry.grid(column=2, row=1, sticky='ew')

def no_hw_radio():
    hw_label.grid_forget()
    hw_entry.grid_forget()
    hw_entry_var.set(value='Enter H.W. Details')

def yes_test_radio():
    test_marks_label.grid(column=1, row=3, sticky='ew')
    test_marks_entry.grid(column=2, row=3, sticky='w')

    test_topic_label.grid(column=1, row=4, sticky='ew')
    test_topic_entry.grid(column=2, row=4, sticky='ew')

def no_test_radio():
    test_marks_label.grid_forget()
    test_marks_entry.grid_forget()
    marks_entry_var.set(value=15)

    test_topic_label.grid_forget()
    test_topic_entry.grid_forget()
    test_entry_var.set(value='Enter Test Topic')

def send_review_btn_func():
    review = review_entry_var.get()
    send_whatsapp_message(body=f"{review}", num="7874015674")
    #send_whatsapp_message(msg=review)
    messagebox.showinfo("INFO", "Review Successfully Sent!")
    #review_entry_var.set(value="Write your review")


''' ---------- WIDGETS ---------- '''

''' --- Menu --- '''
main_menu_bar = tk.Menu(window)

# File Menu
file_menu = tk.Menu(main_menu_bar, tearoff=False)
file_menu.add_command(label='Update Report', command=lambda: update_report_frame.lift())
file_menu.add_command(label='New Report', command=lambda: new_report_frame.tkraise())
file_menu.add_command(label='Open Report', command=lambda: open_report_frame.lift())

help_menu = tk.Menu(main_menu_bar, tearoff=False)
help_menu.add_command(label='Contact Developer', command=lambda: help_required_frame.lift())

main_menu_bar.add_cascade(label='File', font='Calibri 20', menu=file_menu)
main_menu_bar.add_cascade(label='Help', font='Calibri 20', menu=help_menu)

window.configure(menu=main_menu_bar)

''' --- Creating Top Frame --- '''
# setting top frame in window
top_frame = ttk.Frame(window, relief='groove', borderwidth=5)

# widgets in the top frame
# left widget: label Heading
Heading_label = ttk.Label(top_frame, text='NAME OF THE INSTITUTE',
                          font='comicsans 20 bold', background='yellow', foreground='black')

# middle widget: label date
d = date.today()
print(d)
date_final = DateConfig.DateConversion(d)# This converts the date in the word format
date_label = ttk.Label(top_frame, text=f'{date_final}', font='Ariel 12')


# left widget: label Weekday
day = datetime.now().weekday()
current_day = ''
# print(day)
if day == 0:
    current_day = 'Monday'
elif day == 1:
    current_day = 'Tuesday'
elif day == 2:
    current_day = 'Wednesday'
elif day == 3:
    current_day = 'Thursday'
elif day == 4:
    current_day = 'Friday'
elif day == 5:
    current_day = 'Saturday'
    #print('Saturday')
elif day == 6:
    current_day = 'Sunday'

weekday_label = ttk.Label(top_frame, text=current_day, font='Ariel 12')


''' --- Creating Main Frame and Sub Frames --- '''
# Setting Main Frame in the window
main_frame = ttk.Frame(window, relief='groove', borderwidth=5)

''' Main Frame for Welcome'''
welcome_frame = ttk.Frame(main_frame, relief='groove', borderwidth=5)
''' Main Frame for Update Report '''
update_report_frame = ttk.Frame(main_frame, relief='groove', borderwidth=5)
''' Main Frame for New Report '''
new_report_frame = ttk.Frame(main_frame, relief='groove', borderwidth=5)
''' Main Frame for Open Report '''
open_report_frame = ttk.Frame(main_frame, relief='groove', borderwidth=5)
'''Help Required Frame'''
help_required_frame = ttk.Frame(main_frame, relief='groove', borderwidth=1)

''' widgets in the Main Welcome Frame '''
welcome_label = ttk.Label(welcome_frame, text="Hi, Welcome to\nProgress Report Management System", font='Calibri 24 bold')

''' Sub Frames in the Main Update Report Frame '''
update_top_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
batch_selection_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
session_details_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
progress_update_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
update_bottom_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
report_sender_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)
update_in_excel_frame = ttk.Frame(update_report_frame, relief='groove', borderwidth=5)

''' widgets in update_top_frame '''
update_top_frame_var = tk.StringVar(value="Select The Batch")
update_top_frame_label = ttk.Label(update_top_frame, textvariable=update_top_frame_var, font='Calibri 18 bold')

''' widgets in batch_selection_frame '''
batch_radio_var = tk.StringVar(value='NULL')
batch_radio1 = ttk.Radiobutton(batch_selection_frame, text='CLASS 11TH MON/THU BATCH',  variable=batch_radio_var, value='CLASS_11_B1', command=lambda: print("Radio Selected"))
batch_radio2 = ttk.Radiobutton(batch_selection_frame, text='CLASS 11TH TUE/FRI BATCH',  variable=batch_radio_var, value='CLASS_11_B2', command=lambda: print("Radio Selected"))
batch_radio3 = ttk.Radiobutton(batch_selection_frame, text='CLASS 11TH WED/SAT BATCH',  variable=batch_radio_var, value='CLASS_11_B3', command=lambda: print("Radio Selected"))
batch_radio4 = ttk.Radiobutton(batch_selection_frame, text='CLASS 12TH TUE/FRI BATCH',  variable=batch_radio_var, value='CLASS_12_B2', command=lambda: print("Radio Selected"))
batch_radio5 = ttk.Radiobutton(batch_selection_frame, text='CLASS 12TH WED/SAT BATCH',  variable=batch_radio_var, value='CLASS_12_B3', command=lambda: print("Radio Selected"))

''' widgets in session_details_frame '''
ask_hw = ttk.Label(session_details_frame, text='Was any H.W. Given?', font='Calibri 18 bold')

ask_hw_radio_var=tk.StringVar(value='NULL')
hw_radio1 = ttk.Radiobutton(session_details_frame, text='yes', value='yes_hw_given', variable=ask_hw_radio_var, command=yes_hw_radio)
hw_radio2 = ttk.Radiobutton(session_details_frame, text='no', value='no_hw_given', variable=ask_hw_radio_var, command=no_hw_radio)

hw_label = ttk.Label(session_details_frame, text='H.W.:', font='Calibri 15 bold')
hw_entry_var = tk.StringVar(value='Enter H.W. Details')
hw_entry = ttk.Entry(session_details_frame, textvariable=hw_entry_var)


ask_test = ttk.Label(session_details_frame, text='Was any Test Taken?', font='Calibri 18 bold')

ask_test_radio_var=tk.StringVar(value='NULL')
test_radio1 = ttk.Radiobutton(session_details_frame, text='yes', value='yes_test_taken', variable=ask_test_radio_var, command=yes_test_radio)
test_radio2 = ttk.Radiobutton(session_details_frame, text='no', value='no_test_taken', variable=ask_test_radio_var, command=no_test_radio)

test_marks_label = ttk.Label(session_details_frame, text='Max. Marks:', font='Calibri 15 bold')
marks_entry_var = tk.IntVar(value=15)
test_marks_entry = ttk.Entry(session_details_frame, textvariable=marks_entry_var)

test_topic_label = ttk.Label(session_details_frame, text='Topic:', font='Calibri 15 bold')
test_entry_var = tk.StringVar(value='Enter Test Topic')
test_topic_entry = ttk.Entry(session_details_frame, textvariable=test_entry_var)

session_content_label = ttk.Label(session_details_frame, text="Today's Session Content:", font='Calibri 16 bold')
session_content_var = tk.StringVar(value='Enter Session Content')
session_content_entry = ttk.Entry(session_details_frame, textvariable=session_content_var)


''' widgets in progress_update_frame '''
progress_update_frame_label = ttk.Label(progress_update_frame, text="Individual progress report\nwill be updated here", font='Algerian 16')

'''Sub-frames in progress_update_frame'''
progress_update_subframe_1 = ttk.Frame(progress_update_frame, borderwidth=5, relief='groove')
progress_update_subframe_2 = ttk.Frame(progress_update_frame, borderwidth=5, relief='groove')
progress_update_subframe_3 = ttk.Frame(progress_update_frame, borderwidth=5, relief='groove')
progress_update_subframe_4 = ttk.Frame(progress_update_frame, borderwidth=5, relief='groove')
progress_update_subframe_5 = ttk.Frame(progress_update_frame, borderwidth=5, relief='groove')

'''Widgets in subframe_1'''
name_var = tk.StringVar(value="Report of 'Student Name'")
name_label = ttk.Label(progress_update_subframe_1, text="Report of 'Student Name'", font='Times 18 bold', textvariable=name_var)

'''Widgets in Subframe_2'''
attendance_label = ttk.Label(progress_update_subframe_2, text='Attendance:', font='Times 18 bold')

attendance_var = tk.StringVar(value='Present')
attendance_radio1 = ttk.Radiobutton(progress_update_subframe_2, text='Present', value='Present', variable=attendance_var, command=att_radio1_func)
attendance_radio2 = ttk.Radiobutton(progress_update_subframe_2, text='Absent', value='Absent', variable=attendance_var, command=att_radio2_func)
attendance_radio3 = ttk.Radiobutton(progress_update_subframe_2, text='Other',value='attendance_other',variable=attendance_var, command=att_radio3_func)

att_entry_var = tk.StringVar(value='Null')
attendance_entry = ttk.Entry(progress_update_subframe_2, textvariable=att_entry_var)

'''Widgets in Subframe_3'''
hw_status_label = ttk.Label(progress_update_subframe_3, text="H.W. Status:", font='Times 18 bold')

hw_status_var = tk.StringVar(value='Complete')
hw_status_radio1 = ttk.Radiobutton(progress_update_subframe_3, text='Complete', value='Complete', variable=hw_status_var, command=hw_status_radio_1_func)
hw_status_radio2 = ttk.Radiobutton(progress_update_subframe_3, text='Incomplete', value='Incomplete', variable=hw_status_var, command=hw_status_radio_2_func)
hw_status_radio3 = ttk.Radiobutton(progress_update_subframe_3, text='Other', value='hw_status_other', variable=hw_status_var, command=hw_status_radio_3_func)

hw_status_entry_var = tk.StringVar(value="Null")
hw_status_entry = ttk.Entry(progress_update_subframe_3, textvariable=hw_status_entry_var)

'''Widgets in subframe_4'''
test_score_label = ttk.Label(progress_update_subframe_4, text="Test Score:", font='Times 18 bold')

test_score_var = tk.StringVar(value='Enter marks here')
test_score_entry = ttk.Entry(progress_update_subframe_4, textvariable=test_score_var)

test_out_of_label_var = tk.StringVar(value="out of max marks")
test_out_of_label = ttk.Label(progress_update_subframe_4, text="out of max. marks", textvariable=test_out_of_label_var)

test_other_radio_var = tk.StringVar(value='Null')
test_other_radio = ttk.Radiobutton(progress_update_subframe_4, text="Other:", value='test_score_other', variable=test_other_radio_var, command=test_other_radio_func)
test_other_entry_var = tk.StringVar(value='Null')
test_other_entry = ttk.Entry(progress_update_subframe_4, textvariable=test_other_entry_var)

'''Widgets in subframe_5'''
save_n_continue = ttk.Button(progress_update_subframe_5, text="Save & Continue", command=save_and_continue)
'''progress bar in save_n_conti function'''
back_button = ttk.Button(progress_update_subframe_5, text='Back', command=back_button_func)

''' widgets in update_bottom_frame '''
update_next_button = ttk.Button(update_bottom_frame, text='NEXT', command=UpdateNextButton)
update_previous_button = ttk.Button(update_bottom_frame, text='PREVIOUS', command=UpdatePreviousButton)

'''widgets in message_sender_frame'''
report_sender_frame_head_label = ttk.Label(report_sender_frame, text="Message Editor", font="Calibri 18 bold")

line1_label = ttk.Label(report_sender_frame, text="Line 1:", font="Times 14 bold")
line2_label = ttk.Label(report_sender_frame, text="Line 2:", font="Times 14 bold")
line3_label = ttk.Label(report_sender_frame, text="Line 3:", font="Times 14 bold")
line4_label = ttk.Label(report_sender_frame, text="Line 4:", font="Times 14 bold")

'''Tkinter variables for entry fields'''
line1_entry_var = tk.StringVar(value="*Today's Session Report of :*")
line2_entry_var = tk.StringVar(value="*Attendance Status :*")
line3_entry_var = tk.StringVar(value="*Homework Status :*")
line4_entry_var = tk.StringVar(value="*Test Score :*")

line1_entry = ttk.Entry(report_sender_frame, textvariable=line1_entry_var)
line2_entry = ttk.Entry(report_sender_frame, textvariable=line2_entry_var)
line3_entry = ttk.Entry(report_sender_frame, textvariable=line3_entry_var)
line4_entry = ttk.Entry(report_sender_frame, textvariable=line4_entry_var)

line1_name_label = ttk.Label(report_sender_frame, text="Student Name", font="Times 14 bold")
line2_att_label = ttk.Label(report_sender_frame, text="Attendance Status", font="Times 14 bold")
line3_hw_label = ttk.Label(report_sender_frame, text="HW Status", font="Times 14 bold")
line4_test_label = ttk.Label(report_sender_frame, text="Test Status", font="Times 14 bold")

send_reports_button = ttk.Button(report_sender_frame, text="Send Reports in Whatsapp", command=send_reports_btn_func)

report_sender_progress_label = ttk.Label(report_sender_frame, text="Please Wait...", font="Times 16 bold")

'''report_sender_progess_bar = ttk.Progressbar(report_sender_frame, orient='horizontal', )'''


'''widgets in update_in_excel frame'''
update_in_excel_button = ttk.Button(update_in_excel_frame, text="Update in Excel", command=up_in_excel_btn_func)


''' widgets in the new_report_frame '''
new_label = ttk.Label(new_report_frame, text="This will create New Progress Report.", font='Calibri 18 bold')
''' widgets in the open_report_frame '''
open_label = ttk.Label(open_report_frame, text="This will open Students' Progress Report.", font='Calibri 18 bold')

'''Widgets in Help Required Frame'''
review_label = ttk.Label(help_required_frame, text="Review :", font="Algerian 16 bold")
review_entry_var = tk.StringVar(value="Write your review")
review_entry = ttk.Entry(help_required_frame, textvariable=review_entry_var)

send_review_button = ttk.Button(help_required_frame, text="Send to Developer", command=send_review_btn_func)


''' ---------- LAYOUTS ---------- '''
# Setting Main Grid Layout
window.columnconfigure(0, weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=10, uniform='a')

''' --- Top Frame --- '''
# Top frame in window
top_frame.grid(row=0, column=0, sticky='nsew')
# Grid Layout inside the top frame
top_frame.columnconfigure(0, weight=2, uniform='b')
top_frame.columnconfigure((1, 2), weight=1, uniform='b')
top_frame.rowconfigure(0, weight=1, uniform='b')

# widgets in top frame
Heading_label.grid(column=0, row=0, sticky='sw', padx=5)
date_label.grid(column=1, row=0, sticky='se')
weekday_label.grid(column=2, row=0, sticky='s')

''' --- Main Frame --- '''
# Setting Main Frame in window
main_frame.grid(column=0, row=1, sticky='nsew')

# Grid Layout inside the main frame for Sub Frames
main_frame.columnconfigure(0, weight=1, uniform='c')
main_frame.rowconfigure(0, weight=1, uniform='c')

''' Setting Welcome frame '''
welcome_frame.grid(column=0, row=0, sticky='nsew')
welcome_frame.columnconfigure(0, weight=1, uniform='d')
welcome_frame.rowconfigure(0, weight=1, uniform='d')
welcome_frame.lift()

''' Setting Update Report frame '''
update_report_frame.grid(column=0, row=0, sticky='nsew')

update_report_frame.columnconfigure(0, weight=1)
update_report_frame.rowconfigure(0, weight=1, uniform='h')
update_report_frame.rowconfigure(1, weight=10, uniform='h')
update_report_frame.rowconfigure(2, weight=1, uniform='h')

# setting sub-frames in update report frame
'''Top Frame 1'''
update_top_frame.grid(column=0, row=0, sticky='nsew')
update_top_frame.columnconfigure(0, weight=1)
update_top_frame.rowconfigure(0, weight=1)

update_top_frame_label.grid(column=0, row=0)

'''Middle Frame 1'''
batch_selection_frame.grid(column=0, row=1, sticky='nsew')

if current_day=='Sunday':
    batch_selection_frame.columnconfigure(0, weight=1, uniform='i')
    batch_selection_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='i')

    batch_radio1.grid(column=0, row=0, sticky='ns')
    batch_radio2.grid(column=0, row=1, sticky='ns')
    batch_radio3.grid(column=0, row=2, sticky='ns')
    batch_radio4.grid(column=0, row=3, sticky='ns')
    batch_radio5.grid(column=0, row=4, sticky='ns')

    batch_selection_frame.lift()

elif current_day == 'Monday' or current_day == 'Thursday':
    batch_selection_frame.columnconfigure(0, weight=1, uniform='k')
    batch_selection_frame.rowconfigure(0, weight=1, uniform='k')

    batch_radio1.grid(column=0, row=0, sticky='ns')

    batch_selection_frame.lift()

elif current_day == 'Tuesday' or current_day == 'Friday':
    batch_selection_frame.columnconfigure(0, weight=1, uniform='l')
    batch_selection_frame.rowconfigure([0, 1], weight=1, uniform='l')

    batch_radio2.grid(column=0, row=0, sticky='ns')
    batch_radio4.grid(column=0, row=1, sticky='ns')

    batch_selection_frame.lift()

elif current_day == 'Wednesday' or current_day == 'Saturday':
    batch_selection_frame.columnconfigure(0, weight=1, uniform='m')
    batch_selection_frame.rowconfigure((0, 1), weight=1, uniform='m')

    batch_radio3.grid(column=0, row=0, sticky='ns')
    batch_radio5.grid(column=0, row=1, sticky='ns')

    batch_selection_frame.lift()

'''Middle Frame 2'''
session_details_frame.grid(column=0, row=1, sticky='nsew')

session_details_frame.columnconfigure((0, 1, 2), weight=1, uniform='session_details')
session_details_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='session_details')

ask_hw.grid(column=0, row=0, rowspan=2, sticky='nsew')
hw_radio1.grid(column=1, row=0, sticky='nsew')
hw_radio2.grid(column=2, row=0, sticky='nsew')

ask_test.grid(column=0, row=2, rowspan=3, sticky='nsew')
test_radio1.grid(column=1, row=2, sticky='nsew')
test_radio2.grid(column=2, row=2, sticky='nsew')

session_content_label.grid(column=0, row=5, sticky='nsew')
session_content_entry.grid(column=1, row=5, columnspan=2, sticky='ew')

'''Middle Frame 3'''
progress_update_frame.grid(column=0, row=1, sticky='nsew')


'''Bottom Frame 1'''
update_bottom_frame.grid(column=0, row=2, sticky='nsew')
update_bottom_frame.columnconfigure((0, 1), weight=1, uniform='j')
update_bottom_frame.rowconfigure(0, weight=1, uniform='j')

update_next_button.grid(column=1, row=0, sticky='nsew')


'''setting message_sender_frame'''
report_sender_frame.grid(column=0, row=1, sticky='nsew')

report_sender_frame.columnconfigure(0, weight=1, uniform='msg_sender_frame')
report_sender_frame.rowconfigure(0, weight=1, uniform='msg_sender_frame')

report_sender_frame_head_label.grid(column=0, row=0, sticky='nsew')

'''Setting update_in_excel_frame'''
update_in_excel_frame.grid(column=0, row=1, sticky='nsew')

update_in_excel_frame.columnconfigure(0, weight=1, uniform='up_in_excel')
update_in_excel_frame.rowconfigure(0, weight=1, uniform='up_in_excel')

'''setting widgets in update_in_excel_frame'''
update_in_excel_button.grid(column=0, row=0)


''' Setting New Report frame '''
new_report_frame.grid(column=0, row=0, sticky='nsew')
new_report_frame.columnconfigure(0, weight=1, uniform='f')
new_report_frame.rowconfigure(0, weight=1, uniform='f')

''' Setting Open Report frame '''
open_report_frame.grid(column=0, row=0, sticky='nsew')
open_report_frame.columnconfigure(0, weight=1, uniform='g')
open_report_frame.rowconfigure(0, weight=1, uniform='g')

# setting widgets in welcome frame
welcome_label.grid(column=0, row=0)
# setting widgets in new report frame
new_label.grid(column=0, row=0)
# setting widgets in open report frame
open_label.grid(column=0, row=0)

'''Setting help required frame'''
help_required_frame.grid(column=0, row=0, sticky='nsew')

help_required_frame.columnconfigure((0,1), weight=1, uniform='help')
help_required_frame.rowconfigure(0, weight=5, uniform='help')
help_required_frame.rowconfigure(1, weight=1, uniform='help')

review_label.grid(column=0, row=0, sticky='nse')
review_entry.grid(column=1, row=0, sticky='w')
send_review_button.grid(column=0, row=1, columnspan=2, sticky='n')

''' ----- events ----- '''
main_frame.bind('<ButtonPress>', lambda event : print("How can I help you?"))
def reset_test_other_entry():
    test_other_entry_var.set(value='Null')
    test_other_entry.grid_forget()
    test_other_radio_var.set(value='Null')
    test_score_var.set(value='')
test_score_entry.bind("<ButtonPress>",lambda event :reset_test_other_entry())

def test_other_entry_event():
    test_score_var.set(value='Enter marks here')
    test_other_entry_var.set(value='')
test_other_entry.bind('<ButtonPress>', lambda event: test_other_entry_event())

hw_entry.bind("<ButtonPress>", lambda event: hw_entry_var.set(value=''))
test_topic_entry.bind("<ButtonPress>", lambda event: test_entry_var.set(value=''))
session_content_entry.bind("<ButtonPress>", lambda event: session_content_var.set(value=''))

attendance_entry.bind("<ButtonPress>", lambda event: att_entry_var.set(value=''))
hw_status_entry.bind("<ButtonPress>", lambda event: hw_status_entry_var.set(value=''))

review_entry.bind('<ButtonPress>', lambda event: review_entry_var.set(value=''))


# run for main window
window.mainloop()
