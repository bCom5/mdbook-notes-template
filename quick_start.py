import subprocess

port = '3024'
line_fmt = 'open -a \"/Applications/Google Chrome.app\" {}'
subprocess.run(line_fmt.format(f'http://localhost:{port}/'), shell=True)
subprocess.run(f'subl .', shell=True)
subprocess.run(f'subl src/SUMMARY.md', shell=True)
subprocess.run(f'mdbook serve -p {port}', shell=True)
