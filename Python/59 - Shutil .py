import shutil

# If we want to copy the data from one file to another file 

# Note 1 , Note 2

a = "This is the first line data"
b = 'This is the second Line'
shutil.copy('59 - Shutil .py' , '59- 1 - Shutil .py')

#--------------------------------------------------------------------------------------------------------------

# If we want to copy the folder and inside the folder files means ..

shutil.copytree('59 - Shutil example' , '59- 2 - Shutil .txt')

# ----------------------------------------------------------------------------------------------------------

# If we want to move particulat file from folder to Present Direcatry path..

shutil.move("./59 - Shutil example/file.txt", "./file.txt")

#-----------------------------------------------------------------------------------------------------------

# If we want to remove the Folder means 

shutil.rmtree('59- 2 - Shutil .txt')

# ----------------------------------------------------------------------------------------------------------

## If we want to remove the particular file which was present in folder means

import os

os.remove('./59- 2 - Shutil .txt/hari.html')

























# NOTES :

# Note 1 :- If the given file name already exist means (59- 1 - Shutil .py) or (59- 2 - Shutil .py) then it will directly Paste in that File

# Note 2 :- If the file not exist means (59- 1 - Shutil .py) or (59- 2 - Shutil .py) , then it will create and paste it.



# Reference Limk : https://youtu.be/5b-mcBqPRGo [Telugu]
# Reference Limk :https://youtu.be/wII2JhNACJE [Hindi]