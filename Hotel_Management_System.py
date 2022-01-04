# _*_ coding:utf-8   _*_
# 开发团队：XXXXXX
# 开发人员：李晓明
# 开发时间：2020/12/15
# 文件名称：binguan.py
# 开发工具：PyCharm
import re  # 导入正则表达式模块
import os  # 导入操作系统模块
import time
localtime = time.localtime(time.time())
filename = "binguan.txt"
filename2 = "dates.txt"
#三种类型房间房价
biao_money=100
shuang_money=150
hhf_money=200




def main():
    if not os.path.exists(filename):
        chushihua()  #初始化房间信息
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D", "", option)  # 提取数字
        if option_str in ['8', '1', '2', '3', '4', '5', '6', '7']:
            option_int = int(option_str)
            if option_int == 8:  # 退出系统
                print('您已退出宾馆管理系统！')
                ctrl = False
            elif option_int == 1:  # 录入顾客信息
                insert()
            elif option_int == 2:  # 查找顾客信息
                search()
            elif option_int == 3:  # 删除顾客信息
                delete()
            elif option_int == 4:  # 修改顾客信息
                modify()
            elif option_int == 5:  # 排序
                sort()
            elif option_int == 6:  # 统计空余房间
                total()
            elif option_int == 7:  # 显示所有顾客信息
                show()

def menu():
    # 输出菜单
    print('''
    ████████宾馆信息管理系统████████
    █                                          █
    █               ★功能菜单★               █
    █                                          █
    █           ❶ 录入顾客信息(开房)           █
    █           ❷ 查找顾客信息(查房)           █
    █           ❸ 删除顾客信息(退房)           █
    █           ❹ 修改顾客信息                 █
    █           ❺ 排序                         █
    █           ❻ 统计顾客总人数               █
    █           ❼ 显示所有顾客信息             █
    █           ❽ 退出系统                     █
    █                                          █
    ████████████████████████
    ''')

def chushihua():
    binguanList = []
    for i in range(10):
        binguan = {"id": 2010-i, "name": "null", "IdCard":0,"days": 0, "hometype": "标间","yu_money": 0}  # 将输入的顾客信息保存到字典
        binguanList.append(binguan)  # 将顾客字典添加到列表中
    for i in range(5):
        binguan = {"id": 1010-i, "name": "null", "IdCard":0,"days": 0, "hometype": "双人房","yu_money": 0}  # 将输入的顾客信息保存到字典
        binguanList.append(binguan)  # 将顾客字典添加到列表中
    for i in range(5):
        binguan = {"id": 1005-i, "name": "null", "IdCard":0,"days": 0, "hometype": "豪华房","yu_money": 0}  # 将输入的顾客信息保存到字典
        binguanList.append(binguan)  # 将顾客字典添加到列表中
    save(binguanList)  # 将顾客信息保存到文件
    print("顾客信息录入完毕！！！")


'''1 录入顾客信息'''
def insert():
    show()

    if os.path.exists(filename) :  # 判断文件是否存在
        with open(filename, 'r') as rfile:   # 打开文件
            binguan_old = rfile.readlines()  # 读取全部内容
    else:
        return
    while True:
        #防止输入的房间号为非数字类型数据而导致程序报错
        try:
            print("您好，提醒您：1001-1005为豪华房，1006-1010为双人房，2001-2010为标间")
            binguanid = int(input("请输入要入住的房间号ID："))
            if binguanid <1001 or binguanid>2010 or  1010<binguanid<2001:
                print("您输入的房间号有误请核对后再输入")
                continue
        except:
            print("您输入的房间号不规范，请核对")
        else:
            break

    with open(filename,"w") as wfile:# 以写模式打开文件
        for binguan in binguan_old:

            d = dict(eval(binguan))  # 字符串转字典

            if d["id"] == binguanid:
                if d["name"] =="null":
                    while True:
                        try:
                            d["name"] = input("请输入姓名：")
                            d["IdCard"] = int(input("请输入身份证号："))
                            if d["IdCard"]<10000 :

                                print("请输入正确的身份证号")
                                continue
                            d["days"] = int(input("请输入入住天数："))
                            if d["days"]<1 :
                                print("请输入规范的天数")
                                continue
                            if d["hometype"]=="标间":
                                d["yu_money"]=d["days"]*biao_money
                            elif d["hometype"]=="双人房":
                                d["yu_money"]=d["days"]*shuang_money
                            elif d["hometype"]=="豪华房":
                                d["yu_money"]=d["days"]*hhf_money


                        except:
                            print("您的输入有误，请重新输入")
                        else:
                            break  # 跳出循环
                    with open(filename2,"a") as wfile2:
                        wfile2.write("【开房信息】：\n 时间：{},房间号:{}，顾客:{}，身份证号：{},入住天数：{},预付金额：{}\n".format(time.strftime("%Y-%m-%d  %H:%M:%S ", time.localtime()),d["id"],d["name"],d["IdCard"],d["days"],d["yu_money"]))
                        wfile2.close()
                    binguan = str(d)  # 将字典转换为字符串
                    wfile.write(binguan + "\n")   # 将修改的信息写入到文件
                    print("登记完毕！")
                else:
                    print("抱歉，该房间已经有客人了，请您核对房间号")
                    wfile.write(binguan)

            else:

                wfile.write(binguan)  # 将未修改的信息写入到文件
        #print("您输入的房间号有误，请检查正确的房间号后重新录入!")
    mark = input("是否继续登记其他顾客信息？（输入y继续，输入其他默认退出）：")
    if mark == "y":
        insert()  # 重新执行修改操作

