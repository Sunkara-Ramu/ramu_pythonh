import os
class SystemDriveFinder:
    def _init_(self):
        pass
    def find_drives(self):
        print("this is the find drives method of system drive method of system drive finder class")
        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives

if __name=='main_':
    obj=SystemDriveFinder()
    print(obj.find_drives())