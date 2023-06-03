import mysql.connector as x
import datetime

con=x.connect(host="localhost",user="root",passwd="12345",database="bank")

def openAcc():
    while True:   
        n=input("Enter Name: ")
        sql3="SELECT count(name) FROM account where accno=%s"
        data=(n,)
        c=con.cursor()
        c.execute(sql3,data)
        myresult=c.fetchone()
        if myresult[0]!=0:
            print(" The given name has been already registered ")
        else:
            print(" The given name has been accepted")
            break

    while True:   
        ac=input("Enter Account No (no. must consist 10 numbers) : ")
        sql3="SELECT count(accno) FROM account where accno=%s"
        data=(ac,)
        c=con.cursor()
        c.execute(sql3,data)
        myresult=c.fetchone()
        if ac.isnumeric():
    
            if len(ac)!=10:
                print("account number is Invalid")
            else:
                if myresult[0]!=0:
                    print(" Account number has been already taken or unavailable")
                else:
                    print(" Account number has been accepted")
                    break
                
        else:
            print("Enter dights only")
        

    while True:
        db = input("Enter date of birth (YYYY-MM-DD): ")
        try:
            year, month, day = map(int, db.split('-'))
            date_of_birth = datetime.date(year, month, day)
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

    print("Date of Birth:", date_of_birth.strftime('%Y-%m-%d'))
    

    while True:
        p=input("Enter Phone: ")
        if p.isnumeric():
    
            if len(p)!=10:
                print("Mobile number is Invalid")
            else:
                break
        else:
            print("Enter dights only")

    while True:
        ob=int(input("Enter opening Balance: "))
    
        if ob<=0:
            print("Invalid(Opening Balance should be greater that zero)")
        else:
            break
        

    
    data1=(n,ac,db,p,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data entered successfully")
    main()


def depoAmo():
    am=int(input("Enter Amount: "))
    ac=input("Enter Account No: ")
    a="select bal from amount where accno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set bal =%s  where accno=%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    main()

def witham():
    am=int(input("Enter Amount: "))
    ac=input("Enter Account No: ")
    a="select bal from amount where accno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    if tam>=0:
        sql="update amount set bal =%s  where accno=%s"
        d=(tam,ac)
        c.execute(sql,d)
        con.commit()
        main()
    else:
        print("Insufficient Balance")

def balance():
    ac=input("Enter Account No: ")
    a="select bal from amount where accno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for account: ",ac,"is ",myresult[0])
    main()


def dispacc():
    
    ac = input("Enter Account No: ")
    
    a = "SELECT bal FROM amount WHERE accno = %s"
    b = "SELECT name FROM account WHERE accno = %s"
    c = "SELECT dob FROM account WHERE accno = %s"
    d = "SELECT ph FROM account WHERE accno = %s"
    data = (ac,)
    
    cursor = con.cursor()

    cursor.execute(b, data)
    name = cursor.fetchone()
    print("Name: ", name[0])  

    cursor.execute(a, data)
    balance = cursor.fetchone()
    print("Balance: ", balance[0]) 
    
    cursor.execute(c, data)
    dob = cursor.fetchone()
    print("Date of Birth: ", dob[0])  

    cursor.execute(d, data)
    phno = cursor.fetchone()
    print("Phone number:", phno[0])  

    cursor.close()
    con.close()

    main()



def closeac():
    ac=input("Enter Account No: ")
    sql1="delete from account where accno=%s"
    sql2="delete from account where accno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()

def main():
    print("-----------BANK MANAGEMENT SYSTEM-----------") 
    print("""
    1.OPEN NEW ACCOUNT 
    2.DEPOSIT AMOUNT 
    3.WITHDRAW CASH
    4.BALANCE ENQUIRY 
    5.DISPLAY CUSTOMER DETIALS
    6.CLOSE ACCOUNT 
    """)
    choice=input("Enter Task no: ")
    if(choice=='1'):
       openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        witham()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeac()
    else:
        print("Wrong choice...")
        
main()
