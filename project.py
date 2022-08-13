from distutils import extension
import os
import shutil
fromfolder= "C:/Users/KRANTI/Downloads"
tofolder="C:/Users/KRANTI/Desktop/nidhi documents"
listoffiles=os.listdir(fromfolder)
print (listoffiles)
for file in listoffiles:
    root,Extension =os.path.splitext(file)
    #print("The root of the file :",root)
    #print("The extension of the file:",Extension)
    if Extension== " ":
        continue 
    if Extension in [".txt",".doc",".docx",".pdf"]:
        path1=fromfolder+"/"+file
        path2=tofolder+"/"+ "nidhi documents"
        path3=tofolder+"/"+"nidhi documnets"+file
        if os.path.exists(path2):
          print("Moving"+"file_name"+"..........")
          shutil.move(path1,path3)
            
        else:
            os.mkdir(path2)
            print("Moving"+"file_name" + "..........")
            shutil.move(path1,path3)
            