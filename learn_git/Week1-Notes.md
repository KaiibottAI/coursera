Learning git with Coursera: Introduction to Git and GitHub (Sponsered by Google)

#Week 1
----------
#Commands used
git add
git init
git clone
git commit
git commit -m
git status
git log
----------



[+]Version Control
Keeping a version history is critical when changes come up so you can see where an item may have worked before, but not after an update

Using a VCS (Version Control System) this allows you to 'rollback' easily if there is an issue in the code

[+]Keeping Historical Copies:
WHen working with a team, you all may be working a on the same project and everyone will have their own versions. Kind of a nightware, right?
You may have your own 'master version' while a team member may have their own. The files will overlap and be a bad time.

[+]'Diff'ing files:
use the 'diff' command line tool to find the differences between files or even directories
Example:
```
diff rearrange1.py rearrange2.py 
6c6 #the 'c' will tell us there is a 'changed' line
< 	result = re.search(r"^([\w .]*), ([\w .*])$", name) #the '<' tell us a removed line
---
> 	result = re.search(r"^([\w .-]*), ([\w .-]*)$", name) #the '>' tell us an added line
```

Example with '-u' flag to show more context (default 3 lines) behind where the change exists
-u, -U NUM, --unified[=NUM]
              output NUM (default 3) lines of unified context

```
diff -u rearrange1.py rearrange2.py 
--- rearrange1.py	2022-01-02 13:15:18.348316704 -0800
+++ rearrange2.py	2022-01-02 13:15:19.068356826 -0800
@@ -3,7 +3,7 @@
 import re
 
 def rearrange_name(name):
-	result = re.search(r"^([\w .]*), ([\w .*])$", name)
+	result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
 	if result == None:
 		return result
 	return "{} {}".format(result[2],result[1])
\ No newline at end of file

```

[+]Applying Changes
You can send a team member a 'diff' file to show the changes easier
You can send them a command like this
```
diff -u old_file new_file > change.diff
```
The diff command will export to a 'change.diff' file so whomever reads the change can see exactly the new difference from the updates.
You can make the changes from the 'change.diff' file with a command called 'patch'
```
patch cpu_usage.py < cpu_usage.diff 
patching file cpu_usage.py
```

[+]What is Version Control?
A VCS or Version Control System, saves the history of files rather than only keeping the most updated version. This helps show how a file was changed, who did the change and when.

[+]Version Control and Automation
Since VCS stores and controls the file configuration, this is invaluable to keeping track of changes even if you are a solo dev. This saves you from looking at code from three months ago without comments. Say you have a DHCP server go down over the weekend. You can look at the VCS to find that there was an update on Friday afternoon that had a duplicate entry that caused the issue. Using the VCS, you can rollback the change to a stable environment before the 'new' problem code went out.

[+]What is Git?
Git is a VCS created in 2005 by Linus Torvalds, the developer who created Linux kernel
You can use Git with or without a network connection using a Git server locally on the machine or on a server. Git client talks to a Git server to start the process. Git can talk over http, ssh or Git's own special protocol.

[+]First Steps with Git
To track how you are using git and how others can track you, you need to tell Git who you are.
```
git config --global user.email "#####"
git config --global user.name "#####"
```
You can start using git by either creating a repository by using the 'git init' command or you can clone an existing repository by using 'git clone'.
To start working with git, we will use the 'git init' commands. Watch this.
```
git init
Initialized empty Git repository in /home/afk/learn_git/checks/.git/
```
You can verify the 'git init' command worked by using 'ls -la' to view all files that start with '.'
```
ls -la
total 12
drwxrwxr-x 3 afk afk 4096 Jan  2 19:42 .
drwxrwxr-x 3 afk afk 4096 Jan  2 19:42 ..
drwxrwxr-x 7 afk afk 4096 Jan  2 19:43 .git
```
You can view all the items in '.git' by the following
```
ls -l .git
total 32
drwxrwxr-x 2 afk afk 4096 Jan  2 19:42 branches
-rw-rw-r-- 1 afk afk   92 Jan  2 19:43 config
-rw-rw-r-- 1 afk afk   73 Jan  2 19:42 description
-rw-rw-r-- 1 afk afk   21 Jan  2 19:43 HEAD
drwxrwxr-x 2 afk afk 4096 Jan  2 19:42 hooks
drwxrwxr-x 2 afk afk 4096 Jan  2 19:42 info
drwxrwxr-x 4 afk afk 4096 Jan  2 19:42 objects
drwxrwxr-x 4 afk afk 4096 Jan  2 19:42 refs
```
The git directory contains all the changes and their history and the working tree contains the current versions of the files.The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current versions of the files.
You can use the 'git add' command to add files to the next 'git commit'. You can check on the items that are going to be effected by using the 'git status' command.
```
git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   disk_usage.py

```

