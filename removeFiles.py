import os
import shutil
import time

def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0

    path = '/Users/sourindramaity/Documents/Monty/Coding/Python/Project 99/sample1.txt'
    days = 30

    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for rootFolders,folders,files in os.walk(path):
            if seconds >= getFileOrFolderAge(rootFolders):
                removeFolder(rootFolders)
                deletedFoldersCount += 1

                break
            
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolders,folder)

                    if seconds>=getFileOrFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount += 1
                
                for file in files:
                    filePath = os.path.join(rootFolders,file)

                    if seconds >= getFileOrFolderAge(filePath):
                        removeFile(filePath)
                        deletedFilesCount += 1

        else:
            if seconds >= getFileOrFolderAge(path):
                removeFile(path)
                deletedFilesCount += 1
        
        print(f"Total Folders Deleted: {deletedFoldersCount}")
        print(f"Total Files Deleted: {deletedFilesCount}")

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed sucessfully")

    else:
        print(f"Unable to delete the" + path)

def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed sucessfully")

    else:
        print(f"Unable to delete the" + path)

def getFileOrFolderAge(path):
    ctime = os.stat(path).st_ctime

    return ctime

if __name__ == '__main__':
    main()