# Coursera - Troubleshooting and Debugging

## Week 1

### Intro to Debugging
Debugging - The process of identifying, analyzing, and removing bugs in a system
Tools like "tcpdump" and "Wireshark" can help us with network analyzing tools
Tools like "ps", "top", or "free" can show us the number and types of resources used in the system.
We can use a tool like "strace" to look at the system calls made by a program, or "ltrace" to look at the library calls made by the software.

Step 1. Reproduction Case / Gathering Information
Step 2. Find Root Cause
Step 3. Preform remediation / Long-term remediation

-Document everything you did/do

Tool - strace
Example: strace -o %outputfile% %filename% (This allows the output to be directed to a file for later investigation)
Exapmle: strace %filename% | less (This allows the output to be in terminal)

### Understanding the Problem

When reading logs, there are different locations for the issues.
On Linux, you may use "/var/log/syslog", for user specific logs ".xsession-errors"
On MacOS, "/Library/Logs"
On Windows, "Event Viewer" tool
```
Linux commands
iotop - a tool similar to top that lets us see which processes are using the most input and output
iostat - show statistics on the input/output operations
vmstat - show statistics on the virtual memory operations
ionice - reduce process priority
iftop - shows the current traffic on the network interfaces
rsync - used for backing up data
rsync -bwlimit - limits bandwidth consumption with rsync
nice - reduce priority in accessing CPU
```
Werner Hiesenberg
The Hiesenberg or Observer Effect: Observing a phenomenon alters the phenomenon

### Binary Searching a Problem

Sort a search before using Binary Search algorithim
This reduces the time it takes to search thru a list by its base 10 number
a list of 1000 items takes 10 searches

#### Example from Quiz
```
def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False
  list.sort() # This has to be added to srot the list FIRST before doing a binary search
  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)
    
  return False

#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
```

```
def binary_search(list, key):
    #Returns the position of key in the list if found, -1 otherwise.

    #List must be sorted:
    list.sort()
    left = 0
    right = len(list) - 1

    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            print("Checking the left side")
            right = middle - 1
        if list[middle] < key:
            print("Checking the right side")
            left = middle + 1
    return -1 

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
"""Should print 2 debug lines and the return value:
Checking the left side
Checking the left side
0
"""

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
"""Should print no debug lines, as it's located immediately:
4
"""

print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the left side
Checking the right side
6
"""

print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
"""Should print 3 debug lines and the return value:
Checking the right side
Checking the right side
Checking the right side
9
"""

print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
"""Should print 4 debug lines and the "not found" value of -1:
Checking the right side
Checking the right side
Checking the right side
Checking the right side
-1
"""
```

Helpful linux commands to do a manual bisect search
```
wc -l /print the amount of lines in a file
head -15 /print the FIRST 15 lines
tail -20 /print the LAST 20 lines
```

bisecting a problem is cutting the amount of tests in half to find if your half of thr problem exists in the certain subset of data. If it does, cut in half again and again until the error is in the unique subset of data.
100 computers = 50 in the first, 50 in the last
50 computers = 25 in the first, 25 in the last
25 = 13 in the first, 12 in the last
12 = 6 and 6
and so on until you narrow the issue out.

Example from Quiz
```
def linear_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #Initialize the counter of steps
    steps=0
    for i, item in enumerate(list):
        steps += 1
        if item == key:
            break
    return steps 

def binary_search(list, key):
    #Returns the number of steps to determine if key is in the list 

    #List must be sorted:
    list.sort()
    #The Sort was 1 step, so initialize the counter of steps to 1
    steps=1

    left = 0
    right = len(list) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        
        if list[middle] == key:
            break
        if list[middle] > key:
            #steps +=1
            right = middle - 1
        if list[middle] < key:
            #steps +=1
            left = middle + 1
        #steps +=1
    return steps 

def best_search(list, key):
    steps_linear = linear_search(list, key)
    steps_binary = binary_search(list, key)
    results = "Linear: " + str(steps_linear) + " steps, "
    results += "Binary: " + str(steps_binary) + " steps. "
    if (steps_linear < steps_binary):
        results += "Best Search is Linear."
    elif (steps_linear > steps_binary):
        results += "Best Search is Binary."
    else:
        results += "Result is a Tie."

    return results

print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.

print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.

print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.

print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.

print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.
```

## Week 2

### Understanding Slowness
Speed in rank
CPU > RAM > SDD/HDD > Network

linux commands
```
top / top - display Linux processes
nice / nice - run a program with modified scheduling priority
renice / renice - alter priority of running processes
pidof / pidof -- find the process ID of a running program.
ps / ps - report a snapshot of the current processes.
```

If you notice there is a process that is taking a lot of the processing power and isn't playing "nice", you can use the renice command 
Example:
```
for pid in $(pidof %processname%); do renice 19 $pid; done
```
The above example will iterate over pid (process ID) as a variable. Using the "pidof" command (pidof -- find the process ID of a running program.) and pass the name of the pid to find its process ID, next it will change the nice of the pid (nice - run a program with modified scheduling priority)

If you change the nice levels of processes but still notice slugishness, you can find why the processes are doing what they are using the "ps ax" command (To see every process using the BSD syntax)
You can search inside the command with the "/" search key first, then enter what you are looking for.
Once you narrow down what you are looking for, you can use the "locate" command in linux as well to find certain files/folders.
```
locate command was an install with 'sudo apt install plocate'
```

### Slow Code


### When Slowness Problems Get Complex

## Module Quiz
```
import psutil
psutil.cpu_percent()
psutil.disk_io_counters()
psutil.net_io_counters()
```
Below is a script used from the quiz
```
multisync.py 
    #!/usr/bin/env python3
    from multiprocessing import Pool
    def run(task):
      # Do something with task here
        print("Handling {}".format(task))
    if __name__ == "__main__":
      tasks = ['task1', 'task2', 'task3']
      # Create a pool of specific number of CPUs
      p = Pool(len(tasks))
      # Start each task within the pool 
      p.map(run, tasks)
```
The qwick labs was apparently broken by the users it seems, here was the "answer" they wanted
```
#!/usr/bin/env python3
from multiprocessing import Pool
import multiprocessing
import subprocess
import os
home_path = os.path.expanduser('~')
src = home_path + "/data/prod/"
dest = home_path + "/data/prod_backup/"
if __name__ == "__main__":
    pool = Pool(multiprocessing.cpu_count())  
    pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
```