def search():
    mark = True
    binguan_list=[]
    with open(filename, 'r') as file:  # 打开文件
        binguan = file.readlines()
        for list in binguan:
            d = dict(eval(list))
            binguan_list.append(d)
    def paixu(x):
        datas=binguan_list
        lens=len(datas)
        for i in range(lens-1,-1,-1):
            for j in range(i):
                if int(datas[j][x])>int(datas[j+1][x]):
                    datas[j],datas[j+1]=datas[j+1],datas[j]
        return datas

    while mark:
        binguan_query = []

        if os.path.exists(filename):  # 判断文件是否存在
            print(
                '''
    ┏┳┳┳┳┳┳┳┳┳┳┳┳┳┳┳┳┳┳┓
    ┣               ★查找              ┫
    ┣      ①按房间号查找  ▶插值法       ┫
    ┣      ②按身份证号查找▶二分法       ┫
    ┣      ③按姓名查找    ▶顺序法       ┫
    ┣                                   ┫
    ┗┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┛
            ''')
            mode = input("请选择：")
            if mode=="1":
                key = int(input("请输入房间号："))
                if key <1001 or key>2010 or  1010<key<2001:
                    print("您输入的房间号有误请核对后再输入")
                    continue
                list=paixu("id")#调用排序函数
                length = len(list)
                low = 0
                high = length - 1
                while low <= high:
                    mid = low + int((high - low) * (key - list[low]["id"]) / (list[high]["id"] - list[low]["id"]))# 计算mid值是插值算法的核心代码
                    if key < list[mid]["id"]:
                        high = mid - 1
                    elif key > list[mid]["id"]:
                        low = mid + 1
                    else:
                        binguan_query.append(list[mid])
                        if list[mid]["days"]==0:
                            print("该房间还没有人入住,请核对您输入的房间号")
                            break
                        else:
                            show_binguan(binguan_query)
                            #print(list[mid])
                            break


            elif mode == "2":
                while True:
                    try:
                        id = int(input("请输入身份证号："))
                        if id<10000 :
                            print("请输入正确的身份证号")
                            continue
                    except:
                        print("您输入的身份证号不规范，请核对")
                    else:
                        break


                nums=paixu("IdCard")#二分查找先排序
                left, right = 0, len(nums) - 1
                while left <= right:
                    pivot = left + (right - left) // 2
                    if nums[pivot]["IdCard"] == id:
                        binguan_query.append(nums[pivot])

                        show_binguan(binguan_query)
                        #print(nums[pivot])
                        break
                    if id < nums[pivot]["IdCard"]:
                        right = pivot - 1
                    else :
                        left = pivot + 1
                if nums[pivot]["IdCard"] != id:
                    print("您所输入的身份证号没有开房信息，请重新核对！")




            elif mode =="3":
                #顺序查找法
                name = ""
                name =input("请输入您要查找的姓名")
                #print(name)
                if name == "":
                    print("查无此人")
                else:
                    names=''
                    for i in binguan_list:
                        if name == i["name"]:
                            binguan_query.append(i)
                            show_binguan(binguan_query)
                            names=i["name"]
                            break
                    if name != names:
                        print("没有找到名为{}的顾客,请核对您的输入".format(name))

            else:
                print("请输入正确的数字")

            inputMark = input("是否继续查询？（输入y继续，输入其他默认退出）:")
            if inputMark == "y":
                mark = True
            else:
                mark = False

