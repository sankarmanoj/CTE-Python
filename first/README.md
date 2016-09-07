Intro to Unix
===================

Points to Remember
------------------

Any file can be accessed through either its absolute position or the one relative to the current working directory.
For example a file in `/home/user/project/python` called *helloworld.py* can be opened by using `nano /home/user/project/python/helloworld.py`, regardless of current working directory. If the current working directory is the home folder, i.e. `/home/user`, then it can be opened by `nano project/python/helloworld.py`

**Tilde operator ~** This refers to the home directory of the current user.  `/home/user/hello.txt` can also be referred to as `~/hello.txt`.  It takes the value of the path stored in $HOME

__Wildcard operator - * and ? __
`*` can be used to match with none or any  length of characters in a file or directory name.
`?` will match with exactly one character.

Example - Consider you have many python files in a directory `~/project/python/` , which need to copied to `~/project/`. This can be achieved by using `cp ~/project/python/*.py ~/project/`. In this case, `*.py` referee to any file ending with py

**Tab Key**
The tab key can be used to autocomplete paths to folders. For example, if you have typed `cp pro` and hit tab, and if there is only one file or folder that starts with pro, i.e. projects, then it will autocomplete to `cp projects`. In case there are multiple files or folders that start with pro,or if there are none, the first time you hit nothing will happen, except for an audible bell. If you hit tab again in quick succession, it will show all possible options if there are multiple options.

**Environment variables**
These are variables that can be accessed by any program, and can change the behaviour of either the OS or other programs.
Type `export` to list all environment variables.
Commonly used environment variables are

- HOME - Location of user's home directory in the filesystem
- PATH - a list of directory paths. When the user types a command into a system terminal without providing the full path, this list is checked to see whether it contains a path that leads to the command. It can contain multiple paths, which need to be separated by a :
- EDITOR - Default editor used by the OS

These variables can be edited by using the export command.
For example, to change HOME, use `export HOME=<new-directory>`
To append a directory to PATH use `export PATH=$PATH:<new-directory>`


## List of Common Commands ##
- ls
- cd
- pwd
- mkdir
- rm
- rmdir
- touch
- cat
- chmod
- chown
- cp
- mv
- grep
- find
- whoami
- kill / killall
- ssh

------
Description of Selected Commands
-------------
**man** - The most important command. It gives the manual page for any other command. Type
`man <name-of-command>` to see that commands man page. It is highly recommended that you try looking at the man page of most commands.

**pwd** - It stands for Print Working Directory.

**mkdir** - Make directory. `mkdir <name-of-directory>` . `enter code here`

**cp** - Copy.  `cp <input-file> <output-file>` . You can use the -R flag to copy directories. `cp -R <input-directory> <name-of-output-directory>`

**mv** - Move. This implements the same functionality as cut-and-paste.  `mv <input-file> <output-file>` . You can use the -R flag to move directories. `mv -R <input-directory> <name-of-output-directory>`

**rm** - Remove. This deletes files. `rm <file-to-be-deleted>`. To delete folders, recursively, use `rm -rf <folder-to-be-deleted>` . In this command *r* is for recursive and *f* is for force delete.

**touch** - Create an empty file. `touch <empty-file-that-is-created>`
