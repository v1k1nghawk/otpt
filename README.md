# otpt
* _Purpose:_ Process syscalls tracing (with primary focus on a process output).
* _Usage:_ **otpt** PID [<u>SYSCALL</u>|**--all**]

    **PID** is a process identifier (get it by **ps afx** command).
    <u>SYSCALL</u> is a Linux system call (get it by **man syscalls** command). Alternativelly, one can use **--all** arg that shows all of a process syscalls.
    Without <u>SYSCALL</u> or **--all**, **otpt** utility shows a parameter of the **write** sycalls, which allows the utility to duplicate the entire output of the process with the specified **PID**.


---


* _Examples:_

_Example #1:_ otpt 28638 -all
_Example #2:_ otpt 28638 openat
_Example #3:_ otpt 28638
* _Internal force:_ Utility **strace** is used under the hood.

