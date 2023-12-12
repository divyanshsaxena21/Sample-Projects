import mysql.connector as ms
import random
cn=ms.connect(host="localhost", user="root" ,passwd="kanpur",auth_plugin='mysql_native_password' )
cs=cn.cursor()
print("*********************** W E L C O M E ************************** ")
print(" \t\t\t  TO  THE")  
print("\t\tRAILWAYS RESERVATION SYSTEM")
print()
print(" D E V E L O P E D  B Y :")
print(" HARSHIT & DIVYANSH")
print(" XII - A")
print(" AIR FORCE SCHOOL")
print()

cs.execute("create database if not exists Railway") 
cs.execute("use Railway")
cs.execute("create table if not exists passengers(pid varchar(20) primary key,First_name varchar(30),Last_name varchar(20), age varchar(5),gender varchar(10))")
cs.execute("create table if not exists booking(pid varchar(20) references passengers(pid),pnr varchar(30) primary key,train_name varchar(20),boarding varchar(20),destination varchar(20),fare varchar(20))")
while True:
    print(" 1- FOR INSTRUCTIONS")
    print(" 2- ADD PASSENGERS DETAILS")
    print(" 3- TO EDIT PASSENGERS DETAILS")
    print(" 4- CREATE TABLE TRAIN DETAILS")
    print(" 5- TO SHOW ALL TRAIN DETAILS")
    print(" 6- TO SHOW ALL PASSENGERS DETAILS")
    print(" 7- RESERVATION OF TICKET")
    print(" 8- CANCEL THE RESERVATION")
    print(" 9- DISPLAY THE TICKET OF PASSENGER")
    print(" 10- EXIT")

    #MENU()

    def introduction():     #choice 1
        intro = '''
        ------------------------------------------------------------------------------------------------------
                  W E L C O M E    T O      I N D I A N     R A I L W A Y S
        -------------------------------------------------------------------------------------------------------
                    
        WELCOME TO THE INDIAN RAILWAYS. WE PROVICE YOU FACILITY TO BOOK YOUR SEATS
        IN FOLLOWING CATEGORIES: 
            COACHES                
        ****************           
             SLEEPER
             SECOND AC
             FIRST AC
       # THE GST IS APPLICABLE ON THE BOOKING AMOUTNT AS PER GOVERNMENT GUIDLINES. 
       # IN CASE OF CANCELLATION OF TICKETS THE CANCELLATION CHARGES ARE APPLICABLE
         AS PER THE GOVERNMENT GUIDLINES.
       # FOOD CHARGES ARE EXTRA THEN TICKET CHARGES AND HAVE TO BE PAID IN CASH. 
         LIST OF FOOD AVAILABLE :-
             1. VEGITERIAN       : 300/- PER THALI
             2. NON-VEGITERIAN   : 400/- PER THALI
        ---------------------------------------------------------------------------'''
        print(intro)
    

    def add_pasdetails():   #choice 2
        pid=input("Enter Passenger Id: ")
        Fname=input("Enter passenger's first name: ")
        Lname=input("Enter passenger's last name: ")
        gender=input("Enter gender: ")
        age=input("Enter passenger's age: ")
        cs.execute("insert into passengers values('"+pid+"','"+Fname+"','"+Lname+"','"+age+"','"+gender+"')")
        cn.commit()
        print("Record inserted")

    def edit_pndetails():   #choice 3
        ch="y"
        while ch.lower()=="y":
            i=input("Enter PID whose details you want to change: ")
            c=input("Enter the field in which you want to make changes(First Name/Last Name/Gender/Age): ")
            if c.lower()=="first name":
                cs.execute("select first_name from passengers where pid=('"+i+"')")
                for k in cs:
                    print("Old name is","\t".join(k))
                n=input("Enter the new name: ")
                cs.execute("update passengers set first_name='"+n+"' where pid='"+i+"'")
                cn.commit()
                print("record updated")
                ch=input("Do you want to change anything else? Y/N")
            elif c.lower()=="last name":
                cs.execute("select last_name from passengers where pid=('"+i+"')")
                for k in cs:
                    print("Old name is","\t".join(k))
                n=input("Enter the new name: ")
                cs.execute("update passengers set last_name='"+n+"' where pid='"+i+"'")
                cn.commit()
                print("record updated")
                ch=input("Do you want to change anything else? Y/N")
            elif c.lower()=="gender":
                cs.execute("select gender from passengers where pid=('"+i+"')")
                for k in cs:
                    print("Old gender is","\t".join(k))
                n=input("Enter the new gender: ")
                cs.execute("update passengers set gender='"+n+"' where pid='"+i+"'")
                cn.commit()
                print("record updated")
                ch=input("Do you want to change anything else? Y/N")
            elif c.lower()=="age":
                cs.execute("select age from passengers where pid=('"+i+"')")
                for k in cs:
                    print("Old age is","\t".join(k))
                n=input("Enter the new age: ")
                cs.execute("update passengers set age='"+n+"' where pid='"+i+"'")
                cn.commit()
                print("record updated")
                ch=input("Do you want to change anything else? Y/N")
            else:
                print("Wrong input")
            
            

    def create_traindetails():     #choice 4
        cs.execute("create table if not exists traindetails(tname varchar(30),tnum varchar(10) primary key,Starting_point varchar(25),Ending_Point varchar(30),AC1_fare varchar(5),AC2_fare varchar(5),sleeper_fare varchar(5) )")
        tname="Royal Express"
        tnumber="22468"
        S="Mumbai"
        D="Kolkata"
        AC1='5000'
        AC2='4000'
        Sleeper='3000'
        cs.execute("insert into traindetails values('"+tname+"','"+tnumber+"','"+S+"','"+D+"','"+AC1+"','"+AC2+"','"+Sleeper+"')")
        cn.commit()
        tname="Jammu Tavi"
        tnumber="12469"
        S="Kanpur"
        D="Jammu"
        AC1='7000'
        AC2='6000'
        Sleeper='5000'
        cs.execute("insert into traindetails values('"+tname+"','"+tnumber+"','"+S+"','"+D+"','"+AC1+"','"+AC2+"','"+Sleeper+"')")
        cn.commit()
        print("Table created")
        
    def show_traindetails():   #choice 5
        print("ALL TRAINS DETAILS")
        print("Train_Name\t\tTrain_Number\tStarting\tEnding point\tAC1-Fare\tAC2-Fare\tSleeper-Fare")
        cs.execute("select * from traindetails")
        for i in cs:
            print("\t\t".join(i))


    def showpasdetails():   #choice 6
        print("ALL PASSENGERS DETAILS")
        print("PID\t\tFirst_Name\tLast_Name\tAge\t\tGender")
        cs.execute("select * from passengers")
        for i in cs:
            print('\t\t'.join(i))
        
    def ticketreservation():   #choice 7
        print("WE HAVE FOLLOWING TYPES OF SEATS FOR YOU")
        print("Press 1 for ROYAL EXPRESS from kanpur:-")
        print()
        print("1. FIRST CLASS AC RS 5000 Per PERSON")
        print("2. SECOND CLASS AC RS 4000 Per PERSON")
        print("3. FOR SLEEPER RS 3000 Per PERSON")
        print()
        print("Press 2 for JAMMU TAVI EXPRESS from New Delhi:-")
        print()
        print("1. FIRST CLASS AC RS 7000 per PERSON")
        print("2. SECOND CLASS AC RS 6000 per PERSON")
        print("3. FOR SLEEPER RS 5000 per PERSON")

        pid=input("Please Enter your passenger ID: ")
        pid=str(pid)
        tname=int(input("Enter your choice of train please ->"))
        if tname==1:
            print("ROYAL EXPRESS")
            a,b='NULL','NULL'
            a=input("Enter the Boarding station of your Journey: ")
            b=input("Enter the destination of your Journey: ")
            x=int(input("Enter your choice of ticket class please ->"))
            n=int(input("How many tickets you need:  "))
            if x==1:
                print("You have chosen FIRST CLASS ticket")
                s=5000*n
            elif x==2:
                print("You have chosen SECOND CLASS ticket")
                s=4000*n
            elif x==3:
                print("You have chosen SLEEPER ticket")
                s=3000*n
            else:
                print("Invalid option")
                
        elif tname==2:
            print("JAMMU TAVI EXPRESS")
            a,b='NULL','NULL'   
            a=input("Enter the Boarding station of your Journey: ")
            b=input("Enter the destination of your Journey: ")
            x=int(input("Enter your choice of ticket class please ->"))
            n=int(input("How many tickets you need:  "))
            if x==1:
                print("You have chosen FIRST CLASS ticket")
                s=7000*n
            elif x==2:
                print("You have chosen SECOND CLASS ticket")
                s=6000*n
            elif x==3:
                print("You have chosen SLEEPER ticket")
                s=5000*n
            else:
                print("Invalid option")
        print("Do you want food service? ")

        fd=input(" Y/N: ")
        while fd in('Y','y'):
            vg=input('Do you want Veg/Non-Veg Thali: ')
            if vg.lower()=="veg":
                s=s+300
                print("Your total price is=",s,"\n")
            elif vg.lower()=="non-veg":
                s=s+400
                print("Your total price is=",s,"\n")
            print("Do you wnt more thatli")
            fd=input("Y/N")
        else:
            print("Ticket Booked") 
            print("Your total price is=",s,"\n")

        pnr=random.randint(100000,1000000)
        print("\t******NOTICE----Please remember the following pnr number for further process: ",pnr,"******")
        print("\n\n")
        pnr=str(pnr)
        s=str(s)
        
        if tname==1:
            tname=("Royal Express")
        elif tname==2:
            tname=("Jammu Tavi")
        cs.execute("insert into booking values('"+pid+"','"+pnr+"','"+tname+"','"+a+"','"+b+"','"+s+"')")
        cn.commit()
        print("P_ID\t\tPNR\t\tTrain_Name\t\tBoarding\t\tDestination\tFare")
        cs.execute("select * from booking where pnr=('"+pnr+"')")
        for i in cs:
            print('\t\t'.join(i))
        
    def cancel():   #choice 8
        n=input("Enter pnr no. of cancelling passenger's reservation: ")
        cs.execute("delete from booking where pnr='"+n+"'")
        cn.commit()
        print("P_ID\t\tPNR\t\tTrain_Name\t\tSource\t\tDestination\tFare")
        cs.execute("select * from booking")
        for i in cs:
            print("\t\t".join(i))

            
    def showbooking():  #choice 9
        n=input("Enter the pnr number whose ticket you want to search: ")
        cs.execute("select * from booking where pnr=('"+n+"')")
        print("P_ID\t\tPNR\t\tTrain_Name\t\tBoarding\tDestination\tFare")
        for i in cs:
            print('\t\t'.join(i))
    

    n=int(input("Enter your choice:  "))
    #main
    if n==1:
        introduction()
    elif n==2:
       add_pasdetails()
    elif n==3:
        edit_pndetails()
    elif n==4:
        create_traindetails()
    elif n==5:
        show_traindetails()
    elif n==6:
        showpasdetails()
    elif n==7:
         ticketreservation()
    elif n==8:
        cancel()
    elif n==9:
        showbooking()
    elif n==10:
        break
    else:
        print("Wrong choice!!")


