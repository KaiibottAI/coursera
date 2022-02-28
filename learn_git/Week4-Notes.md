Week4-Notes.md

Learning git with Coursera: Introduction to Git and GitHub (Sponsered by Google)

#Week 4
----------
#Commands used (Week 1)
diff
diff -u
git add
git init
git clone
git commit
git commit -m
git status
git log

#Commands used (Week 2)
git commit -a / Stage Files Automatically
git log -p / produces patch text
git show / show various objects
git log --stat 
git diff / show differences in various commits
git diff --staged / alias to --cached, show stages files compared tothe named commit
git add -p / allows user to revieew patches to add to the cuirrent commit
git rm / removes files from the git tracked files
git mv / renames files from the git tracked files
.gitignore / specifies files to ignore and not track like temp files
git branch / Used to manage branches
git branch <name> / Creates the branch
git branch -d <name> / Deletes the branch
git branch -D <name> / Forcibly deletes the branch
git checkout <branch> / Switches to a branch.
git checkout -b <branch> / Creates a new branch and switches to it.
git merge <branch> / Merge joins branches together. 
git merge --abort / If there are merge conflicts (meaning files are incompatible), --abort can be used to abort the merge action.
git log --graph --oneline / This shows a summarized view of the commit history for a repo.

#Commands used (Week 3)

git clone URL / Git clone is used to clone a remote repository into a local workspace
git push / Git push is used to push commits from your local repo to a remote repo
git pull / Git pull is used to fetch the newest updates from a remote repository
git remote / Lists remote repos
git remote -v / List remote repos verbosely
git remote show <name> / Describes a single remote repo
git remote update / Fetches the most up-to-date objects
git fetch / Downloads specific objects
git branch -r / Lists remote branches; can be combined with other branch arguments to manage remote branches

#Commands used (Week 4)

rebase -i / Interactive rebase
When using Rebase,
-squash / combines the commit messages into one
-fixup / discards new commit messages
----------

[+] Squashing Changes

[+] Code Reviews
