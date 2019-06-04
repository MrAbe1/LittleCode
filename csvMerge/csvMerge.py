import pandas as pd
import os.path

print("请输入文件夹1的目录");
dir1 = input()
print("请输入文件夹2的目录");
dir2 = input()
print("请输入输出的目录");
out = input()

files = os.listdir(dir1)

for file in files:
    data_a = pd.read_csv(dir1+"\\"+file, encoding='utf-8')
    data_b = pd.read_csv(dir2+"\\"+file, encoding='utf-8')
    data_d= data_b.drop({data_b.columns[0],data_b.columns[1]},axis=1)
    data_c = pd.concat([data_a,data_d],axis=1)
    data_c.to_csv(out + "\\" + file, index=False);

#data_c.to_csv("E:\\out\\1.csv",index=False);
'''data_c.to_csv("E:\\out\\1.csv",index=False);
print(data_c)'''