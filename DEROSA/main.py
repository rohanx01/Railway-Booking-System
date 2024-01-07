#=========================================RAILWAY RESERVATION SYSTEM================================================================
import views
import passenger as qw
#import math
import sys
import admin
##import random
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='deepak0913',database='railways')
##if conn.is_connected():
##    print("Successfully connected")
##else:
##    print("not connected")
cur=conn.cursor()
#
#
#
#
#

views.head()
views.top()
views.instructions()
while True:
    print("__________+ L O G I N +________ :",file=sys.stderr)
    print("1. ADMIN/EMPLOYEE")
    print("2. PASSENGER")
    print("3. QUIT")
    c=int(input("Enter your choice: "))
    #
    #
    #
    if c==1:
        if admin.admin_login() is True:
             print("WELCOME ADMIN",file=sys.stderr) ; print("\n",'\n')
             wait=input("\nPRESS A KEY TO CONTINUE\n")
             admin.ad_sch()
             wait=input("\nPRESS A KEY TO CONTINUE\n")
        else:
            print("WRONG PASSWORD!!!!!!!!\nACCESS DENIED, VISIT AGAIN...!!!!",file=sys.stderr)
            #
            #
            #
    elif c==2:
        while True:
            print("=========================_____||~~~~~~~~~~WELCOME~~~~~~~~~~||_____=========================")
            qw.pass_login()
            ch=int(input("Enter your choice 1-6 : "))
            #
            #
            if ch==1:
                cur.execute("select* from train_schedule")
                dat=cur.fetchall()
                print("__TRAIN NO.__||__TRAIN NAME__||__ORIGIN__||__DESTINATION__||__ RUNS ON__",file=sys.stderr)
                for i in dat:
                    print(i)
                wait=input("\nPRESS A KEY TO CONTINUE\n")
            elif ch==2:
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                qw.reservation()
                wait=input("\nPRESS A KEY TO CONTINUE\n")
            elif ch==3:
                qw.ticketdetails()
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                #pnr status ka yaha
            elif ch==4:
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                qw.cancel_reservation()
                wait=input("\nPRESS A KEY TO CONTINUE\n")
            elif ch==5:
                    while True:
                        wait=input("\nPRESS A KEY TO CONTINUE\n")
                        print("a. Seat Availability")
                        print("b. Fare Enquiry")
                        print("c. Train Route")
                        print("d. Back")
                        cc=input("Enter choice (a-d) : ")
                        if cc=='a':
                            qw.seat_availability() 
                            wait=input("\nPRESS A KEY TO CONTINUE\n")
                        elif cc=='b':
                            wait=input("\nPRESS A KEY TO CONTINUE\n")
                            qw.fare_main()
                            wait=input("\nPRESS A KEY TO CONTINUE\n")
                        elif cc=='c':
                            qw.route()
                            wait=input("\nPRESS A KEY TO CONTINUE\n")
                        elif cc=='d':
                            break
            elif ch==6:
                break
            else:
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                print("INVALID CHOICE...!!!!!!!",file=sys.stderr)
                wait=input("\nPRESS A KEY TO CONTINUE\n")
    elif c==3:
        views.quit()
        break

