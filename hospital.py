#from doctor import *
from admin import *

user = ['A',5]
# commands:
DOC = ['search', 'add']
NURSE = []
ADMIN = ['doctor_sum','drug_sum','pos_med','pos_diag']
# user[0] = role
# user[1] = staff id

# After user logs in, continuously ask what to do until they log out.

print "Available operations: ",
if user[0] == "D":
     print ' ,'.join(DOC)
elif user[0] == "N":
     print ' ,'.join(NURSE)
else:
    print ' ,'.join(ADMIN)

while True:
     op = raw_input("Please enter an operation or 'logout' to quit: ").lower()
     #Doctors
     if user[0] == "D":
          if op == "search":
               get_chart()

          elif op == "add":
               line_type = raw_input("Enter line type ('S','D','M' or '0' to exit): ").upper()
               while line_type not in "SDM":
                    line_type = raw_input("Enter line type ('S','D','M' or '0' to exit): ")
                    if line_type == '0':
                         break
               if line_type == '0':
                    continue
                              
               add_line(line_type)

          elif op == 'logout':
               print "Goodbye!"
               break

          else:
               print "Invalid Command"

     #ADMIN
     if user[0] == "A":
          if op == "doctor_sum":
               admin_query1()
               
          elif op == "drug_sum":
               admin_query2()
               
          elif op == "pos_med":
               admin_query3()
               
          elif op == "pos_diag":
               admin_query4()
          elif op == "logout":
               print "Goodbye!"
               break
          
          #NURSE
     elif user[0] == "N":
          pass
          