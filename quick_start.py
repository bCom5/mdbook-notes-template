import subprocess

line = 'open -a \"/Applications/Google Chrome.app\" {}'.format('http://localhost:3000/')
subprocess.run(line, shell=True)

