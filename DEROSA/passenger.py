#=========================================RAILWAY RESERVATION STSTEM================================================================
import sys
import random
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='deepak0913',database='railways')
##if conn.is_connected():
##    print("Successfully connected")
##else:
##    print("not connected")
cur=conn.cursor()
"""PASSENGER related Functions"""

def payment(pnr,fare):
    cn='anon'
    #faredist()
    for i in range(3):
        ac=str(input("ENTER YOUR 12-DIGIT DEBIT/CREDIT CARD NUMBER:"))
        if len(ac)!=12:
            print("CHECK YOUR CARD NO. IT MUST BE OF 12 DIGIT!")
            print("MAXIMUM ATTEMPTS LEFT:",2-i)
        else:
            cn="CARD ACCEPTED"
            break
    if cn=="CARD ACCEPTED":
        er=str(random.randint(10000,999999))
        file1=open("OTP FOR TRANSACTION.txt","w+")
        file1.write("Please enter the OTP given below in the Program:\n")
        file1.write(er)
        file1.close()
        otp=str(input("ENTER OTP SENT TO YOUR FOLDER:"))
        if otp==er:
            print("TRANSACTION SUCCESSFUL")
            tr_id='DD-SS-RK'+' '+str(random.randint(100000000000,9896687865786))
            print("YOUR TRANSACTION ID IS:",tr_id)
            print("Keep it for future use :)")
            cur.execute("INSERT INTO PAYMENT_DETAILS VALUES({},'{}',{})".format(pnr,tr_id,fare))
            conn.commit()
            return ("DONE")
        else:
            print("INCORRECT OTP,FOR SECURITY REASONS WE ARE CANCELLING YOUR TICKET:")
            return ('CANCEL TICKET')
    else:
        print("YOU HAVE REACHED MAXIMUM LIMITS...CANCELLING TICKET.....")
        return ("CANCEL TICKET")


