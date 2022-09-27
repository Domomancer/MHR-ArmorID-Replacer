# skript to search and replace outfit ids from armor mods

# --- Imports     --- #
import os
# --- Imports END --- #

# --- Global Variables     --- #
# ArmorIDs: 200: Kamura
# List of ArmorIDs: https://github.com/mhvuze/MonsterHunterRiseModding/wiki/Armor-IDs

# before: current armorID for Armor-Mod
before = "000"
# after: new armorID for Armor-Mod
after = "000"
# PATH TO MOD FOLDER (BEFORE IT IS INSERTED INTO THE NATIVES FOLDER!)
# Example: 'C:/MHR-ArmorID-Replacer/TEMP/Folder-with-Mod'
rootFolder = '<PATH TO MOD FOLDER>'

renameCount = 0
renameLaterList = []
# --- Global Variables END --- #

def main():
  print("#### [INFO]: Starting renaming skript")

  # Change into the root directory as a searchbase
  if(changeDirectory(rootFolder) == False):
    print(f"#### [ERROR]: changing the directory to {rootFolder} caused an Error. Program will be terminated!")
    exit()

  print(f"#### [INFO]: Replacing ArmorID {before} with ArmorID {after}")

  # start to crawl through all files and folders in the root directory to search and replace all files
  replaceIDsInFilePathsRecursive(rootFolder)

  # Change back into the root directory to search and replace all the folders you didnt have the right to, before
  if(changeDirectory(rootFolder) == False):
    print(f"#### [ERROR]: changing the directory to {rootFolder} caused an Error. Program will be terminated!")
    exit()
  
  searchAndReplace(renameLaterList)

  print(f"#### [INFO]: Recursive replacement has finished. {renameCount} Elements have been renamed.")

  exit()

# --- functions     --- #

def replaceIDsInFilePathsRecursive(currentPath):
  global before, after
  # print(os.listdir("."))
  for element in os.listdir("."):
    elementPath = '{}/{}'.format(currentPath, element)
    # print(elementPath)
    if(isDirectory(elementPath)):
      # If isDirectory == True, try to enter the directory and call replaceIDsInFilePathsRecursive again
      # print("change Directory!!")
      if(changeDirectory(elementPath) == False):
        print(f'Skipping {elementPath}')
      replaceIDsInFilePathsRecursive(elementPath)

    # search and replace 'before' with 'after' for current element (file or folder)
    if(str(before) in element):
      # create new path with renamed filename/foldername in element (dont replace entire path!)
      newElementPath = '{}/{}'.format(currentPath, element.replace(str(before), str(after)))
      print(f"#### [INFO]: Found {element}")
      renameLaterList.append([elementPath, newElementPath])
  pass

def searchAndReplace(array):
  global renameCount
  # search and replace all elements in the "renameLaterList"-Array
  for a in array:
    # a[0] = old name; a[1] = new name
    os.rename(a[0], a[1])
    # print(f"Renamed {a[0]} to {a[1]}")
    print(f"#### [INFO]: Renamed {a[1]}")
    renameCount = renameCount + 1
  pass

# --- functions END --- #

#  --- Util functions --- #

def isDirectory(path):
  return os.path.isdir(path)

def isFile(path):
  return os.path.isfile(path)

def changeDirectory(path):
  try:
    os.chdir(path)
  except PermissionError:
    print(f'Permission Error occured for: {path}')
    return False
  return True

#  --- Util functions END --- #

if __name__ == "__main__":
  main()

# LEAVE A LAST LINE!
