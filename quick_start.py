import subprocess

line_fmt = 'open -a \"/Applications/Google Chrome.app\" {}'
subprocess.run(line_fmt.format('http://localhost:3000/'), shell=True)