def delete():
    show()  # 显示全部顾客信息
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            binguan_old = rfile.readlines()  # 读取全部内容
    else:
        return
    while True:
        #防止输入的房间号为非数字类型数据而导致程序报错
        try:
            print("您好，提醒您：1001-1005为豪华房，1006-1010为双人房，2001-2010为标间")
            binguanid = int(input("请输入要退的房间号ID："))
            if binguanid <1001 or binguanid>2010 or  1010<binguanid<2001:
                print("您输入的房间号有误请核对后再输入")
                continue
        except:
            print("您输入的房间号不规范，请核对")
        else:
            break

    with open(filename, "w") as wfile:  # 以写模式打开文件
        for binguan in binguan_old:
            d = dict(eval(binguan))  # 字符串转字典
            if d["id"] == binguanid and d["days"] ==0:
                print("你所要退的房间为空房间,请再次核对您的输入")
            if d["id"] == binguanid and d["days"]!=0:  # 是否为要修改的房间
                print("{}号房间，顾客{}退房成功".format(d["id"],d["name"]))


                with open(filename2,"a") as wfile2:
                    wfile2.write("【退房信息】：\n 退房时间:{},{}号房间，客户:{}，身份证号：{},入住天数：{},预付金额：{}\n".format(time.strftime("%Y-%m-%d  %H:%M:%S ", time.localtime()),d["id"],d["name"],d["IdCard"],d["days"],d["yu_money"]) + "\n")
                    wfile2.close()
                while True:  # 输入要修改的信息
                    try:
                        d["name"] = "null"
                        d["IdCard"] = 0
                        d["days"] = 0
                        d["yu_money"]=0
                        #d["hometype"] = "null"

                    except:
                        print("您的输入有误，请重新输入。")
                    else:
                        break  # 跳出循环
                binguan = str(d)  # 将字典转换为字符串
                wfile.write(binguan + "\n")   # 将修改的信息写入到文件
                #print("退房成功！")
            else:

                wfile.write(binguan)  # 将未修改的信息写入到文件


    mark = input("是否继续退房？（输入y继续，输入其他默认退出）：")
    if mark == "y":
        delete()  # 重新执行修改操作
def modify():
    show()
    if os.path.exists(filename) :  # 判断文件是否存在
        with open(filename, 'r') as rfile:   # 打开文件
            binguan_old = rfile.readlines()  # 读取全部内容
    else:
        return


    while True:
        #防止输入的房间号为非数字类型数据而导致程序报错
        try:
            print("您好，提醒您：1001-1005为豪华房，1006-1010为双人房，2001-2010为标间")
            binguanid = int(input("请输入要修改的房间号ID："))
            if binguanid <1001 or binguanid>2010 or  1010<binguanid<2001:
                print("您输入的房间号有误请核对后再输入")
                continue
        except:
            print("您输入的房间号不规范，请核对")
        else:
            break
    with open(filename,"w") as wfile:# 以写模式打开文件
        for binguan in binguan_old:

            d = dict(eval(binguan))  # 字符串转字典
            if d["id"] == binguanid:  # 是否为要修改的房间

                if d["days"] !=0:
                    while True:
                        try:
                            d["name"] = input("请输入姓名：")
                            d["IdCard"] = int(input("请输入身份证号："))
                            if d["IdCard"]<10000 :
                                print("请输入正确的身份证号")
                                continue
                            d["days"] = int(input("请输入入住天数："))
                            if d["days"]<1 :
                                print("请输入规范的天数")
                                continue

                            if d["hometype"]=="标间":
                                d["yu_money"]=d["days"]*biao_money
                            elif d["hometype"]=="双人房":
                                d["yu_money"]=d["days"]*shuang_money
                            elif d["hometype"]=="豪华房":
                                d["yu_money"]=d["days"]*hhf_money
                        except:
                            print("您的输入有误，请重新输入")
                        else:
                            break  # 跳出循环
                    binguan = str(d)  # 将字典转换为字符串
                    wfile.write(binguan + "\n")   # 将修改的信息写入到文件
                    with open(filename2,"a") as wfile2:
                        wfile2.write("【修改记录】：\n 时间：{},房间号:{}，顾客:{}，身份证号：{},入住天数：{},预付金额：{}\n".format(time.strftime("%Y-%m-%d  %H:%M:%S ", time.localtime()),d["id"],d["name"],d["IdCard"],d["days"],d["yu_money"]))
                        wfile2.close()
                    print("修改完毕！")
                else:
                    print("抱歉，该房间还未入住，请您核对房间号")
                    wfile.write(binguan)

            else:
                wfile.write(binguan)  # 将未修改的信息写入到文件
    mark = input("是否继续登记其他顾客信息？（输入y继续，输入其他默认退出）：")
    if mark == "y":
        modify()  # 重新执行修改操作




