from tkinter import *
import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox as MessageBox
import datetime
import math
import os
App = Tk()
App.geometry("1900x1000")
App.title("login")
us1=StringVar()
pw1=StringVar()
label_login = Label(App,text="INVENTORY MANAGEMENT SYSTEM",relief=SOLID,padx=410,pady=12,font=('bold',40)).pack()       
def login():
    if us1.get() == '' and pw1.get()=='':
        k=Label(App,text='Please enter your username and password',font=('Bold', 15),fg='red',bg="white").place(x=900,y=310)
        print("//////")
        

    elif us1.get()== 'vikas' and pw1.get()=='vikas':
        
        i=Label(App,text='Login success',font=('Bold', 15),fg='blue',bg="white").place(x=900,y=310)
        print("login success")
        main = tk.Tk()
        main.title("inventory management system/home" )
        main.geometry("1960x1080")
##        main.configure(bg="blue")
        TopFrame = Frame(main,width=1980,height=100,bd = 15,relief = "raise",bg="red").pack(side=TOP)

        lblTitle = Label(main,TopFrame,text="INVENTORY MANAGEMENT SYSTEM",font=("Times New Roman",30),bg='blue',relief=SOLID,padx=410,pady=12,fg="black" ).place(x=7,y=10)
        photo1 = PhotoImage(file="bg.png")
##====================================================HELP========================================================================
        def help():

                win1 = tk.Toplevel()
                win1.geometry("1000x500")
                win1.configure(bg="blue")
                win1.title("INVENTORY MANAGEMENT SYSTEM/HELP")
                win1.resizable(0,0)
                L1 = Label(win1,text="Inventory management software is made "
                           "\nup of several key components working together to create"
                           "\na cohesive inventory of many organization's systems.\n",font=("times",20),bg="blue",fg="white",relief=SOLID,padx=100,pady=100).pack(pady=50)             
