#!/usr/bin/python

def func():
    list1=input("1st list :").split(',')
    list2=input("2nd list :").split(',')
    count=0
    for i in list1:
        i=i.replace("[","").replace("]","").replace(" ","")
        k=int(i)
        list1[count]=k
        count+=1

    count=0
    for i in list2:
        i=i.replace("[","").replace("]","").replace(" ","")
        k=int(i)
        list2[count]=k
        count+=1


    new_list=[]
    list3 = list1+list2

    for x in list3:
        if x not in new_list:
            new_list.append(x)

    new_list.sort()
    print("=>Union",new_list)
    new_list2=[]
    for x in list1:
        if x in list2:
            new_list2.append(x)

    print("=>intersection",new_list2)

if __name__ == '__main__':
    func()

