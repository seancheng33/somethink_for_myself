'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/9/01
@Program      : 1.实现下述功能。在屏幕上显示功能菜单，功能菜单示例如下：
显示所有信息
追加信息
删除信息
请输入数字1-3选择功能：
收用户输入数字选择功能，如果输入错误，要求用户重新输入。如果输入正确，
在屏幕上显示提示语句：您选择了功能1/2/3.
2.实现功能1——当用户选择1的时候，从通讯录文件读取信息，显示所有信息。
3.实现功能2——追加信息。让用户从键盘输入一个学生的信息，用逗号隔开。
在屏幕上显示追加后的所有信息，并将信息写入文件 new_address.txt 中，
文件格式与 address 相同。
'''
address_list = []
with open('address.txt','r',encoding='utf-8') as infile:
    for listItem in infile.readlines():
        address_list.append(listItem.strip('\n'))
print('1.显示所有信息')
print('2.追加信息')
print('3.删除信息')
s=eval(input('请输入数字1-3选择功能：'))
while s not in (1,2,3):
    s=eval(input('请输入数字1-3选择功能：'))


if s == 1:
    # print('您选择了功能1')
    for listItem in address_list:
            print(listItem)
if s == 2:
    print('您选择了功能2')
    newinput = input()
    address_list.append(newinput)
    with open('new_address.txt','w',encoding='utf-8') as outfile:
        outfile.write('\n'.join(address_list))
    for listItem in address_list:
        print(listItem)
if s == 3:
    print('您选择了功能3')    
