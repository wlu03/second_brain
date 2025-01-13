Some operating systems support aliases for file which act as alternative name or references. These aliases may represent either the actual file content or just the filename. For example the `ln` command (stands for link) in **UNIX** creates an alias to an existing file: 
$$\text{ln foo bar}$$
This results an alias **bar** to access the contents of an existing file named **foo**. This is referred as a **hard link** gives an equal status to the new name **bar** as **foo**. If we delete file foo, the contents of the file are accessible through **bar**. 
![[Screenshot 2024-11-13 at 8.04.49 PM.png]]
**Soft Link** is a type of file that points to another file or directory in a file system. A soft link points to the path of the target file or directory.  For example, in UNIX the command $$\text{ln -s foo bar}$$
Creates an alias named bar for foo. However, it doesn't point to the file contents but the name itself. The size of foo is 80 bytes while bar is just the name of the string foo (3 bytes). Deletion of `foo` results in the removal of the file contents. The name `bar` still exists, but its alias `foo` and the file contents do not. Trying to access the file named `bar` results in an access error.

**Problems**
___
However, a hard link to a directory can lead to circular lists, which can make deletion operations of directories very difficult. For this reason, operating systems such as Unix disallow creating hard links to directories.



