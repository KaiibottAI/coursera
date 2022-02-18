Learning git with Coursera: Introduction to Git and GitHub (Sponsered by Google)

#Week 2
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
----------

[+] Skipping the Staging Area
If you know that the changes you want to make are going to the main file, you can use 'git commit -a'. This has to be a tracked file, this cannot be an untracked or 'new' file in the folder.
```
git commit -a -m "Call check_reboot, exit with 1 on error"
[main 3dae588] Call check_reboot, exit with 1 on error
 1 file changed, 4 insertions(+), 1 deletion(-)
 ```
 When using the 'git commit -m' you can only use short messages. When using the 'git commit -a', this SKIPS the staging area not allowing you to check the changes made.
 ```
 git log
commit 3dae588010e14bf5e7c6fe9e378f367658d3c966 (HEAD -> main)
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Mon Jan 3 09:47:14 2022 -0800

    Call check_reboot, exit with 1 on error
```
Git using the 'HEAD' alias to show you the latest snapshot of your project. When branches come up, the 'HEAD' could be part of a different part of your project. Kind of like a bookmark!

[+] Getting more info on Changes
By default, change logs will have the Author, Date and commit message. If you want more info, you can use the 'git log -p' (patch) command. This is similar to the 'diff -u' command
```
git log -p
commit 3dae588010e14bf5e7c6fe9e378f367658d3c966 (HEAD -> main)
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Mon Jan 3 09:47:14 2022 -0800

    Call check_reboot, exit with 1 on error

diff --git a/all_checks.py b/all_checks.py
index d418793..768ca2e 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -1,11 +1,14 @@
 #!/usr/bin/env python3
 
 import os
+import sys
```
Using commit IDs (the string next to the commit line) to identify unique commits.
```
git show
commit 3dae588010e14bf5e7c6fe9e378f367658d3c966 (HEAD -> main)
```
'git show' will show you the latest commit message or you can supply the unique commit ID to find others.
you can use 'git log --stat' to show more info on the commit messages
```
git log --stat
commit 3dae588010e14bf5e7c6fe9e378f367658d3c966 (HEAD -> main)
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Mon Jan 3 09:47:14 2022 -0800

    Call check_reboot, exit with 1 on error

 all_checks.py | 5 ++++- #Right here
 1 file changed, 4 insertions(+), 1 deletion(-)
 ```
If you make a lot of changes over a long amount of time, it could be difficult to remember all the changes you made and why. You can use the 'git diff' command to find out.
```
git diff
diff --git a/all_checks.py b/all_checks.py
index 768ca2e..f6b9de2 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -10,5 +10,8 @@ def main():
        if check_reboot():
                print("Pending Reboot.")
                sys.exit(1)
+       else:
+               print("Looks good here!")
+               sys.exit(0)
 
 main()
\ No newline at end of file
```
Lets say you did this to NUMEROUS files, you can instead pass the file name to the 'git diff' command to look at one individual file rather than all changes on screen.
Say you have chagnes that you don't want to commit just yet or all the changes. You can use the 'git add -p' and ask if you want to stage the change or not.
```
git add -p
diff --git a/all_checks.py b/all_checks.py
index 768ca2e..f6b9de2 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -10,5 +10,8 @@ def main():
 	if check_reboot():
 		print("Pending Reboot.")
 		sys.exit(1)
+	else:
+		print("Looks good here!")
+		sys.exit(0)
 
 main()
\ No newline at end of file
(1/1) Stage this hunk [y,n,q,a,d,e,?]? y
```
Since you now staged the change, there won't be a 'git diff' anymore. Instead, you need to check the staged files using 'git diff --staged'
```
git diff --staged
diff --git a/all_checks.py b/all_checks.py
index 768ca2e..f6b9de2 100755
--- a/all_checks.py
+++ b/all_checks.py
@@ -10,5 +10,8 @@ def main():
        if check_reboot():
                print("Pending Reboot.")
                sys.exit(1)
+       else:
+               print("Looks good here!")
+               sys.exit(0)
 
 main()
\ No newline at end of file
```

[+] Deleting and Renaming Files
You can use the 'git rm' command to remove a file from being tracked. File removals follow the same as commits, so you'll need a message as to why it was removed.
Likewise, say you need to rename a file in the git repository, you can use the 'git mv' command to rename a file.
```
git mv disk_usage.py check_free_space.py
git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	renamed:    disk_usage.py -> check_free_space.py

git commit -m 'Update name for disk_usage.py'
[main 874af45] Update name for disk_usage.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename disk_usage.py => check_free_space.py (100%)
 ```
 Say there are files you want to ignore in the git repository like temp files or test files. You can use the '.gitignore' file to ignore these cases.
 ```
echo .DS_STORE > .gitignore
ls -la #show all files

total 24
drwxrwxr-x 3 afk afk 4096 Jan  3 10:15 .
drwxrwxr-x 3 afk afk 4096 Jan  3 09:47 ..
-rwxrwxr-x 1 afk afk  298 Jan  3 09:59 all_checks.py
-rwxrwxr-x 1 afk afk  546 Jan  2 19:56 check_free_space.py
drwxrwxr-x 8 afk afk 4096 Jan  3 10:08 .git
-rw-rw-r-- 1 afk afk   10 Jan  3 10:16 .gitignore
```
Since this is a new file, this isn't being tracked. Don't forget to commit the files!
```
git add .gitignore 
git commit -m 'Add gitignore file'
[main 980b0a1] Add gitignore file
 1 file changed, 1 insertion(+)
 create mode 100644 .gitignore
```