def reservation():
    print("|_____________RESERVATION PORTAL_____________|",file=sys.stderr)
    aa=int(input("Add number of Travellers:"))
    while True:
        a=int(input("Enter desired train no. for reservation:"))
        cur.execute("select * from Train_Schedule where train_no={}".format(a))
        data1=cur.fetchall()
        if len(data1)==0:
            print("Train doesn't exist in our database! We Are Improving :)")
            continue
        break
    while True:
        b=input("Enter BOARDING POINT:")
        cur.execute("select STATION_NAME from TIMETABLE_{} where STATION_NAME='{}'".format(a,b))
        data2=cur.fetchall()
        if len(data2)==0:
            print("Station Doesn't Exist in Train's Route!")
            wait=input("\nPRESS A KEY TO CONTINUE\n")
            continue
        break
    while True:
        c=input("Enter Destination:")
        cur.execute("select STATION_NAME from TIMETABLE_{} where STATION_NAME='{}'".format(a,c))
        data3=cur.fetchall()
        if len(data3)==0:
            print("Station Doesn't Exist in Train's Route!")
            wait=input("\nPRESS A KEY TO CONTINUE\n")
            continue
        break
        
        
    while True:       
        d=input("Enter date of journey(in format YYYY-MM-DD) : ")
        print("--Class details--")
        kp=input("Type 3AC/2AC/SL(any one):")
        if kp=='3AC':
            cur.execute("select Date_of_Journey,STATUS_3AC,3AC FROM seat_availability_for_{} where Date_of_Journey='{}'".format(a,d))
            data4=cur.fetchall()
            if len(data4)==0:
                print("TRAIN DOES NOT RUN ON",d)
                print("Try choosing another Date Or refer to Train Schedule")
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                continue
            print("(DATE OF JOURNEY,AVAILABLE/WAITING/RAC,STATUS)")
            for i in data4:
                axe=i[1]
                axe1=i[2];print(axe1)
                print(i)
            wait=input("\nPRESS A KEY TO CONTINUE\n")
            cl='B'+str(random.randint(1,4))
            break
        elif kp=='2AC':
            cur.execute("select Date_of_Journey,STATUS_2AC,2AC FROM seat_availability_for_{} where Date_of_Journey='{}'".format(a,d))
            data4=cur.fetchall()
            if len(data4)==0:
                print("TRAIN DOES NOT RUN ON",d)
                print("Try choosing another Date Or refer to Train Schedule")
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                continue
            print("(DATE OF JOURNEY,AVAILABLE/WAITING/RAC,STATUS)")
            for i in data4:
                axe=i[1]
                axe1=i[2]
                print(i)
            wait=input("\nPRESS A KEY TO CONTINUE\n")
            cl='A'+str(random.randint(1,4))
            break       
        elif kp=='SL':
            cur.execute("select Date_of_Journey,STATUS_SL,SLEEPER FROM seat_availability_for_{} where Date_of_Journey='{}'".format(a,d))
            data4=cur.fetchall()
            if len(data4)==0:
                print("TRAIN DOES NOT RUN ON",d)
                print("Try choosing another Date Or refer to Train Schedule")
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                continue
            print("(DATE OF JOURNEY,AVAILABLE/WAITING/RAC,STATUS)")
            for i in data4:
                axe=i[1]
                axe1=i[2]
                print(i)
            cl='S'+str(random.randint(1,12))
            break
        else:
            print("wrong choice!")
            continue
        
    while True:
        if axe=='GNWL' or axe=='PQWL' or axe=='RLWL' or axe=='REGRET' or axe=='CLASS DOES NOT EXIST':
            print("SORRY CURRENTLY WE DON'T BOOK IN WAITING QUOTA! TRY IN DIFFERENT CLASS OR DATE :)")
            wait=input("\nPRESS A KEY TO CONTINUE\n")
            break
        f,dst=faredist(a,b,c,kp)
        print("YOUR TOTAL FARE FOR THE JOURNEY IS: ",aa*f,'\n','AND DISTANCE IS: ',dst,' KMS')
        ps=input("Want To Continue(Y/N):")
        if ps!='Y':
            print("See you Again!")
            break
        pnr=random.randint(100000000000,999999999999)
        

        pr=input("PRESS ENTER TO GET TO PAYMENT GATEWAY:")
        if pr=='':
            pss=payment(pnr,aa*f)
            if pss=='DONE':
                if axe=='RAC':
                    #print("Your PNR no. is: ",pnr)
                    
                    for i in range(aa):
                        print("Fill up the Details of Passenger",i+1)
                        x=input("Enter Name of Passenger:")
                        y=int(input("Enter age of passenger: "))
                        z=input("Enter Gender M/F/Others: ")
                        xp='RAC'+' '+str(axe1+(i+1))
                        #print("Your seat details are: ")
                        #print(xp)
                        #Yaha seat details deni hai or station 
            
                        cur.execute("insert into PASSENGER values({},{},'{}',{},'{}','{}','{}','{}','{}','{}')".format(pnr,a,x,y,z,b,c,d,kp,xp))
                        conn.commit()
                else:
                    #print("Your PNR no. is: ",pnr)
                    
                    for i in range(aa):
                        print("Press Enter to Fill up the Details of Passenger",i+1)
                        x=input("Enter Name of Passenger:")
                        y=int(input("Enter age of passenger: "))
                        z=input("Enter Gender M/F/Others: ")
                        xp=cl+' '+str(random.randint(1,72))
                        #print("Your seat details are: ")
                        #print(xp)
                        #Yaha seat details deni hai or station 
                        cur.execute("insert into PASSENGER values({},{},'{}',{},'{}','{}','{}','{}','{}','{}')".format(pnr,a,x,y,z,b,c,d,kp,xp))
                        conn.commit()
                seat_update(a,kp,axe,aa,d)
                print("Yayy! Ticket Booked!",file=sys.stderr)
                print("Your PNR no. is: ",pnr)
                NAME=str(pnr)+' ticket.txt'
                cur.execute("select * from passenger where pnr=%s"%(pnr,))  #Seat details dalni hai
                dit=cur.fetchall()
                DIT=""
                for I in dit:
                    #for J in I:
                        DIT+=str(I)+'\n'
                TICKET=['|    PNR    |TRAIN_NO|    NAME    | |AGE| |SEX| | ORIGIN | |DESTINATION| |DOJ| |CLASS| |SEAT_STATUS|\n',DIT]
                ticket(NAME,TICKET)
                print("YOUR TICKET DETAILS HAS BEEN SENT TO YOUR FOLDER\n Please check your ticket for seat details :)")
                print("We wish you a happy journey :)")
                wait=input("\nPRESS A KEY TO CONTINUE\n")
                break                   
            elif pss==("CANCEL TICKET"):
                break


