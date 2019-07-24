import os

path = '/home/ali/Desktop/data'


arr = os.listdir(path)
print(arr)


f= open("test.txt","w+")


for i in arr:
    new_path=path+"/"+i
    new_arr=os.listdir(new_path)
    for j in new_arr:
        sub_path=new_path+"/"+j
        sub_arr=os.listdir(sub_path)
        print(sub_path)
        print(sub_arr)
        f.write(sub_path+" "+i[2:]+"\n")
f.close