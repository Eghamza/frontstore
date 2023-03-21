import subprocess
letters = ['A','B','C','D','E','F','G','H']


# total_dir = []
# for l in letters:
#     dir =  f"{l}:\\"
#     # command =["powershell", "& { dir ls -Recurse | select * }"]
#     # total_dir=subprocess.run(command, shell=True, capture_output=True )
    
#     print(dir)

# command =["powershell", "& { C:\> ls -Recurse | select * | Out-File -FilePath="+C:\Users\Nisa\Desktop\y.csv+"}"]
# total_dir=subprocess.run(command, shell=True, capture_output=True )
# print(total_dir)

path = r"C:\Users\Nisa\Desktop\yes.csv"
command =["powershell", "& { C:\> ls -Recurse | select * | Out-File -FilePath "+path+"}"]
t=subprocess.run(command, shell=True )
print(t)