[+] Undoing Changes before Commiting
'git checkout' or 'git restore' followed by the name can revert changes you have made but may not want to commit anymore. Like a time machine going back.
```
git status 
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   all_checks.py

no changes added to commit (use "git add" and/or "git commit -a")
git restore all_checks.py
```
Say you already staged changes but don't want them to go thru anymore. you can use 'git restore --staged <file name>' command.
```
./all_checks.py > output.txt
git add *
git status 
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   output.txt

git restore --staged output.txt
git status 
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	output.txt

nothing added to commit but untracked files present (use "git add" to track)
```

[+] Ammending Commits
Say you've made a commit but there are errors in the commit message or you added the wrong or not all files in your commit. You can use the 'git commit --amend' command to fix this. This will OVERWRITE the previous commit you made.
```
touch auto-update.py
touch gather-information.sh
git add auto-update.py 
git commit -m 'add two new scripts'
[main ffc270d] add two new scripts
 1 file changed, 0 insertions(+), 0 deletions(-) #The commit only added one script
 create mode 100644 auto-update.py

git add gather-information.sh
git commit --amend
[main 4656ac2] add two new scripts
 Date: Mon Jan 3 10:38:29 2022 -0800
 2 files changed, 0 insertions(+), 0 deletions(-) #the amend fixes this
 create mode 100644 auto-update.py
 create mode 100644 gather-information.sh

git log #checking our new amended commit
commit 4656ac222c74f5203bdd251ce65b999c8785fc4a (HEAD -> main)
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Mon Jan 3 10:38:29 2022 -0800

    add two new scripts
    
    Fixed addition to include the second script.
    gather-information.sh will be used to collect informatino in case of errors.
    auto-update.py will be run daily to update any tasks.
```
'git commit --amend' is okay for LOCAL git repositories, this is not cool with public commits.

[+] Rollbacks
Say you made a bad commit that had some errors in the commit that you don't find out until hours later when tickets pile in.
```
git commit -a -m 'Add call to disk_full function'
[main 8ae0eff] Add call to disk_full function
 1 file changed, 3 insertions(+)
```
Instead of hunting for the bug while the issue persists, you can rollback the change using 'git revert HEAD'
```
git revert HEAD
[main a4b5b11] Revert "Add call to disk_full function"
 1 file changed, 3 deletions(-)
```
Next you want to check the logs on why a revert was made.
```
git log -p -2 #the '-p' command is for patch, the '-2' command is to show the latest 2 changes
```

[+] Identifying a Commit
commit IDs use SHA1 to hash together the commit message, date, author and the change to keep it unique. This is all part of the magic of git to ensure what you put in, is what you get out with hashes.
```
git log -1
commit a4b5b117b41cfacc340e53e4b784a7506f7d24ac (HEAD -> main)
```
this commit ID is a hash of the change.
You can revert back to even EARLIER changes using the commit ID
```
ls
all_checks.py  auto-update.py  check_free_space.py  gather-information.sh
git revert 874af45cefed38390d9b3e66d6e249522c984ffd
[main dc4aa29] Revert "Update name for disk_usage.py"
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename check_free_space.py => disk_usage.py (100%)
ls
all_checks.py  auto-update.py  disk_usage.py  gather-information.sh
```
[+] What is a branch?
Branch - Pointer to a particular commit
The defualt branch that is created is called 'master'
This is typically the 'known good' version of the product

[+] Creating a new branch
You can use the 'git branch' command to list, create, delete and manipulate branches
```
git branch
* main
git branch new-feature
git branch
* main
  new-feature
```
You can swap between branches with the 'git checkout'
```
git checkout new-feature 
Switched to branch 'new-feature'
git branch 
  main
* new-feature
```
You can create a new branch and move to with 'git checkout -b <branch name>'
```
git checkout -b new-branch
Switched to a new branch 'new-branch'
```

[+] Working with branches
git branch will change files in the git repository based on what branch it is currently checked out. You can delete branches with 'git branch -d <branch name>'
```
git branch -d new-feature 
Deleted branch new-feature (was dc4aa29).
```
[+] Merging branches
A best practice with adding new features is to branch off of main, make updates, changes and validatations before merging to main with your updates. Merging is a term the Git uses for cobining branched data and history together.
'git merge'
```
git checkout main
Switched to branch 'main'
afk@ubuntu:/ /learn_git/checks$ git branch 
* main
  new-branch
afk@ubuntu:/ /learn_git/checks$ git merge new-branch 
Updating dc4aa29..d0ea69c
Fast-forward
 free_memory.py | 6 ++++++
 1 file changed, 6 insertions(+)
 create mode 100644 free_memory.py
```

[+] Merge conflicts
```
git merge new-branch 
Auto-merging free_memory.py
CONFLICT (content): Merge conflict in free_memory.py
Automatic merge failed; fix conflicts and then commit the result.
afk@ubuntu:/ /learn_git/checks$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   free_memory.py

no changes added to commit (use "git add" and/or "git commit -a")
```
