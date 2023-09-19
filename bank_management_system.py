import sqlite3
import random
from accounts import Account

conn=sqlite3.connect('Bank.db')
cur=conn.cursor()

def check_if_exists(accountNo):
    cur.execute("SELECT AccountNo FROM ACCOUNTS")
    data=list(cur.fetchone())
    if accountNo in data:
        return True
    else:
        return False

#Delete the existing database and uncomment the following lines (and run the code) to create a fresh database!
#cur.execute("""CREATE TABLE ACCOUNTS(accountNo int primary key,fname text,lname text,bal integer)""")
#conn.commit()

while True:
    print("Welcome to ABC Bank!")
    print("==MENU==")
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Account Summary\n5. Display all Accounts\n6. Exit")
    choice=int(input("Please enter your choice: "))
    if choice==1:
        fname=input("Please enter first name: ")
        lname = input("Please enter last name: ")
        accNo=0
        while True:
            try:
                accountNo=random.randint(1,1000)
                query="INSERT INTO ACCOUNTS VALUES(?,?,?,0)"
                params=(accountNo,fname,lname)
                cur.execute(query,params)
                conn.commit()
                accNo=accountNo
                break
            except:
                pass
        print("Account created successfully!")
        print(f"Your Account Number is {accNo}")
    elif choice==2:
        accountNo=int(input("Enter the account number: "))
        if not check_if_exists(accountNo):
            print("Account not Found!")
            continue
        val=int(input("Enter the amount to deposit: "))
        query="UPDATE ACCOUNTS SET bal=bal+? WHERE accountNo=?"
        params=(val,accountNo)
        cur.execute(query,params)
        conn.commit()
    elif choice==3:
        accountNo = int(input("Enter the account number: "))
        if not check_if_exists(accountNo):
            print("Account not Found!")
            continue
        val = int(input("Enter the amount to withdraw: "))
        query = "SELECT * FROM ACCOUNTS WHERE accountNo=?"
        params = (accountNo,)
        cur.execute(query,params)
        bal=cur.fetchone()[-1]
        if val>bal:
            print("Not enough balance in the account!")
            continue
        query="UPDATE ACCOUNTS SET bal=bal-? WHERE accountNo=?"
        params=(val,accountNo)
        cur.execute(query,params)
        conn.commit()
    elif choice==4:
        accountNo=int(input("Enter Account Number: "))
        if not check_if_exists(accountNo):
            print("Account not Found!")
            continue
        query="SELECT * FROM ACCOUNTS WHERE accountNo=?"
        params=(accountNo,)
        cur.execute(query,params)
        data=cur.fetchone()
        print(f"""Account Number: {data[0]}\nCustomer Name: {data[1]} {data[2]}\nBalance: {data[3]}""")
    elif choice==5:
        cur.execute("SELECT * FROM ACCOUNTS")
        data = cur.fetchall()
        for i in data:
            print(f"Account Number: {i[0]}, Name: {i[1]} {i[2]}, Balance: {i[3]}")
    elif choice==6:
        break
    else:
        print("Please enter a valid choice!")

print("Thank you!")
conn.close()