[+]Tracking Files
Git consists of three sections.
-Git Directory
-Working Tree: Contains the current state of the project, including changes that we've made.
-Staging Area: Contains the changes that have been marked to be included in the next commit.
Each time you make a commit, Git creates a 'snapshot' of how all your code looks at that time.
Files can be in one of three stages,
-Modified: we've made changes to it that we haven't committed yet
-Staged: Changes made to the files are 'ready' to be commited
-Committed: Changes made to files are stored in the git repository or VCS

Lets take a look at how the terminal may look when going thru git messages and status'
```
afk@ubuntu:/ /learn_git/checks$ git status
On branch main
nothing to commit, working tree clean
```
No changes were made when checking the status. Lets change the disk_usage.py file in the directory to add spaces.
```
afk@ubuntu:/ /learn_git/checks$ ls -l
total 4
-rwxrwxr-x 1 afk afk 544 Jan  2 19:47 disk_usage.py
afk@ubuntu:/ /learn_git/checks$ subl disk_usage.py
```
After making the change, lets check the 'git status' of the file.
``` 
afk@ubuntu:/ /learn_git/checks$ git status 
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   disk_usage.py

no changes added to commit (use "git add" and/or "git commit -a")
```
Since we made a change, but didn't have the disk_usage.py included to the 'git add' command, it shows up in red and tells us there are no changes added to the commit.
Let's change that and add this file to the 'git add' for staging.
```
afk@ubuntu:/ /learn_git/checks$ git add disk_usage.py 
afk@ubuntu:/ /learn_git/checks$ git status 
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    modified:   disk_usage.py
```
We can commit the file and add a commit message using the '-m' flag followed by the string of comments to add to the commit
```
afk@ubuntu:/ /learn_git/checks$ git commit -m 'Add periods to end of status messages'
[main 50cc3a2] Add periods to end of status messages
 1 file changed, 2 insertions(+), 2 deletions(-)
```

[+] Basic Git workflow
To make a new git repository, you start with the 'git init' command. Bam, you're done and created a new git repository for you to keep track of your files. Kinda.
You want to check how you are using the git repository and what your config may look like. You can check this by using the 'git config -l' command.
```
git config -l
user.email=cookcal.computech@gmail.com
user.name=KaiibottAI
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
```
```
afk@ubuntu:/ /learn_git/checks$ subl all_checks.py
afk@ubuntu:/ /learn_git/checks$ chmod +x all_checks.py
```
We created a new all_checks.py file in the git repository on our machine. Since this a new file, this means this is an 'untracked' file by git.
``` 
afk@ubuntu:/ /learn_git/checks$ git status 
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    all_checks.py

nothing added to commit but untracked files present (use "git add" to track)
```
To add the file to be tracked, and to the staged status, you need to use the 'git add' command followed by the file being tracked.
```
afk@ubuntu:/ /learn_git/checks$ git add all_checks.py 
afk@ubuntu:/ /learn_git/checks$ git status 
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    new file:   all_checks.py

afk@ubuntu:/ /learn_git/checks$ git commit
[main 5f5bbf0] This is the start of a skeleton python script
 1 file changed, 6 insertions(+)
 create mode 100755 all_checks.py
 ```
If you don't add a commit message, the commit is ignored and nothing changes.

[+]Useful Commit Messages
Writing a clear informative message is curcial to commit messages. Without this, you yourself can get lost. How do you think that would be to someone else who hasn't seen the code history?
A commit message can be generally broken down to a few parts.
The First part of the commit message should be a short summary of what was done. This is usually 50 characters or less
The Second part of the commit may include a more indepth show of what was changed. This is usally 72 characters or less.
The third part of the commit is only really added if the previous does not explain enough. This can include links to sources used but there is a reason for the short character length.

You can check the commit messages of a repository using the 'git log' command.
```
git log
commit 7d588778fc1b6fde6abc5377b49deb78a4321aae (HEAD -> main)
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Sun Jan 2 20:16:22 2022 -0800

    add a check_reboot function

commit 5f5bbf0aa7772d9f9529fb92176fc9548b24dd50
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Sun Jan 2 20:11:14 2022 -0800

    This is the start of a skeleton python script

commit 50cc3a2536adbccdf6e63f4cbcf3ba8ffe36129b
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Sun Jan 2 19:57:27 2022 -0800

    Add periods to end of status messages

commit 19cb63dba0db57afbc78cd1762029af3607f9d83
Author: KaiibottAI <cookcal.computech@gmail.com>
Date:   Sun Jan 2 19:49:47 2022 -0800
```