'''5 排序'''
def sort():

    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as file:  # 打开文件
            binguan_old = file.readlines()  # 读取全部内容
            binguan_new = []
        for list in binguan_old:
            d = dict(eval(list))  # 字符串转字典
            binguan_new.append(d)  # 将转换后的字典添加到列表中
    else:
        return

    print('''
    █████████████████████
    ▎                                      ▎
    ▎          ▶请选择排序方式              ▎
    ▎      ①按房间号排序  ▶冒泡排序        ▎
    ▎      ②按入住天数排序▶希尔排序        ▎
    ▎      ③按预付房费降序▶冒泡排序        ▎
    ▎      ④按预付房费排序▶插入排序        ▎
    ▎      ⑤按预付房费排序▶选择排序        ▎
    █████████████████████
                 ''')
    mode =input("您的选择：")
    if mode == "1":#冒泡排序
        datas=binguan_new
        lens=len(datas)
        for i in range(lens-1,-1,-1):
            for j in range(i):
                if int(datas[j]["id"])>int(datas[j+1]["id"]):
                    datas[j],datas[j+1]=datas[j+1],datas[j]



        print("============================================================================")
        print("【排序前数据】：")
        show()  # 显示全部学生信息

        print("============================================================================")
        print("【排序后数据】")
        show_binguan(datas)


    elif mode == "2":

        arr=binguan_new
        gap = len(arr) // 2
        while gap > 0:
            # 从增量值开始遍历比较
            for i in range(gap, len(arr)):
                j = i
                current = arr[i]
                # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
                while j - gap >= 0 and current["days"] < arr[j - gap]["days"]:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = current
            # 缩小增量（间隔）值
            gap //= 2

        print("============================================================================")
        print("【排序前数据】：")
        show()  # 显示全部学生信息

        print("============================================================================")
        print("【排序后数据】")
        show_binguan(arr)

    elif mode == "3":
        datas=binguan_new
        lens=len(datas)

        for i in range(lens-1,-1,-1):
            for j in range(i):
                if int(datas[j]["yu_money"])<int(datas[j+1]["yu_money"]):
                    datas[j],datas[j+1]=datas[j+1],datas[j]
        #print("【排序前数据】：")
        print("============================================================================")
        print("【排序前数据】：")
        show()  # 显示全部学生信息
        #print("【排序后数据】")
        print("============================================================================")
        print("【排序后数据】")
        show_binguan(datas)

    elif mode == "4":#插入排序法
        datas=binguan_new
        length = len(datas)
        if length <= 1:
            return

        for i in range(1, length):
            value = datas[i]
            j = i - 1
            while j >= 0 and datas[j]["yu_money"] > value["yu_money"]:
                datas[j + 1] = datas[j]
                #print(datas)
                j -= 1
            datas[j + 1] = value
            #print(datas)

        print("============================================================================")
        print("【排序前数据】：")
        show()  # 显示全部学生信息

        print("============================================================================")
        print("【排序后数据】")
        show_binguan(datas)

    elif mode == "5":#选择排序法
        datas=binguan_new
        length = len(datas)
        if length <= 1:
            return

        for i in range(length):
            min_index = i
            min_val = datas[i]
            for j in range(i, length):
                if datas[j]["yu_money"] < min_val["yu_money"]:
                    min_val = datas[j]
                    min_index = j
            datas[i], datas[min_index] = datas[min_index], datas[i]

        print("============================================================================")
        print("【排序前数据】：")
        show()  # 显示全部学生信息

        print("============================================================================")
        print("【排序后数据】")
        show_binguan(datas)
    else:
        print("请输入正确的序号")
        sort()
    modes=input("是否继续进行排序:(输入y继续，输入其他默认退出)")
    if modes == "y":
        sort()