##==========================================================inventory page2=================================================================
        def stock(): 
            def ADD():
                    id = e_id.get()
                    product_name = e_product_name.get();
                    stock =e_stock.get();
                    cost_pr = e_cp.get();
                    selling_pr = e_sp.get();
                    vendor_name = e_vendor_name.get();
                    vendor_ph = e_vendor_ph.get();
                    total_sp = e_total_sp.get();
                    total_cp = e_total_cp.get();
                    profit = e_profit.get();
            
            
             

                    if(id =="" or product_name=="" or stock=="" or cost_pr =="" or selling_pr =="" or vendor_name==""or vendor_ph==""or total_cp==""or total_sp==""or profit==""):
                        MessageBox.showinfo("Insert status","all field are required")
                    else:
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        cursor = conn.cursor()
                        cursor.execute("insert into sales values('"+ id +"','"+ product_name +"','"+stock+"','"+cost_pr+"','"+selling_pr+"','"+vendor_name+"','"+vendor_ph+"','"+total_cp+"','"+total_sp+"','"+profit+"')")
                        cursor.execute("commit");

                
                        e_id.delete(0,'end') 
                        e_product_name.delete(0,'end')
                        e_stock.delete(0,'end')
                        e_cp.delete(0,'end')
                        e_sp.delete(0,'end')
                        e_vendor_name.delete(0,'end')
                        e_vendor_ph.delete(0,'end')
                        e_total_sp.delete(0,'end')
                        e_total_cp.delete(0,'end')
                        e_profit.delete(0,'end')
                        show()
                        MessageBox.showinfo("Insert status","Inserted succesfully");
                        conn.close();


            def delete():
                    if (e_id.get ==""):
                        MessageBox.showinfo("Delete status","Id is compulsory for delete")
                    else:
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        cursor = conn.cursor()
                        cursor.execute("delete from sales where id='"+e_id.get()+"'") 
                        cursor.execute("commit");
                        MessageBox.askokcancel("are you sure ","OK or Cancel")
                
                        e_id.delete(0,'end') 
                        e_product_name.delete(0,'end')
                        e_stock.delete(0,'end')
                        e_cp.delete(0,'end')
                        e_sp.delete(0,'end')
                        e_vendor_name.delete(0,'end')
                        e_vendor_ph.delete(0,'end')
                        e_total_sp.delete(0,'end')
                        e_total_cp.delete(0,'end')
                        e_profit.delete(0,'end')
                       
                        show()
                        MessageBox.showinfo("Insert status","deleted successfully");
                        conn.close();

            def update():
                    id = e_id.get()
                    product_name = e_product_name.get();
                    stock =e_stock.get();
                    cost_pr = e_cp.get();
                    selling_pr = e_sp.get();
                    vendor_name = e_vendor_name.get();
                    vendor_ph = e_vendor_ph.get();
                    total_sp = e_total_sp.get();
                    total_cp = e_total_cp.get();
                    profit = e_profit.get();
            

                    if(id =="" or product_name=="" or stock=="" or cost_pr =="" or selling_pr =="" or vendor_name==""or vendor_ph==""or total_cp==""or total_sp==""or profit==""):
                        MessageBox.showinfo("Insert status","all field are required")
                    else:
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        cursor = conn.cursor()
                        cursor.execute("update sales set product_name='"+product_name+"',stock='"+stock+"',cp='"+cost_pr+"',sp='"+selling_pr+"',vendor_name='"+vendor_name+"',vendor_ph='"+vendor_ph+"',total_cp='"+total_cp+"',total_sp='"+total_sp+"',profit='"+profit+"' where id='"+id+"'")
                        cursor.execute("commit");

                
                        e_id.delete(0,'end') 
                        e_product_name.delete(0,'end')
                        e_stock.delete(0,'end')
                        e_cp.delete(0,'end')
                        e_sp.delete(0,'end')
                        e_vendor_name.delete(0,'end')
                        e_vendor_ph.delete(0,'end')
                        e_total_sp.delete(0,'end')
                        e_total_cp.delete(0,'end')
                        e_profit.delete(0,'end')
                
                        show()
                        MessageBox.showinfo("update status","update succesfully");
                        conn.close();
            def get():
                    if (e_id.get ==""):
                        MessageBox.showinfo("Delete status","Id is compulsory for delete")
                    else:
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        cursor = conn.cursor()
                        cursor.execute("select * from sales where id='"+e_id.get()+"'") 
                        rows = cursor.fetchall()

                        for row in rows:
                            e_product_name.insert(0,row[1])
                            e_stock.insert(0,row[2])
                            e_cp.insert(0,row[3])
                            e_sp.insert(0,row[4])
                            e_vendor_name.insert(0,row[5])
                            e_vendor_ph.insert(0,row[6])
                            e_total_sp.insert(0,row[7])
                            e_total_cp.insert(0,row[8])
                            e_profit.insert(0,row[9])    

                        conn.close();
            def show():
                    conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                    cursor = conn.cursor()
                    cursor.execute("select * from sales") 
                    rows = cursor.fetchall()
                    list.delete(0, list.size())

                    for row in rows:
                        insertData = str(row[0])+'                           '+str(row[1])+'                           '+str(row[2])+'                                   '+str(row[3])+'                              '+str(row[4])+'                              '+str(row[5])+'                                 '+str(row[6])+'                                '+str(row[7])+'                              '+str(row[8])+'          '+str(row[9])#+'   '+str(row[4])+'    '+str(row[4])
               
                        list.insert(list.size()+1,insertData)
                    conn.close();
            root = Tk()
            root.geometry("1900x1000")
            root.title("")
            win_title = Label(root,text="Stock Management",font=("arial 20 bold"),bg="red",relief=SOLID,padx=640,fg="white").pack()
            
            root.configure(bg="blue")
            Id  = Label(root, text="Product Id",font=("bold",12),bg="blue",fg="white")
            Id.place(x=30,y=550)

            product_name  = Label(root, text="Product name",font=("bold",12),bg="blue",fg="white")
            product_name.place(x=30,y=590)

            stock  = Label(root, text="Product quantity",font=("bold",12),bg="blue",fg="white")
            stock.place(x=30,y=630)
            
            cost_price  = Label(root, text="Cost price",font=("bold",12),bg="blue",fg="white")
            cost_price.place(x=30,y=670)

            selling_price = Label(root, text="Selling price",font=("bold",12),bg="blue",fg="white")
            selling_price.place(x=30,y=710)

            vendor_name  = Label(root, text="Vendor name",font=("bold",12),bg="blue",fg="white")
            vendor_name.place(x=400,y=550)

            vendor_ph  = Label(root, text="Vendor phone",font=("bold",12),bg="blue",fg="white")
            vendor_ph.place(x=400,y=590)

            total_cp  = Label(root, text="Total cost price",font=("bold",12),bg="blue",fg="white")
            total_cp.place(x=400,y=630)

            total_sp  = Label(root, text="Total selling price",font=("bold",12),bg="blue",fg="white")
            total_sp.place(x=400,y=670)

            profit  = Label(root, text="Profit",font=("bold",12),bg="blue",fg="white")
            profit.place(x=400,y=710)



            e_id = Entry(root,font=("bold",12),bd=5)
            e_id.place(x=160,y=550)
            e_id.focus()

            e_product_name = Entry(root,font=("bold",12),bd=5)
            e_product_name.place(x=160,y=590)

            e_stock = Entry(root,font=("bold",12),bd=5)
            e_stock.place(x=160,y=630)

            e_cp = Entry(root,font=("bold",12),bd=5)
            e_cp.place(x=160,y=670)

            e_sp = Entry(root,font=("bold",12),bd=5)
            e_sp.place(x=160,y=710)

            e_vendor_name = Entry(root,font=("bold",12),bd=5)
            e_vendor_name.place(x=550,y=550)

            e_vendor_ph = Entry(root,font=("bold",12),bd=5)
            e_vendor_ph.place(x=550,y=590)

            e_total_cp = Entry(root,font=("bold",12),bd=5)
            e_total_cp.place(x=550,y=630)

            e_total_sp = Entry(root,font=("bold",12),bd=5)
            e_total_sp.place(x=550,y=670)

            e_profit = Entry(root,font=("bold",12),bd=5)
            e_profit.place(x=550,y=710)


            insert = Button(root,text="INSERT",font=("italic 12 bold"),bg="white",command=ADD,width=28,bd=4)
            insert.place(x=800,y=550)

            delete = Button(root,text="DELETE",font=("italic 12 bold"),bg="white",command=delete,width=28,bd=4)
            delete.place(x=800,y=650)

            update = Button(root,text="UPDATE",font=("italic 12 bold"),bg="white",command=update,width=28,bd=4)
            update.place(x=800,y=600)

            get = Button(root,text="GET",font=("italic 12 bold"),bg="white",command=get,width=28,bd=4)
            get.place(x=800,y=700)


            l1 = Label(root,text="ID",font=("italic",10),bg="blue",fg="white")
            l1.place(x=40,y=40)

            l2 = Label(root,text="NAME",font=("italic",10),bg="blue",fg="white")
            l2.place(x=140,y=40)

            l3 = Label(root,text="QUANTITY",font=("italic",10),bg="blue",fg="white")
            l3.place(x=290,y=40)

            l4 = Label(root,text="COST PRICE",font=("italic",10),bg="blue",fg="white")
            l4.place(x=430,y=40)

            l5 = Label(root,text="SELLING PRICE",font=("italic",10),bg="blue",fg="white")
            l5.place(x=580,y=40)

            l6 = Label(root,text="VENDOR NAME",font=("italic",10),bg="blue",fg="white")
            l6.place(x=720,y=40)

            l7 = Label(root,text="VENDOR PHONE",font=("italic",10),bg="blue",fg="white")
            l7.place(x=900,y=40)

            l8 = Label(root,text="TOTAL COS.PRICE",font=("italic",10),bg="blue",fg="white")
            l8.place(x=1070,y=40)

            l9 = Label(root,text="TOTAL SEL.PRICE",font=("italic",10),bg="blue",fg="white")
            l9.place(x=1260,y=40)

            l10 = Label(root,text="PROFIT",font=("italic",10),bg="blue",fg="white")
            l10.place(x=1420,y=40)


            Exit_btn = Button(root,text="EXIT",font=("italic 12 bold"),width=10,command=root.destroy,height=2,bg="red")
            Exit_btn.place(x=1200,y=650)
            list = Listbox(root,width = 162,height=22,font=("arial 12 bold"),bd=5)

            list.place(x=30,y=60)
            show()
