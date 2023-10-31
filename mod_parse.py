#按照班级分类：[[className,member1,member2,……],[className,member1,member2,……]，……]
def classify(list_name):
    list_className=[]
    #结构：[[className,member1,member2,……],[className,member1,member2,……]，……]
    list_classify=[]
    #temp2:一个[name,className]
    for temp2 in list_name:
        a=temp2[1] in list_className
        if(a == False):
            list_className.append(temp2[1])
            list_classify.append([temp2[1]])
        count=0
        #找到了，证明list_classify中有，那就直接在list_classify中找到对应项，添加进去
        #temp3=[className,member1,member2,……]
        for temp3 in list_classify:
            #该人员所在班级被找到
            if(temp3[0]==temp2[1]):
               temp3.append(temp2[0])
               #list_classify.pop(count)
               #list_classify.append(temp3)
            count=count+1
    return list_classify

#删掉已经有了的人
def compare_delete(member_source,member_data):
    
    #temp1=一个名字
    for temp1 in member_data:
        count=0
        for temp2 in member_source:
             #找到了
            if(temp1==member_source[count][0]):
                member_source.pop(count)
            count=count+1
    return member_source