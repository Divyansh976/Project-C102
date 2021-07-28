import time
import os
import shutil

def main():
    path = "C:/Users/Jai Gupta/Downloads/Python"
    days = 2
    seconds = time.time() - (days * 24 * 60 * 60)
    deletedFoldersCount = 0
    deletedFilesCount = 0
    if(os.path.exists(path)):
        for rootFolder, Folders, Files in os.walk(path):
            if(seconds >= getAge(rootFolder)):
                removeFolder(rootFolder)
                deletedFoldersCount + 1
                break
            else:
                for Folder in Folders:
                    folderPath = os.path.join(rootFolder, Folder)
                    if(seconds >= getAge(folderPath)):
                        removeFolder(folderPath)
                        deletedFoldersCount + 1
                for File in Files:
                    filePath = os.path.join(rootFolder, File)
                    if(seconds >= getAge(filePath)):
                        removeFile(filePath)
                        deletedFilesCount + 1
    else:
        if(seconds >= getAge(path)):
            removeFile(path)
            deletedFilesCount + 1
def removeFolder(path):
    if(not shutil.rmtree(path)):
        print(f'{path} is removed successfully')
    else:
        print('unable to delete')

def removeFile(path):
    if(not os.remove(path)):
        print(f'{path} is removed successfully')
    else:
        print('unable to delete')


def getAge(path):
    Ctime = os.stat(path).st_ctime
    return Ctime

if __name__ == "__main__":
    main()
