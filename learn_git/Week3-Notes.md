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

Learning git with Coursera: Introduction to Git and GitHub (Sponsered by Google)

#Week 3
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
----------
[+] What is GitHub?

[+] What is a remote?
A remote repository

[+] Working with Remotes
```
git remote -v
origin	https://github.com/KaiibottAI/health-checks.git (fetch)
origin	https://github.com/KaiibottAI/health-checks.git (push)
```
You can check the name of the remote by using 'git remote -v'
One is used to fetch data, the other is used to push. They usually use the same URL, but the push can be a different URL like HTTPS or SSH for more security.

You can get more info on the origin with the following command
```
git remote show origin
* remote origin
  Fetch URL: https://github.com/KaiibottAI/health-checks.git
  Push  URL: https://github.com/KaiibottAI/health-checks.git
  HEAD branch: main
  Remote branch:
    main tracked
  Local branch configured for 'git pull':
    main merges with remote main
  Local ref configured for 'git push':
    main pushes to main (up to date)
```
Since we are working with a remote, using 'git status' will have some more info
```
git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

[+] Fetching new Changes
using the 'git fetch' command will update our local repositories if there was an update to the remote repo while we were working with a team.
you can merge the remote repo with 'git merge origin/master' to update the local repo to the remote repo.
git pull instantly merges while git fetch only retrieves remote updates.git remote 

[+] PULL-MERGE-PUSH workflow
