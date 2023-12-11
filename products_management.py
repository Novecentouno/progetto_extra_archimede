from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    
    #validate
    accepted = accept_var.get()
    
    if accepted == 'Accepted':
    # print('hi')
        firstname = firstName_entry.get()
        lastname = lastName_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numSemesters = numSemesters_spinbox.get()

            print('firstname: ',firstname, 'lastname: ', lastname)
            print('title: ',title, 'age: ', age, 'nationality: ', nationality)
            print('# courses: ',numcourses, '# semesters: ', numSemesters)
        else:
            messagebox.showwarning(title='Error', message='First and last name are required')
    else:
        messagebox.showwarning(title='Error', message='You have not accepted the terms')

    
window = Tk()
window.title("Gestione Prodotti")

frame=ttk.Frame(window)
frame.pack()

user_info_frame = ttk.LabelFrame(frame, text='Inserisci un prodotto')
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

#firstname & lastname
firstName_label = ttk.Label(user_info_frame, text = 'First Name')
firstName_label.grid(row=0, column=0)
lastName_label = ttk.Label(user_info_frame, text = 'Last Name')
lastName_label.grid(row=0, column=1)

firstName_entry = ttk.Entry(user_info_frame)
lastName_entry = ttk.Entry(user_info_frame)
firstName_entry.grid(row=1, column=0)
lastName_entry.grid(row=1, column=1)

#title
title_label=ttk.Label(user_info_frame, text='Title')
title_combobox=ttk.Combobox(user_info_frame, values=['','mr', 'ms'])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

#age
age_label=ttk.Label(user_info_frame, text='Age')
age_spinbox=ttk.Spinbox(user_info_frame, from_=18, to=99)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

#nationality
nationality_label=ttk.Label(user_info_frame, text='Nationality')
nationality_combobox=ttk.Combobox(user_info_frame, values=['','Asia', 'Africa', 'Europe', 'America', 'Oceania'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#other frame
courses_frame=ttk.Labelframe(frame)
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

#registration status
registered_label=ttk.Labelframe(courses_frame, text='Registration Status')

reg_status_var = StringVar(value='Not Registered')
registered_check = ttk.Checkbutton(courses_frame, text='Currently Registered', variable=reg_status_var, onvalue='Registered', offvalue='Not Registered')

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

#courses
numcourses_label = ttk.Label(courses_frame, text='# Completed Courses')
numcourses_spinbox = ttk.Spinbox(courses_frame, from_=0, to=90)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

#semesters
numSemesters_label = ttk.Label(courses_frame, text='# Semesters')
numSemesters_spinbox = ttk.Spinbox(courses_frame, from_=0, to=50)
numSemesters_label.grid(row=0, column=2)
numSemesters_spinbox.grid(row=1, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#terms & condition
terms_frame=ttk.Labelframe(frame, text='Terms and Conditions')
terms_frame.grid(row=2, column=0, sticky='news', padx=20, pady=20)

#accept
accept_var=StringVar(value='Not accepted')
terms_check=ttk.Checkbutton(courses_frame, text='I accept the terms', variable=accept_var, onvalue='Accepted', offvalue='Not accepted')
terms_check.grid(row=0, column=0)

#button
btn=ttk.Button(frame, text='Enter data', command=enter_data)
btn.grid(row=3, column=0, sticky='news', padx=20, pady=20)


window.mainloop()