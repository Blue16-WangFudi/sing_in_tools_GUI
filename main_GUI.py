#encoding=utf-8
#author: blue16（Index:blue16.cn）
#date: 2023-10-29
#summary: 一个带GUI且分模块的签到小程序，刚好三个人三个模块。

#GUI库文件
import PySimpleGUI as sg
import os
#导入mod
import mod_datarw as rw
import mod_parse as parse
 
# 布局
layout=[[sg.Text("选择输入数据集:"),sg.In(key = '-Input-',enable_events=True),sg.FolderBrowse(button_text = "选择目录",target = '-Input-')],
        [sg.Text("找到的数据表:")],
        [sg.Text("",key='-Prompt_Department-')],
        [sg.Text("选择名单数据集:"),sg.In(key = '-InputTable-',enable_events=True),sg.FolderBrowse(button_text = "选择文件",target = '-InputTable-')],
        [sg.Text("选择输出文件夹:"),sg.In(key = '-Output-'),sg.FolderBrowse(button_text = "选择目录",target = '-Output-')],
        [sg.Text("生成输出:")],
        [sg.Text("",key="-Prompt_Output")],
        [sg.Button("开始生成",key = '-Start-'),sg.Button("退出",key = '-Exit-')]

] 
# 创建窗口
window = sg.Window('签到统计小工具 - by Blue16', layout)
#找到的数据文件，后面会用到
list_files=[]
# 事件循环
while True:
    event, values = window.read()

    #这里有一个问题：反复点击编辑框会导致反复查找
    if(event=="-Input-"):
        list_files=os.listdir(values["-Input-"])
        print(list_files)
        count=1
        str=""
        for temp in list_files:
            temp2=temp.split(".")
            if(temp2[len(temp2)-1]!="xlsx"):
                continue
            if(count==len(list_files)):
                str=str+temp
            else:
                str=str+temp+"\n"
            count=count+1
        window['-Prompt_Department-'].update(str)
    if(event=='-Start-'):
        rw.merge_xlsx(values['-InputTable-'],"namelist_merge.xlsx")
        for temp in list_files:
            temp2=temp.split(".")
            if(temp2[len(temp2)-1]!="xlsx"):
                continue
            list_member=rw.get_memberinfo("namelist_merge.xlsx","姓名","班级")
            list_sign_in=rw.get_column(values["-Input-"]+"\\"+temp,"姓名")
            list_result=parse.compare_delete(list_member,list_sign_in)
            list_classify=parse.classify(list_result)
            #需要修改，写个parse
            rw.output(values['-Output-'],list_classify,temp)
            window['-Prompt_Output'].update("读取名单\n获取成员信息\n比较与分类\n输出文本")
        sg.popup_ok("生成完成！",title="提示")
    if event == sg.WIN_CLOSED or event == 'Submit' or event=='-Exit-':
        break

# 关闭窗口
window.close()
