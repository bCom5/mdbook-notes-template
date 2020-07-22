import subprocess
name = input('What to name this book?\n')

lines = f'''[book]
authors = ["Brian Liao"]
language = "en"
multilingual = false
src = "src"
title = "{name}"

[output.html]
default-theme = "ayu"
mathjax-support = true
'''

with open('book.toml', 'w') as f:
    f.write(lines)

port = input('What port to use when serving mdbooks?\n')

quick_start = '''import subprocess
line_fmt = 'open -a \"/Applications/Google Chrome.app\" {}'
'''
quick_start += f'''
subprocess.run(line_fmt.format(f'http://localhost:{port}/'), shell=True)
subprocess.run(f'subl .', shell=True)
subprocess.run(f'subl src/SUMMARY.md', shell=True)
subprocess.run(f'mdbook serve -p {port}', shell=True)
'''

with open('quick_start.py', 'w') as f:
    f.write(quick_start)

origin = input('What is the Github origin to add? ( https://github.com/new )\n')
subprocess.run('rm -rf .git', shell=True)
subprocess.run('rm -rf release', shell=True)
subprocess.run('git init', shell=True)
subprocess.run('git add .', shell=True)
subprocess.run('git commit -m \'init commit\'', shell=True)
subprocess.run(f'git remote add origin {origin}', shell=True)
subprocess.run('git push -u origin master', shell=True)

subprocess.run('mkdir release', shell=True)
subprocess.run('git worktree add release/ -b gh-pages', shell=True)
subprocess.run('git checkout master', shell=True)

settings = origin.replace('.git', '/settings')
print(f'\nWhen deployed remember to set to https at {settings}')
