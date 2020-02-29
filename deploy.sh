import subprocess

temp_loc="mdbook_template"

git add -A
git commit -m 'update repo'
git push

git worktree add /tmp/$temp_loc/ gh-pages
mdbook build
rm -rf /tmp/$temp_loc/* # this won't delete the .git directory
cp -rp book/* /tmp/$temp_loc/
cd /tmp/$temp_loc
git add -A
git commit -m 'update book'
git push origin gh-pages
cd -
git checkout master

