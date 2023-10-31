import pandas as pd
import os

#读取特定的一列，需要提供中文ID
def get_column(xlsx_path,id_column):
    data=pd.read_excel(xlsx_path,"Sheet1")
    return data[id_column].to_list()

#绝对路径，日期（A-B），上午0或下午1(id_1)，签到0或签退1(id_2)
def output(path,list_classify,file_name):
    msg=""
    #解析部分
    #month,day,id_1,id_2
    title=file_name.replace(".xlsx","")
    msg=msg+title+"\n"
    for temp in list_classify:
        first=True
        msg=msg+temp[0]+":"
        for temp2 in temp:
            if(first):
                #跳过第一个
                first=False
                continue
            msg=msg+temp2+"，"
        msg=msg+"\n"

    file=open(path+"\\"+title+".txt","w")
    file.write(msg)
    file.close()

#ID需要提供中文,返回人员信息：[[name1,class1],[name2,class2]]
def get_memberinfo(xlsx_path,id_column_name,id_column_className):
    data=pd.read_excel(xlsx_path,"Sheet1")
    list_className=data[id_column_className].to_list()
    list_name=data[id_column_name].to_list()
    #定义一个list存放结果
    ret=[]
    count=0
    for temp1 in list_name:
        ret.append([temp1,list_className[count]])
        count=count+1
    return ret

def merge_xlsx(folder,destdir):
    list_files=os.listdir(folder)
    list_data=pd.read_excel(folder+"\\"+list_files[0])
    for temp in list_files:
        list_data=pd.concat([list_data,pd.read_excel(folder+"\\"+temp)])
    list_data.to_excel(destdir)