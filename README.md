# otpt
* _Purpose:_ Process syscalls tracing (with primary focus on a process output).
* _Usage:_ **otpt** <ins>PID</ins> [<ins>SYSCALL</ins>|**--all**]

    <ins>PID</ins> is a process identifier (get it by **ps afx** command).<br/>
    <ins>SYSCALL</ins> is a Linux system call (get it by **man syscalls** command). Alternativelly, one can use **--all** arg that shows all of a process syscalls.<br/>
    Without <ins>SYSCALL</ins> or **--all**, **otpt** utility shows a parameter of the **write** sycalls, which allows the utility to duplicate the entire output of the process with the specified <ins>PID</ins>.


---


* _Examples:_

_Example #1:_ otpt 28638 --all<br/>
_Example #2:_ otpt 28638 openat<br/>
_Example #3:_ otpt 28638<br/>
* _Internal force:_ Utility **strace** is used under the hood.

