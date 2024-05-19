@echo off

git add --all
git commit
timeout /t -1
git push