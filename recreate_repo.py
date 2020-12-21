import subprocess

subprocess.run('git remote -v', shell=True)
_ = input("Delete the repo (type anything to continue) ")

print()
subprocess.run('cd ..; git clone https://github.com/bCom5/mdbook-notes-template.git', shell=True)
subprocess.run('rm -rf ../mdbook-notes-template/src', shell=True)
subprocess.run('cp -r src ../mdbook-notes-template', shell=True)
print()

print('rename the mdbook-notes-template repo and complete the process with `python first_time.py`')