####=================================================view product========================================================+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
        def search_now():
                    root = Tk()
                    root.geometry("1900x1000")
                    root.title("search window")
                    root.configure(bg="blue")
                    win_title = Label(root,text="Search For Inventory Items Here",font=("arial 20 bold"),bg="red",relief=SOLID,padx=650,fg="white").pack()
                    def search_list():
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        cursor = conn.cursor()
                        cursor.execute("select * from sales where id='"+search_e.get()+"'") 
                        rows = cursor.fetchall()
                        list.delete(0, list.size())

                        for row in rows:
                            insertData = str(row[0])+'                           '+str(row[1])+'                           '+str(row[2])+'                                   '+str(row[3])+'                              '+str(row[4])+'                              '+str(row[5])+'                                 '+str(row[6])+'                                '+str(row[7])+'                              '+str(row[8])+'                           '+str(row[9])#+'   '+str(row[4])+'    '+str(row[4])
                            list.insert(list.size()+1,insertData)


                            search_e.delete(0,'end')
                        conn.close();


                    search_e = Entry(root,font=(15),bd=5)
                    search_e.place(x=40,y=500,w=400,h=40)


                    l1 = Label(root,text="ID",font=("italic",10),bg="blue",fg="white")
                    l1.place(x=40,y=40)

                    l2 = Label(root,text="NAME",font=("italic",10),bg="blue",fg="white")
                    l2.place(x=140,y=40)

                    l3 = Label(root,text="QUANTITY",font=("italic",10),bg="blue",fg="white")
                    l3.place(x=290,y=40)

                    l4 = Label(root,text="COST PRICE",font=("italic",10),bg="blue",fg="white")
                    l4.place(x=430,y=40)

                    l5 = Label(root,text="SELLING PRICE",font=("italic",10),bg="blue",fg="white")
                    l5.place(x=580,y=40)

                    l6 = Label(root,text="VENDOR NAME",font=("italic",10),bg="blue",fg="white")
                    l6.place(x=720,y=40)

                    l7 = Label(root,text="VENDOR PHONE",font=("italic",10),bg="blue",fg="white")
                    l7.place(x=900,y=40)

                    l8 = Label(root,text="TOTAL COS.PRICE",font=("italic",10),bg="blue",fg="white")
                    l8.place(x=1070,y=40)

                    l9 = Label(root,text="TOTAL SEL.PRICE",font=("italic",10),bg="blue",fg="white")
                    l9.place(x=1260,y=40)

                    l10 = Label(root,text="PROFIT",font=("italic",10),bg="blue",fg="white")
                    l10.place(x=1420,y=40)


                    list= Listbox(root,width=162,height=20,font=("arial 12 bold"))
                    list.place(x=30,y=60)
                    search_btn = Button(root,text="SEARCH ",font=("arial 13 bold"),command=search_list,width=10,bd=5)
                    search_btn.place(x=450,y=500)
                    
                    Exit_btn = Button(root,text="EXIT",font=("italic 12 bold"),width=10,command=root.destroy,bg="red")
                    Exit_btn.place(x=50,y=600,h=50)
