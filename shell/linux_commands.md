ls  
list files and folders in the current directory

ls -l  
list files and folders in the current directory with their attributes

ls -la  
list all files and folders in the current directory with their attributes

cd directory_to_change_into  
change directory

pwd  
return present working directory

mv file/folder destination_path/  
moves a file/folder to its destination path

cp file new_name/destination_path/  
copies a file to its destination path

-r  
recursive

cp -r folder new_name/destination_path/  
copies folder recursively to its destination path

rm filename  
remove a file from memory

rm -f filename  
removes a file from memory without giving any warning; if file doesn’t exist, it won’t complain

rm -rf files / folder  
removes multiple files or folders from memory recursively without any prompt

cat filename  
prints contents of a file onto terminal

> filename  
write into a file (overwrites)

>> filename  
append into a file (adds at the end)

| (pipe)  
pipe the output into the following command

command < filename  
redirects input from a file instead of the keyboard

grep "query"  
search query from the input

head -n 5  
print the first 5 lines from the file/output

tail -n 5  
print the last 5 lines from the file/output

mkdir foldername  
create a new directory and name it foldername

chmod numericcode filename  
changes read, write, execute privileges of a file

chown newowner filename  
changes ownership of a particular file

touch filename  
creates a new file named filename

nano filename  
opens text editor in terminal for a file named filename

echo "text"  
print text

history  
lists the history of commands you've used recently

whoami  
prints the current username on the terminal

man command
pulls up manual of that particular command

cut