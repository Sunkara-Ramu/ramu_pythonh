import time
import os
class FileFinder:
    def _init_(self):
        pass
    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename
        self.filepath=filepath
        for root,dir,file in os.walk(filepath):
            if filename in file:
                files.append(os.path.join(root,filename))
        return files
if  _name=='main_':
    #st=time.time()
    obj=FileFinder()
    print(obj.find_file('Demo.txt','C:\\'))
    '''et=time.time()
    print(et-st)'''