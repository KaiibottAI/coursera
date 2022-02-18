Before you install Git
```
sudo apt update
sudo apt install git
git --version
```

To create a local git repo
```
mkdir my-git-repo
cd my-git-repo/
git init
```
The git init command creates a new Git repository. In our case, it transformed the current directory into a Git repository. It can also be used to convert an existing, unversioned project to a Git repository or to initialize a new, empty repository.

Executing git init creates a .git subdirectory in the current working directory, which contains all of the necessary Git metadata for the new repository. This metadata includes subdirectories for objects, refs, and template files. A HEAD file is also created which points to the currently checked out commit.

If you've already run git init on a project directory containing a .git subdirectory, you can safely run git init again on the same project directory. The operation is what we call idempotent; running it again doesn't override an existing .git configuration.

Git uses a username to associate commits with an identity. It does this by using the git config command. To set Git username use the following command
```
git config --global user.name "Caleb"
git config --global user.email "CourseraTestDum@course.com"
```