##====================================================================================================================================________________________++++++++++++++++++++++++++

        products_list = []        
        product_price = []
        product_quantity = []
        product_id = []
        class Application:
                    def __init__(self,master,*args,**kwargs):
                        
                        self.left = Frame(master,width=800,height=800,bg="red",bd=8)
                        self.left.pack(side=LEFT)

                        self.right = Frame(master,width=1000,height=800,bg="blue")
                        self.right.pack(side=RIGHT)


                        self.heading = Label(self.left,text="Sales",bg="red",font=("arial 40 bold") )
                        self.heading.place(x=10,y=0)

                        self.date_1 = Label(self.right,text="Today's Date: " + str(datetime.datetime.now()),font=("arial 15 bold"),bg="blue",fg="white")
                        self.date_1.place(x=0,y=0)

                        ####=================================================================
                        self.tproduct = Label(self.right,text="Product",font=("arial 18 bold"),fg="white",bg="blue")
                        self.tproduct.place(x=0,y=60)
                        
                        self.tquantity = Label(self.right,text="Quantity",font=("arial 18 bold"),fg="white",bg="blue")
                        self.tquantity.place(x=230,y=60)
                        
                        self.tamount = Label(self.right,text="Amount",font=("arial 18 bold"),fg="white",bg="blue")
                        self.tamount.place(x=500,y=60)



                        ####===========================================
                        self.enter_id = Label(self.left,text="Enter Product Id",bg="red",font=("arial 20 bold"))
                        self.enter_id.place(x=0,y=90)

                        self.enteride = Entry(self.left,width=25,bd=4,font=("arial 15 bold"))
                        self.enteride.place(x=240,y=90)

                        self.search_btn = Button(self.left,text="SEARCH",bd=3,command = self.ajax,width=15,fg="white",height=1,bg="blue",font=("arial 12 bold"))
                        self.search_btn.place(x=540,y=90)

                        self.productname = Label(self.left,text="",font=("arial 18 bold"),bg="red")
                        self.productname.place(x=0,y=250)
                        
                        self.pprice = Label(self.left,text="",font=("arial 18 bold"),bg="red")
                        self.pprice.place(x=0,y=290)

                        ##toatal label

                        self.total_l = Label(self.right,text="",font=("arial 30 bold"),bg="blue",fg="white")
                        self.total_l.place(x=0,y=600)
                    def ajax(self,*args,**kwargs):
                        self.get_id = self.enteride.get();
                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        c = conn.cursor()
                        result= c.execute("select * from sales where id='"+self.get_id+"'")
                        result = c.fetchall()
                        for self.r  in  result:
                            self.get_id = self.r[0]
                            self.get_product_name = self.r[1]
                            self.get_price = self.r[4]
                            self.get_stock = self.r[2]
                        self.productname.configure(text="Product name: " + str(self.get_product_name))
                        self.pprice.configure(text="Price: " + str(self.get_price))

                        #create the quantity label

                        self.quantity_l = Label(self.left,text="Enter Quantity",font=("arial 18 bold"),bg="red")
                        self.quantity_l.place(x=0,y=370)

                        
                        self.quantity_e = Entry(self.left,bd=4, width=20,font=("arial 18 bold"))
                        self.quantity_e.place(x=190,y=370)
                    # create discount 
                        self.discount_l = Label(self.left,text="Enter Discount",font=("arial 18 bold"),bg="red")
                        self.discount_l.place(x=0,y=420)
                        

                        
                        self.discount_e = Entry(self.left, width=20,bd=4,font=("arial 18 bold"))
                        self.discount_e.place(x=190,y=420)
                        self.discount_e.insert(END,0)

                        self.add_to_cart = Button(self.left,text="ADD TO CART",bd=4,fg="white",command=self.add_to_cart,width=18,bg="blue",height=1,font=("arial 12 bold"))
                        self.add_to_cart.place(x=480,y=420)
                        #change label
                        self.change_l = Label(self.left,text="Given amount",font=("arial 18 bold"),bg="red")
                        self.change_l.place(x=0,y=520)
                        self.change_e = Entry(self.left, width=20,bd=4,font=("arial 18 bold"))
                        self.change_e.place(x=190,y=520)
                        self.change_btn = Button(self.left,text="CALCULATE CHANGE",bd=4,fg="white",command=self.change_func,width=20,bg="blue",height=1,font=("arial 12 bold"))
                        self.change_btn.place(x=480,y=520)
                        self.bill_btn = Button(self.left,text="BILL",command=self.generate_bill,fg="white",width=50,bg="blue",height=1,font=("arial 12 bold"))
                        self.bill_btn.place(x=0,y=650)

                    def add_to_cart(self,*args,**kwargs):
                        self.quantity_value = int(self.quantity_e.get())
                        if self.quantity_value > int(self.get_stock):
                            MessageBox.showinfo("Error quantity","We don't have enough [product] stock on hand for the quantity you selected. Please try again")
                        else:
                            ###calculate final price
                            self.final_price = (float(self.quantity_value))*(float(self.get_price))- (float(self.discount_e.get()))
                            products_list.append(self.get_product_name)
                            product_price.append(self.final_price)
                            product_quantity.append(self.quantity_e.get())
                            product_id.append(self.get_id)

                            self.x_index = 0
                            self.counter = 0
                            self.y_index = 100
                            
                            for self.p in products_list:

                                self.tempname = Label(self.right,text=str(products_list[self.counter]),font=("arial 18 bold"),bg="blue",fg="white")
                                self.tempname.place(x=0,y=self.y_index)
                                
                                self.tempqt = Label(self.right,text=str(product_quantity[self.counter]),font=("arial 18 bold"),bg="blue",fg="white")
                                self.tempqt.place(x=300,y=self.y_index)                

                                self.tempprice = Label(self.right,text=str(product_price[self.counter]),font=("arial 18 bold"),bg="blue",fg="white")
                                self.tempprice.place(x=500,y=self.y_index)

                                
                                self.y_index += 40
                                self.counter += 1

                 
                                #total configure

                                self.total_l.configure(text="Total: Rs "+ str(sum(product_price)))

                    def change_func(self,*args,**kwargs):

                        self.amount_given = float(self.change_e.get())
                        self.our_total = float(sum(product_price))

                        self.to_give =self.amount_given - self.our_total

                            #label change

                        self.c_amount = Label(self.left,text="change: Rs"+str(self.to_give),font=("arial 18 bold"),bg="red")
                        self.c_amount.place(x=0,y=600)
                    

                    def generate_bill(self,*args,**kwargs):
                        self.x = 0

                        conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                        c = conn.cursor()
                        
                        result = c.execute("select * from sales where id='"+(product_id[self.x])+"'")
                        

                        for i in products_list:
                            for self.r in result:
                                self.old_stock = r[2]
                            self.new_stock =int(self.old_stock)- int(product_quantity[self.x])

                            conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                            c = conn.cursor()
                            c.execute("Update sales set stock='"+str(self.new_stock)+"'")   
                            
                            
                            print("decreased")
                            conn.commit()
                            
                            self.x+=1
                            
                
                
                
        def sales():
            root = Tk()
            b = Application(root)
            root.geometry("1900x1000+0+0")
            root.mainloop()
        def Exit():
            result = MessageBox.askquestion('Simple Inventory System', 'Are you sure you want to exit?', icon="warning")
            if result == 'yes':
               main.destroy()
        btn1 = Button(main,width=20,height=5,bd=8,text="INVENTORY",command=stock,bg="red",fg="black").place(x=410,y=200)

        btn3 = Button(main,bd=8,width=20,height=5,text="SEARCH",command=search_now,bg="red",fg="black").place(x=570,y=200)
        btn7 = Button(main,bd=8,width=20,height=5,text="SALES",command=sales,compound="top",activebackground="white",bg="red",fg="black").place(x=730,y=200)

        btn4 = Button(main,bd=8,width=20,height=5,text="HELP",command=help,bg="red",fg="black").place(x=890,y=200)

        #btn2 = Button(main,image=photo2,bd=2,width=95,height=80,text="TRANSACTION",compound="top",bg="white",fg="black").place(x=570,y=200)        
        btn5 = Button(main,bd=8,width=20,height=5,text="EXIT",command=Exit,bg="red",fg="black").place(x=1050,y=200)
