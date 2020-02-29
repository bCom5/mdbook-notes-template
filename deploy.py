import subprocess

subprocess.run('git add -A', shell=True)
subprocess.run('git commit -m \'update repo\'', shell=True)
subprocess.run('git push', shell=True)

# subprocess.run('git worktree add release/ gh-pages', shell=True)
subprocess.run('mdbook build', shell=True)
subprocess.run('rm -rf release/*', shell=True) # this won't delete the .git directory
subprocess.run('cp -rp book/* release/', shell=True)
subprocess.run('cd release', shell=True)
subprocess.run('git add -A', shell=True)
subprocess.run('git commit -m \'update book\'', shell=True)
subprocess.run('git push origin gh-pages', shell=True)
subprocess.run('cd -', shell=True)
# subprocess.run('git checkout master', shell=True)
