def month(year,number):
    if number==2:
        if year%4==0:
            return 29
        else:
            return 28
    elif number in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30  
def salary(time,wage):
    if time>40:
        a=time-40
        s=(40*wage)+(a*40*3/2)
    else:
        s=time*wage
    return s
 
def sapxep(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
def ten(r):
    FirtsName = ""
    MiddleName = ""
    n= ""
    for x in range(len(r)):
        if x==0 or r[x-1]==" ":
           n+=r[x].upper()
        else:
            n+=r[x]
    Space=0
    for x in n:
        if x == " ":
            Space +=1
    a=Space
    for x in range(len(n)):
        if n[x] == " ":
            a -= 1
        if a == 0:
            FirtsName += n[x]
        if a > 0:
            MiddleName += n[x]
    print("Họ và tên lót: ",MiddleName)
    print("Tên: ",FirtsName)
    print("Họ và tên đầy đủ nhân viên là: ",n)
def enter():
    a = int(input('nhap so mon hoc: '))
    b=[]
    c=[]
    for x in range(a):
        b+=[float(input('nhap diem mon: '))]
        c+=[float(input('nhap he so mon 1 đến 3: '))]
    return a,b,c
def point():
    a,b,c = enter()
    ave=0
    hs=0
    for x in range(a):
        ave+= b[x]*c[x]
        hs+=c[x]
    return ave/hs,hs
def mot():
    b=int(input("nhap nam: "))
    a= int(input("nhap thang: "))
    print("nam",b, "thang ",a," co",month(b,a)," ngay.")
def hai():
    time=int(input("Nhập số giờ làm: "))
    wage=int(input("Nhập mức lương: "))
    Luong=salary(time,wage)
    print(Luong)
def ba():
    n= int(input("Nhap danh sach luong: "))
    x= []
    b= 0
    for i in range(n):
        b=int(input("nhap luong nhan vien "+ str(i+1)+": "))  
        x.append(b)
    print("danh sach sau khi sap xep:",sapxep(x))
def bon():
    n=input("nhập họ tên: ")
    ten(n)
def nam():
    a,b=point()
    print("diem so trung binh mon la",a)
    print("cong he so",b)
menu=("""
******************************************
******Chuong Trinh Hoc Thong Minh*****
******************************************
=====================MENU=================
Xin vui long chon
1. Xem lich
2. Tinh luong
3. Xem luong
4. Xem thong tin nhan vien
5. Tinh diem cua hoc sinh
6. Thoat chuong trinh
""")
 
while True:
    print(menu)
    a=int(input("nhap tu ban phim:"))
    if a==1:
        while True:
            mot()
            question = input("Any key for continue and x for go to menu.")
            if question == "x":
                break
    if a==2:
        while True:
            hai()
            question = input("Any key for continue and x for go to menu.")
            if question == "x":
                break
    if a==3:
        while True:
            ba()
            question = input("Any key for continue and x for go to menu.")
            if question == "x":
               
                break
    if a==4:
        while True:
            bon()
            question = input("Any key for continue and x for go to menu.")
            if question == "x":
                break
    if a==5:
        while True:
            nam()
            question = input("Any key for continue and x for go to menu.")
            if question == "x":
                break
    if a==6:
        if a==6:
            print("Xin cảm ơn !")
        break
 

