rm -rf .git
git init
git add .
git commit -m 'init commit'

git remote add origin [link]
git push -u origin master

mkdir release
git worktree add release/ gh-pages
git checkout master