####==================================================PARENT WINDOW OR ROOT WINDOW=========================================================
    
    else:
        m=Label(App,text='Invalid Password and Username',font=('Bold', 15),fg='red').place(x=900,y=300)
def new_user():
        
        def ADDtodatabase():
                name = name.get();
                lname = lname.get();
                gender = v.get();
                email = BG.get();
                user = Ub1.get();
                newp = CB.get();
                conp = CB2.get();

                if(name =="" or lname=="" or gender=="" or email =="" or user =="" or newp==""or conp==""):
                   MessageBox.showinfo("Insert status","all field are required")
                else:
                    conn = mysql.connect(host = "localhost",user="root",password="",database="inventory")
                    cursor = conn.cursor()
                    cursor.execute("insert into emp1 values('"+ name +"','"+ lname +"','"+gender+"','"+email+"','"+user+"','"+newp+"','"+conp+"')")
                    cursor.execute("commit");

            
                    LR1.delete(0,'end') 
                    LR1.delete(0,'end')
                    v.delete(0,'end')
                    BG.delete(0,'end')
                    Ub1.delete(0,'end')
                    CB.delete(0,'end')
                    CB2.delete(0,'end')
                    show()
                    MessageBox.showinfo("Insert status","new user register succesfully");
                    conn.close();
        win1 = tk.Toplevel()
        win1.geometry("800x500")
        win1.configure(bg='skyblue')
        win1.title("INVENTORY MANAGEMENT SYSTEM")
        win1.resizable(0,0)
        w = Label(win1,text="SINGUP",font=("Times New Roman",20),bg="skyblue").place(x=350,y=10)
        
        R1 = Label(win1,text="Firstname",bg="skyblue",font=("bold",15)).place(x=200,y=50)
        R2 = Label(win1,text="Lastname",bg="skyblue",font=("bold",15)).place(x=200,y=80)
        name = Entry(win1,font=("bold",15),).place(x=370,y=50)
        lname = Entry(win1,font=("bold",15),).place(x=370,y=80)
        GL1 = Label(win1,text="Select Your Gender",bg="skyblue",font=(20)).place(x=200,y=110)
        v = tk.IntVar()
        tk.Radiobutton(win1,text="Male",variable=v,bg="skyblue",font=(20),value=1).place(x=300,y=140)
        tk.Radiobutton(win1,text="Female",variable=v,bg="skyblue",font=(20),value=2).place(x=300,y=170)
        tk.Radiobutton(win1,text="Transgender",variable=v,bg="skyblue",font=(20),value=3).place(x=300,y=200)
        Rg1 = Label(win1,text="Email Id",bg="skyblue",font=("bold",15)).place(x=200,y=240)
        BG = Entry(win1,font=("bold",15),).place(x=370,y=240)
        U1 = Label(win1,text="Username",bg="skyblue",font=("bold",15)).place(x=200,y=270)
        Ub1 = Entry(win1,font=("bold",15),).place(x=370,y=270)
        C1 = Label(win1,text="New password",bg="skyblue",font=("bold",15)).place(x=200,y=300)
        C2 = Label(win1,text="confirm password",bg="skyblue",font=("bold",15)).place(x=200,y=330)
        CB = Entry(win1,font=("bold",14),show="*",).place(x=370,y=300)
        CB2 = Entry(win1,font=("bold",14),show="*").place(x=370,y=330)
        S1 = Button(win1,bd=3,text="Register",command=ADDtodatabase,font=("bold",15),widt=35).place(x=200,y=380)


        
