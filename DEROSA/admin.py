#=========================================RAILWAY RESERVATION STSTEM================================================================
import views
import sys
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='deepak0913',database='railways')
'''if conn.is_connected():
    print("Successfully connected")
else:
    print("not connected")'''

cur=conn.cursor()
"""ADMIN related functions"""

def ad_sch():
 while True:
    print("|_____________EMPLOYEE PORTAL_____________|",file=sys.stderr)
    print("1. Train Schedule")
    print("2. Passenger Status")
    print("3. Payment Details")
    print("4. Back")
    x=int(input("Enter your choice 1-4: "))
    if x==1:
          print("\n'_________TRAIN SCHEDULE_________'\n",file=sys.stderr)
          cur.execute("select* from train_schedule")
          dat=cur.fetchall()
          print("__TRAIN NO.__||__TRAIN NAME__||__ORIGIN__||__DESTINATION__||__ RUNS ON__",file=sys.stderr)
          for i in dat:
              print(i)
          wait=input("\nPRESS A KEY TO CONTINUE\n")
          while True:
                print("\n__ADMIN_ONLY__",'\n','\n',file=sys.stderr)
                print("|_____________ALTER TRAIN DETAILS_____________|",file=sys.stderr)
                print("1.Change Arrival time")
                print("2.Change Departure time")
                print("3.Add Train details")
                print("4.Change train details")
                print("5.MAIN MENU")
                y=int(input("Enter your choice 1-5: "))
                if y==1:
                    vg=input('enter station name: ')
                    cz=int(input("Enter train no.: "))
                    cy=input("Enter new ARRIVAL time(in format HH:MM:SS): ")
                    t='timetable_'+str(cz)
                    try:
                      cur.execute("update %s set ARRIVAL='%s' where STATION_NAME='%s'"%(t,cy,vg))
                      conn.commit()
                      print("UPDATED!!!!",file=sys.stderr)
                      wait=input("\nPRESS A KEY TO CONTINUE\n")
                    except:
                      print("Station doesn't exist in train's route",file=sys.stderr)
                      wait=input("\nPRESS A KEY TO CONTINUE\n")
            

                elif y==2:
                    ch2=input("Enter Station name: ")
                    ch=int(input("Enter train no.: "))
                    ch3=input("Enter new departure time(in format HH:MM:SS): ")
                    t='timetable_'+str(ch)
                    try:
                       cur.execute("update %s set DEPARTURE='%s' where STATION_NAME='%s'"%(t,ch3,ch2))
                       conn.commit()
                       print("UPDATED!!!!",file=sys.stderr)
                       wait=input("\nPRESS A KEY TO CONTINUE\n")
                    except:
                       print("Station doesn't exist in train's route",file=sys.stderr)
                       wait=input("\nPRESS A KEY TO CONTINUE\n")
                elif y==3:
                   a=int(input("enter train no"))
                   b=input("enter train name")
                   c=input("Enter ORIGIN station")
                   d=input("Enter DESTINATION station")
                   e=input("Enter working days(seperated by spaces)")
                   nd="insert into train_schedule values(%s,'%s','%s','%s','%s')"%(a,b,c,d,e)
                   cur.execute(nd)
                   conn.commit()
                   print("TRAIN DETAILS ADDED!!!!",file=sys.stderr)
                   wait=input("\nPRESS A KEY TO CONTINUE\n")
                elif y==4:
                    while True:
                      print("1.Change ORIGIN")
                      print("2.Change DESTINATION")
                      print("3.WORKING DAYS")
                      print("4.DELETE ALL DETAILS")
                      print("5.BACK")
                      q=int(input("Enter choice 1-5:"))
                      if q==1:
                          orn=int(input("Enter train no:"))
                          org=input("Enter ORIGIN station")
                          cur.execute("update train_schedule set ORIGIN='%s' where train_no=%s"%(org,orn))
                          conn.commit()
                          print("UPDATED!!!!",file=sys.stderr)
                          wait=input("\nPRESS A KEY TO CONTINUE\n")
                      elif q==2:
                          drn=int(input("Enter train no:"))
                          des=input("Enter DESTINATION station")
                          cur.execute("update train_schedule set DESTINATION='%s' where train_no=%s"%(des,drn))
                          conn.commit()
                          print("UPDATED!!!!",file=sys.stderr)
                          wait=input("\nPRESS A KEY TO CONTINUE\n")
                      elif q==3:
                          wtn=int(input("Enter train no:"))
                          wd=input("Enter WORKING DAYS(separated by spaces)")
                          cur.execute("update train_schedule set RUNS_ON='%s' where train_no=%s"%(wd,wtn))
                          conn.commit()
                          print("UPDATED!!!!",file=sys.stderr)
                          wait=input("\nPRESS A KEY TO CONTINUE\n")
                      elif q==4:
                          dtn=int(input("Enter train no"))
                          t='timetable_'+str(dtn)
                          cur.execute("delete from train_schedule where TRAIN_NO={}".format(dtn))
                          #cur.execute("delete* from %s"%(t))
                          conn.commit()
                          print("TRAIN DETAILS DELETED!!!!",file=sys.stderr)
                          wait=input("\nPRESS A KEY TO CONTINUE\n")
                      elif q==5:
                          break
                elif y==5:
                    break
    elif x==2:
        pass_status()
    elif x==3:
        cur.execute("select * from PAYMENT_DETAILS")
        DAT=cur.fetchall()
        for i in DAT:
            print(i)
    elif x==4:
        break
    else:
        print("\nINVALID CHOICE!!!!!\n",file=sys.stderr)
        wait=input("\nEnter a key to continue\n")


def admin_login():
    f=open(r"admin_login_details.txt",'r')
    pw=input("If administrator, insert password(case sensitive): ")
    password=f.read()
    if pw==password:
        return True
    f.close()


def pass_status():
    while True:
        x=int(input("Enter 12-digit PNR no.: "))
        cur.execute("select * from passenger where PNR=%s"%(x,))
        pdet=cur.fetchall()
        print("Passenger details:-\n",pdet)
        print("___PNR___|__NAME__|AGE|GENDER|TRAIN_NO|_ORIGIN_|DESTINATION|_DOJ_|CLASS|_STATUS_|")
        wait=input("Enter to continue")
        print("1.Change Seat Status")
        print("2.BACK")
    ##    print("3.WORKING DAYS")
    ##    print("4.DELETE ALL DETAILS")
    ##    print("5.BACK")
        ch=int(input("Enter your choice:(1-2) "))
        if ch==1:
            Y=input("Enter updated seat status: ")
            cur.execute("update passenger set SEAT_STATUS='%s'"%(Y))
            conn.commit()
            wait=input("\nEnter a key to continue\n")
        elif ch==2:
            break
        else:
            print("\nINVALID CHOICE!!!!!\n",file=sys.stderr)
            wait=input("\nEnter a key to continue\n")
            pass_status()