''' 6 统计房间入住情况'''


def total():
    empty_room=0
    empty_room_list=[]
    full_room=0
    full_room_list=[]
    empty_hao_room=0
    empty_hao_room_list=[]
    empty_biao_room=0
    empty_biao_room_list=[]
    empty_shuang_room=0
    empty_shuang_room_list=[]
    filename = "binguan.txt"

    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            binguan_old = rfile.readlines()  # 读取全部内容


    for binguan in binguan_old:
        #顺序法查找并统计
        d = dict(eval(binguan))
        if d["days"] ==0:
            empty_room +=1
            empty_room_list.append(d["id"])
            if d["hometype"] == "标间":
                empty_biao_room +=1
                empty_biao_room_list.append(d["id"])
            elif d["hometype"]=="双人房":
                empty_shuang_room +=1
                empty_shuang_room_list.append(d["id"])
            elif d["hometype"]=="豪华房":
                empty_hao_room +=1
                empty_hao_room_list.append(d["id"])
        else:
            full_room +=1
            full_room_list.append(d["id"])

    print("""
    & & & & & & & & & & & & & & & &
    &                             &
    &    ①.统计空房间             &
    &    ②.统计已入住房间         &
    &    ③.统计豪华房入住情况     &
    &    ④.统计双人房入住情况     &
    &    ⑤.统计标间入住情况       &
    &                             &
    & & & & & & & & & & & & & & & &
                 """                  )
    mode = input("请输入序号选择您要统计的信息")
    if mode =="1":
        print("一共有{}间空房间".format(empty_room))
        print("以下为空房间的房间号：\n",empty_room_list)
    elif mode =="2":
        print("有客的房间一共有{}间".format(full_room))
        print("以下为已经入住的房间号:\n",full_room_list)
    elif mode =="3":
        print("豪华房一共有{}间空房\n 以下为空房房号：{}\n".format(empty_hao_room,empty_hao_room_list))
    elif mode =="4":
        print("双人房一共有{}间空房\n 以下为空房房号：{}\n".format(empty_shuang_room,empty_shuang_room_list))
    elif mode =="5":
        print("标间一共有{}间空房\n 以下为空房房号：{}\n".format(empty_biao_room,empty_biao_room_list))
    else:
        print("请输入正确的序号")
    mark = input("是否继续统计？（输入y继续，输入其他默认退出）：")
    if mark == "y":
        total()  # 重新执行修改操作



''' 7 显示所有学生信息 '''


def show():
    binguan_new = []
    if os.path.exists(filename):  # 判断文件是否存在
        with open(filename, 'r') as rfile:  # 打开文件
            binguan_old = rfile.readlines()  # 读取全部内容
        for list in binguan_old:
            binguan_new.append(eval(list))  # 将找到的顾客信息保存到列表中
        if binguan_new:
            show_binguan(binguan_new)
    else:
        print("暂未保存数据信息...")


# 将保存在列表中的学生信息显示出来
def show_binguan(binguanList):
    if not binguanList:
        print("无数据信息\n")
        return
    format_title = "{:^6}\t{:^16}\t{:^8}\t{:^6}{:^10}{:^6}"
    print(format_title.format("ID", "名字", "身份证号", "入住天数", "房间类型","预付金额"))
    format_data = "{:^6}\t{:^16}\t{:^8}\t{:^14}{:<10}{:<6}"
    for info in binguanList:
        print(format_data.format(str(info.get("id")), info.get("name"),str(info.get("IdCard")), str(info.get("days")), info.get("hometype"), str(info.get("yu_money"))))
def save(binguan):
    try:
        binguan_txt = open(filename, "a")  # 以追加模式打开
    except Exception as e:
        binguan_txt = open(filename, "w")  # 文件不存在，创建文件并打开
    for info in binguan:
        binguan_txt.write(str(info) + "\n")  # 按行存储，添加换行符
    binguan_txt.close()  # 关闭文件

if __name__ == "__main__":
    main()