def cancel_reservation():
    print("|_____________RESERVATION CANCELLATION_____________|",file=sys.stderr)
    x=input("Are you sure??(yes/no) : ")
    if x=='yes' or x=='Yes' or x=='YES':
        while True:
            pnr=int(input("Please enter your 12 digit PNR no.: "))
            cur.execute("select * FROM PASSENGER WHERE PNR={}".format(pnr))
            dg=cur.fetchall()
            if len(dg)==0:
                print("CHECK YOUR PNR")
                continue
            else:

                cur.execute("delete from passenger where pnr=%s"%(pnr))
                cur.execute("delete from PAYMENT_DETAILS WHERE PNR=%s"%(pnr))
                conn.commit()
                break
        print("Cancellation successful","\nWe are sad to see you go :(")
        print("YOUR AMOUNT HAS BEEN REFUNDED TO YOUR BANK ACCOUNT")
        wait=input("\nPRESS A KEY TO CONTINUE\n")
    elif x=='no' or x=='No' or x=='NO':
        print('Cancellation Inturrupted...!!!')
        wait=input("\nPRESS A KEY TO CONTINUE\n")
    else:
        print("INVALID CHOICE",file=sys.stderr)
        wait=input("\nPRESS A KEY TO CONTINUE\n")
        cancel_reservation()
        
   
def ticketdetails():
    print("|_____________RESERVATION STATUS ENQUIRY_____________|",file=sys.stderr)
    pnr=int(input("Enter your PNR no."))
    cur.execute("select * from passenger where pnr=%s"%(pnr,))  #Seat details dalni hai
    det=cur.fetchall()
    print(det)
    wait=input("\nPRESS A KEY TO CONTINUE\n")


def pass_login():
    print("__PASSENGER PORTAL__",'\n','\n',file=sys.stderr)
    print("1. Train TimeTable")
    print("2. Reservation")
    print("3. PNR Status")
    print("4. Cancellation")
    print("5. More")
    print("6. MAIN MENU")


def fare_main():
    print("|_____________FARE ENQUIRY_____________|",file=sys.stderr)
    trn=int(input("Enter train no."))
    t='timetable_'+str(trn)
    x=input("Enter Origin: ")
    y=input("Enter Destination: ")
    print("Fare for:-",'\n','1. for 3AC','\n','2. for 2AC','\n','3. for SLEEPER','\n~','\n~')
    z=int(input("Enter choice 1-3:- "))
    try:
        cur.execute("select DISTANCE_KMS from %s where station_name='%s' or station_name='%s'"%(t,x,y))
        val=cur.fetchall()
        #print(val)
        count=[]
        for i in val:
            #print(i)
            #data=i[1]+i[0]
            #print(data)
            for j in i:
                count.append(j)
        dist=count[1]-count[0]
        if z==1:
                fr=50+(3*dist)
                print("fare for your route from",x,'to',y,'is: ',fr,'rupees for AC-THREE TIER','\n','your distance is:',dist,'kms' )
        elif z==2:
            fr=60+(5*dist)
            print("fare for your route from",x,'to',y,'is: ',fr,'rupees for AC TWO TIER','\n','your distance is:',dist,'kms' )
        elif z==3:
            fr=20+(0.5*dist)
            print("fare for your route from",x,'to',y,'is: ',fr,'rupees for SLEEPER','\n','your distance is:',dist,'kms' )
        wait=input("\nPRESS A KEY TO CONTINUE\n")
        
    except:
        print("Train no. doesn't exist",file=sys.stderr)
        wait=input("\nPRESS A KEY TO CONTINUE\n")
    #print(val)


def faredist(trn,x,y,z):
    #trn=int(input("Enter train no."))
    t='timetable_'+str(trn)
    #x=input("Enter Origin: ")
    #y=input("Enter Destination: ")
    #print(" Your Fare for:-",'\n','1. for 3AC','\n','2. for 2AC','\n','3. for SLEEPER','\n~','\n~')
    #z=input("Enter choice 1-3:- "))
    try:
        cur.execute("select DISTANCE_KMS from %s where station_name='%s' or station_name='%s'"%(t,x,y))
        val=cur.fetchall()
        #print(val)
        count=[]
        for i in val:
            #print(i)
            #data=i[1]+i[0]
            #print(data)
            for j in i:
                count.append(j)
        dist=count[1]-count[0]

    except:
        print("Train no. doesn't exist",file=sys.stderr)
        #wait=input("\nPRESS A KEY TO CONTINUE\n")
    #print(val)
    if z=='3AC':
                fr=50+(3*dist)
                return (fr,dist)
    elif z=='2AC':
        fr=60+(5*dist)
        return (fr,dist)
    elif z=='SL':
        fr=20+(0.5*dist)
        return (fr,dist)


