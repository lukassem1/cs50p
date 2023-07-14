import pandas as pd
# Start coding here... 

df_office_ad = pd.read_csv('datasets/office_addresses.csv')
#print(df_office_ad.head())

df_employee_ad = pd.read_excel('datasets/employee_information.xlsx')
#print(df_employee_ad.head())

emergency_contacts_header = ('employee_id', 'last_name', 'first_name', 'emergency_contact', 'emergency_contact_number', 'relationship')
df_employee_emerg = pd.read_excel('datasets/employee_information.xlsx', sheet_name = 'emergency_contacts', header = None, names = emergency_contacts_header)                 
#print(df_employee_emerg)

#employee_roles_header = 
df_employee_roles = pd.read_json('datasets/employee_roles.json', orient= 'index')
#print(df_employee_roles)


#merging the data

employees = df_employee_ad.merge(df_office_ad, how= 'left', left_on='employee_country', right_on='office_country')
#print(employees.head())

updated_employees = employees.merge(df_employee_roles, how= 'inner', left_on='employee_id', right_index=True)
#print(updated_employees)

s_updated_employees = updated_employees.merge(df_employee_emerg, how= 'inner', left_on='employee_id', right_on='employee_id')
#print(s_updated_employees)


#print(s_updated_employees)
#print(list(s_updated_employees.columns))

dropped_emp = s_updated_employees.drop(columns=['last_name','first_name'])
#print()
#print(list(dropped_emp.columns))
dropped_emp = dropped_emp.rename(columns={"employee_last_name": "last_name", "employee_first_name": "first_name"})
for column in dropped_emp.columns:
    if column.startswith('office'):
        dropped_emp[column].fillna('Remote', inplace=True)
#print()
#print(list(dropped_emp.columns))
#print()
final_columns = ["employee_id", "first_name", 'last_name', "employee_country", "employee_city", "employee_street", "employee_street_number", "emergency_contact", 'emergency_contact_number', "relationship", 'monthly_salary', "team", "title", "office", "office_country", 'office_city', 'office_street', "office_street_number"]
employees_final = dropped_emp[final_columns]
employees_final.set_index("employee_id", inplace=True)
print(employees_final)