j=Label(App,text='',font=('Bold', 10),bg="white").place(x=900,y=320)
canvas1 = Canvas(App,width=800, height=700,bg="blue")

        
canvas1.place(x=0,y=100)

canvas2 = Canvas(App,width=748, height=700,bg="red")
canvas2.place(x=780,y=100)

photo = PhotoImage(file="inventory2.01.png")
canvas1.create_image(0,0, image=photo, anchor=NW)

photo1 = PhotoImage(file="inventory3.01.png")
canvas2.create_image(0,0, image=photo1, anchor=NW)

lblTitle = Label(App,text="INVENTORY MANAGEMENT SYSTEM",font=("Times New Roman",30),bg='white',relief=SOLID,padx=410,pady=12,fg="black" ).place(x=7,y=10)
        
a = Label(App ,text="USERNAME",font=('Bold', 15),bg='white').place(x=850,y=200)
b = Label(App ,text="PASSWORD",font=('Bold' ,15),bg='white').place(x=850,y=250)
e = Entry(App,textvariable=us1,font=('Bold', 20),bd=6).place(x=990,y=200)
f = Entry(App,textvariable=pw1,show="*",font=('Bold' ,20),bd=6).place(x=990,y=250)

c1 = Button(App ,width=20 ,text="LOGIN",font=('Bold' ,15),command=login).place(x=850,y=360)
c2 = Button(App,width=20,text="REGISTER",font=('Bold' ,15),command=new_user).place(x=1060,y=360)

App.mainloop()