def route():
    print("|_____________TRAIN ROUTE_____________|",file=sys.stderr)
    x=int(input("Enter train no.for route"))
    arg='timetable_'+str(x)
    cur.execute("select STATION_NAME from %s"%(arg,))
    allstn=cur.fetchall()
    cur.execute("select TRAIN_NAME from TRAIN_SCHEDULE where TRAIN_NO=%s"%(x))
    TRN=cur.fetchall()
    print("train name: ",TRN,file=sys.stderr)
    rou='START'
    for i in allstn:
        for j in i:
            rou+=' ~ '+j
    print(rou,'~ END')


def seat_availability():
    print("1. FOR ONLY AVAILABLE SEATS")
    print("2. AVAILABLE SEATS INCLUDING RAC STATUS")
    print("3. ALL STATUS")
    ch=int(input("ENTER YOUR CHOICE: "))
    cl=input("ENTER CLASS: ")
    TR=int(input("ENTER TRAIN NO.: "))
    if ch==1:
        if cl=='3AC':
            key='STATUS_'+'3AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_3AC,3AC from %s where %s='AVAILABLE'"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='2AC':
            key='STATUS_'+'2AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_2AC,2AC from %s where %s='AVAILABLE'"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='SLEEPER':
            key='STATUS_'+'SL'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_SL,Sleeper from %s where %s='AVAILABLE'"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
    elif ch==2:
        if cl=='3AC':
            key='STATUS_'+'3AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_3AC,3AC from %s where %s='AVAILABLE' or %s='RAC'"%(tab,key,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='2AC':
            key='STATUS_'+'2AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_2AC,2AC from %s where %s='AVAILABLE' or %s='RAC'"%(tab,key,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='SLEEPER':
            key='STATUS_'+'SL'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_SL,Sleeper from %s where %s='AVAILABLE' or %s='RAC'"%(tab,key,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
    elif ch==3:
        if cl=='3AC':
            key='STATUS_'+'3AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_3AC,3AC from %s"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='2AC':
            key='STATUS_'+'2AC'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_2AC,2AC from %s"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)
        elif cl=='SLEEPER':
            key='STATUS_'+'SL'
            tab='seat_availability_for_'+str(TR)
            cur.execute("select Date_of_Journey,STATUS_SL,Sleeper from %s"%(tab,key))
            det=cur.fetchall()
            print('|_DOJ_|_STATUS_|_NO._|')
            print(det)


def seat_update(a,kp,axe,aa,d):
    if kp=='3AC':
        if axe=='AVAILABLE':
             cur.execute("UPDATE seat_availability_for_{} set 3AC=3AC-{} WHERE Date_Of_Journey='{}' ".format(a,aa,d))
        elif axe=='RAC':
            cur.execute("UPDATE seat_availability_for_{} set 3AC=3AC+{} WHERE Date_Of_Journey='{}'".format(a,aa,d))
    elif kp=='2AC':
        if axe=='AVAILABLE':
             cur.execute("UPDATE seat_availability_for_{} set 2AC=2AC-{} WHERE Date_Of_Journey='{}' ".format(a,aa,d))
        elif axe=='RAC':
            cur.execute("UPDATE seat_availability_for_{} set 2AC=2AC+{} WHERE Date_Of_Journey='{}'".format(a,aa,d))
    elif kp=='SL':
        if axe=='AVAILABLE':
            cur.execute("UPDATE seat_availability_for_{} set SLEEPER=SLEEPER-{} WHERE Date_Of_Journey='{}' ".format(a,aa,d))        
        elif axe=='RAC':
            cur.execute("UPDATE seat_availability_for_{} set SLEEPER=SLEEPER+{} WHERE Date_Of_Journey='{}'".format(a,aa,d))
    conn.commit()


def ticket(x,y):
    f=open(x,'w')
    f.writelines(y)
    f.close()

