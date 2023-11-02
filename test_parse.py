import mod_parse as parse
#用于测试mod_parse.py的正确性
print("本程序用于测试mod_parse.py")
#member的list结构：[[name1,className1],[name2,className2],……]
testlist_member_source=[["人员A","1班"],["人员B","1班"],["人员C","2班"],["人员D","3班"],["人员E","3班"]]
testlist_member_data=["人员A","人员C"]
#member_source是所有名单的数据，member_data是已经签到的数据
print("@测试compare_delete")
res1=parse.compare_delete(testlist_member_source,testlist_member_data)
print("测试结果",res1)
#如果正确，输出：
print("正确结果","[['人员B', '1班'], ['人员D', '3班'], ['人员E', '3班']]")
print("@测试classify")
res2=parse.classify(res1)
print("测试结果",res2)
#如果正确，输出：“对拍程序”
print("正确结果","[['1班', '人员B'], ['3班', '人员D', '人员E']]")