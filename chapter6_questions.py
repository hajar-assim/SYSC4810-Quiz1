def get_chapter_6_questions():
    """Returns Chapter 6 questions - Software Security: Exploits and Privilege Escalation"""
    return {
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "What is the most exploitable aspect of weak memory management in software security?",
                    "options": {
                        "A": "Password storage",
                        "B": "Buffer overflows",
                        "C": "SQL injection",
                        "D": "Cross-site scripting"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Buffer overflows are the most exploitable aspect of weak memory management, involving indexing beyond the bounds of fixed-length buffers."
                },
                {
                    "num": 2,
                    "question": "What does TOCTOU stand for in the context of race conditions?",
                    "options": {
                        "A": "Transfer Of Control To Other Users",
                        "B": "Time-Of-Check to Time-Of-Use",
                        "C": "Type Of Conversion To Overflow Utility",
                        "D": "Timing Of CPU Thread Operations Unit"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "TOCTOU stands for Time-Of-Check to Time-Of-Use, describing race conditions where conditions may change between when a check is made and when an action is taken."
                },
                {
                    "num": 3,
                    "question": "In a TOCTOU privilege escalation attack, which system call uses the real UID for permission checking?",
                    "options": {
                        "A": "open()",
                        "B": "read()",
                        "C": "access()",
                        "D": "write()"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The access() syscall uses the process' real UID and GID for permission checking, whereas open() uses the effective UID (eUID)."
                },
                {
                    "num": 4,
                    "question": "What is the underlying problem that makes TOCTOU vulnerabilities exploitable?",
                    "options": {
                        "A": "Weak encryption",
                        "B": "Poor password policies",
                        "C": "Operations do not execute atomically",
                        "D": "Insufficient memory allocation"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The underlying problem is that the check and use operations do not execute atomically, allowing attackers to alter conditions between them."
                },
                {
                    "num": 5,
                    "question": "Why is simply disabling interrupts not a viable solution for preventing TOCTOU race conditions?",
                    "options": {
                        "A": "It would slow down the system too much",
                        "B": "Not all interrupts can be safely disabled, and multi-processor systems share resources",
                        "C": "Interrupts cannot be disabled in modern operating systems",
                        "D": "It would require recompiling all applications"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Not all interrupts can be safely disabled, not all processes can wait, and in multi-processor systems that share memory and resources, this may require disabling interrupts on all processors."
                },
                {
                    "num": 6,
                    "question": "What type of system calls are recommended to mitigate TOCTOU races instead of filename-based calls?",
                    "options": {
                        "A": "Encrypted system calls",
                        "B": "File descriptor-based system calls",
                        "C": "Network socket calls",
                        "D": "Kernel-level calls"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "System calls that deal directly with file descriptors are recommended because they are not subject to change, whereas filenames may be altered between operations."
                },
                {
                    "num": 7,
                    "question": "Which programming language family has the most significant problems with integer-based vulnerabilities?",
                    "options": {
                        "A": "Java family",
                        "B": "Python family",
                        "C": "C family",
                        "D": "Ruby family"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The C-family programming languages (including C++) have the biggest problems due to C's eagerness to allow operations between different data types and weak type safety."
                },
                {
                    "num": 8,
                    "question": "What extension method is used when converting an unsigned int to a wider type?",
                    "options": {
                        "A": "Sign extension",
                        "B": "Zero extension",
                        "C": "Truncation",
                        "D": "Bit shifting"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "An unsigned int is zero-extended (0-extended) when converted to a wider type, padding with zeros."
                },
                {
                    "num": 9,
                    "question": "What extension method is used when converting a signed int to a wider type?",
                    "options": {
                        "A": "Zero extension",
                        "B": "Truncation",
                        "C": "Sign extension",
                        "D": "Bit masking"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "A signed int is sign-extended when converted to a wider type, propagating the sign bit to preserve the value's sign."
                },
                {
                    "num": 10,
                    "question": "If an 8-bit unsigned char has value 0xFF (255) and is incremented, what value is stored?",
                    "options": {
                        "A": "256",
                        "B": "255",
                        "C": "0",
                        "D": "-1"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Due to integer overflow, C retains only the least significant 8 bits, so the value wraps around to 0."
                },
                {
                    "num": 11,
                    "question": "In the rate-limiting login example with a 4-bit signed integer, what decimal value does binary 1000 represent after overflow?",
                    "options": {
                        "A": "8",
                        "B": "0",
                        "C": "-8",
                        "D": "16"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "In two's complement representation, binary 1000 for a 4-bit signed integer represents -8, causing the rate-limiting check to fail."
                },
                {
                    "num": 12,
                    "question": "Which memory segment contains automatic (non-static) local variables and call frames?",
                    "options": {
                        "A": "Heap",
                        "B": "BSS",
                        "C": "Text",
                        "D": "Stack"
                    },
                    "answer": "D",
                    "points": 2,
                    "explanation": "The Stack segment contains automatic (non-static) local variables, call-by-value parameters, and call frames."
                },
                {
                    "num": 13,
                    "question": "Which memory segment is dynamically allocated under program control and grows upward?",
                    "options": {
                        "A": "Stack",
                        "B": "Heap",
                        "C": "Text",
                        "D": "Data"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The Heap is dynamically allocated under program control and grows upward by calls to memory management functions."
                },
                {
                    "num": 14,
                    "question": "What dangerous C function copies byte-for-byte without checking buffer bounds?",
                    "options": {
                        "A": "strncpy()",
                        "B": "memcpy_s()",
                        "C": "strcpy()",
                        "D": "safe_copy()"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The strcpy() function copies byte-for-byte from source to destination, stopping at NUL, without checking if the destination buffer is large enough."
                },
                {
                    "num": 15,
                    "question": "In stack-based buffer overflow attacks, what critical value is typically overwritten to redirect program control?",
                    "options": {
                        "A": "Stack pointer",
                        "B": "Return address",
                        "C": "Base address",
                        "D": "Segment register"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The return address stored in the stack frame is typically overwritten to redirect program control to attacker-chosen code."
                },
                {
                    "num": 16,
                    "question": "In heap-based buffer overflow attacks, what type of pointer can be overwritten to transfer control to attacker code?",
                    "options": {
                        "A": "Stack pointer",
                        "B": "Null pointer",
                        "C": "Function pointer",
                        "D": "File pointer"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "A function pointer holding the address of a function to be called can be overwritten, providing a simple way to transfer control to attacker-selected code."
                },
                {
                    "num": 17,
                    "question": "What attack technique places many copies of attacker code into the heap, often consuming 1-100 MB?",
                    "options": {
                        "A": "Stack smashing",
                        "B": "Heap spraying",
                        "C": "Return-oriented programming",
                        "D": "Format string attack"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Heap spraying places a large number of attacker code copies into the heap by allocating thousands of heap objects, consuming 1-100 MB."
                },
                {
                    "num": 18,
                    "question": "What sequence of instructions precedes shellcode in heap spraying to increase successful execution probability?",
                    "options": {
                        "A": "Jump sled",
                        "B": "NOP sled",
                        "C": "Return sled",
                        "D": "Call sled"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A long NOP (no-operation) sled precedes the shellcode, so any transfer landing in the sled will slide into the malicious shellcode."
                },
                {
                    "num": 19,
                    "question": "What defense technique flags specified address ranges as non-executable memory?",
                    "options": {
                        "A": "ASLR",
                        "B": "Stack canaries",
                        "C": "Data Execution Prevention (DEP)",
                        "D": "Bounds checking"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Data Execution Prevention (DEP) techniques mark memory regions as non-executable, provided by hardware (NX bit) or software."
                },
                {
                    "num": 20,
                    "question": "What are check-words inserted in stack frames to detect buffer overflow attacks called?",
                    "options": {
                        "A": "Guard pages",
                        "B": "Stack canaries",
                        "C": "Shadow values",
                        "D": "Sentinel bytes"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Stack canaries are check-words inserted in stack frames just below return addresses to detect buffer overflow attacks that corrupt adjacent memory."
                },
                {
                    "num": 21,
                    "question": "What defense approach copies return addresses to OS-managed data areas for verification before use?",
                    "options": {
                        "A": "Stack canaries",
                        "B": "DEP",
                        "C": "Shadow stacks",
                        "D": "ASLR"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Shadow stacks copy return addresses to OS-managed data areas and cross-check them for consistency before use."
                },
                {
                    "num": 22,
                    "question": "What defense randomizes the base addresses of stacks, heaps, and executables?",
                    "options": {
                        "A": "DEP",
                        "B": "Stack canaries",
                        "C": "ASLR",
                        "D": "Safe libraries"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "ASLR (Address Space Layout Randomization) randomizes the layout of objects in memory including base addresses for stacks, heaps, and executables."
                },
                {
                    "num": 23,
                    "question": "Which type of programming languages automatically enforce bounds on buffers including run-time checking?",
                    "options": {
                        "A": "Weakly-typed languages",
                        "B": "Assembly languages",
                        "C": "Scripting languages",
                        "D": "Type-safe languages"
                    },
                    "answer": "D",
                    "points": 2,
                    "explanation": "Strongly-typed or type-safe languages (e.g., Java, C#) tightly control data types and automatically enforce bounds on buffers."
                },
                {
                    "num": 24,
                    "question": "What is the first form of privilege escalation, moving from a compiled program to something allowing arbitrary command execution?",
                    "options": {
                        "A": "Kernel access",
                        "B": "Root access",
                        "C": "Shell access",
                        "D": "Network access"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Moving from the fixed functionality of a compiled program to a shell allows execution of arbitrary commands and other programs."
                },
                {
                    "num": 25,
                    "question": "What UID value represents superuser/root privileges that attackers seek to obtain?",
                    "options": {
                        "A": "1",
                        "B": "0",
                        "C": "-1",
                        "D": "1000"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "UID 0 represents root/superuser privileges. Moving from a non-root process to code running with UID 0 is a form of privilege escalation."
                },
                {
                    "num": 26,
                    "question": "What type of Unix program is owned by root but runs with elevated privileges when executed by regular users?",
                    "options": {
                        "A": "Daemon program",
                        "B": "Setuid program",
                        "C": "Kernel module",
                        "D": "Service program"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A setuid program is root-owned but runs with elevated privileges (effective UID of root) when executed by regular users."
                },
                {
                    "num": 27,
                    "question": "Rootkits may use buffer overflow for two purposes: to penetrate the system and to:",
                    "options": {
                        "A": "Encrypt files",
                        "B": "Maintain hidden presence",
                        "C": "Speed up performance",
                        "D": "Create backups"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Rootkits may use buffer overflow to: (1) Penetrate the system, and (2) Maintain hidden presence."
                },
                {
                    "num": 28,
                    "question": "Which memory segment contains program code and is typically read-only?",
                    "options": {
                        "A": "Stack",
                        "B": "Heap",
                        "C": "Text",
                        "D": "BSS"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The Text segment contains program code and is read-only with no buffers."
                },
                {
                    "num": 29,
                    "question": "What happens to high-order bits when converting an integer to a smaller width data type?",
                    "options": {
                        "A": "They are preserved",
                        "B": "They are sign-extended",
                        "C": "They are truncated",
                        "D": "They are zero-filled"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Conversion to a smaller width truncates high-order bits, potentially changing the value significantly."
                },
                {
                    "num": 30,
                    "question": "Why does DEP (Data Execution Prevention) not stop all memory safety violation attacks?",
                    "options": {
                        "A": "It is too slow to be effective",
                        "B": "It only works on 64-bit systems",
                        "C": "It prevents execution but not overwriting of memory",
                        "D": "It requires special hardware"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "DEP prevents execution but not overwriting of memory itself, so it does not stop all attacks involving memory safety violations."
                }
            ]
        },

        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 31,
                    "question": "Software security attacks are different from password stealing, web injection attacks, and malware spreading tactics.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Software security attacks exploit implementation errors and design flaws, which is distinct from password attacks, web injection, and malware tactics."
                },
                {
                    "num": 32,
                    "question": "Antiviruses and firewalls are the primary defenses against buffer overflow attacks.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Software security relies mainly on proper OS defenses and properly implemented applications, not antiviruses and firewalls which prevent malware."
                },
                {
                    "num": 33,
                    "question": "In TOCTOU attacks, the access() system call uses the effective UID (eUID) for permission checking.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The access() syscall uses the real UID and GID, while open() uses the effective UID (eUID)."
                },
                {
                    "num": 34,
                    "question": "Use of access() for permission checks in setuid programs is now largely discouraged.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Use of access() for such checks is now largely discouraged due to TOCTOU vulnerabilities."
                },
                {
                    "num": 35,
                    "question": "Integer-based vulnerabilities involve injection of executable code or scripts.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Integer-based vulnerabilities do not themselves involve injection of executable code, shell commands, or scripts. They are distinct from buffer overflow and code-injection attacks."
                },
                {
                    "num": 36,
                    "question": "C has strong type safety, which helps prevent buffer overflow vulnerabilities.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - C has weak type safety (is weakly-typed), which contributes to buffer overflow vulnerabilities."
                },
                {
                    "num": 37,
                    "question": "A char is converted to an int before any arithmetic operation in C.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - C automatically promotes char and short to int before arithmetic operations."
                },
                {
                    "num": 38,
                    "question": "Same-width data type conversions between signed and unsigned integers alter the bit pattern.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Same-width conversions between signed and unsigned integers do not alter any bits, only the interpretation changes."
                },
                {
                    "num": 39,
                    "question": "Integer overflow can affect program control flow by altering bounds tests on integer variables.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Since bounds tests on integer variables often dictate program branching and looping, an overflow affects control flow."
                },
                {
                    "num": 40,
                    "question": "The stack grows upward (toward higher memory addresses) on most systems.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The stack typically grows downward (toward lower memory addresses), while the heap grows upward."
                },
                {
                    "num": 41,
                    "question": "Unintentional buffer overflows always cause system crashes.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Unintentional buffer overflows may cause crashes, incorrect output, or no ill effects at all if the overwritten memory is unused."
                },
                {
                    "num": 42,
                    "question": "The heap and BSS segments have historically been left executable on many systems.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Many systems have left the heap and BSS not only writable (necessary) but also executable (unnecessary, dangerous)."
                },
                {
                    "num": 43,
                    "question": "Heap spraying attacks are always stopped by defenses that randomize heap layout.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Heap spraying is not stopped by defenses that randomize heap layout because the large number of copies increases hit probability."
                },
                {
                    "num": 44,
                    "question": "Heap spraying often uses JavaScript, which is a type-safe language.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Heap spraying often uses JavaScript (a type-safe language) and may not involve a buffer overflow."
                },
                {
                    "num": 45,
                    "question": "Stack canaries are placed above local variables in the stack frame.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - An extra canary field is inserted typically above local variables and below return addresses in stack frames."
                },
                {
                    "num": 46,
                    "question": "Backwards compatibility is a major barrier to adopting software security defenses.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Proposals that introduce interoperability problems with existing software face immediate opposition due to backwards compatibility concerns."
                },
                {
                    "num": 47,
                    "question": "Moving from UID 0 to kernel-mode privileges is the highest form of privilege escalation.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Moving from UID 0 privileges (user space process) to kernel-mode privileges represents the highest form of privilege escalation."
                },
                {
                    "num": 48,
                    "question": "A sandbox or filesystem jail provides access to the complete filesystem.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - A sandbox or filesystem jail is an isolated environment that prevents access to the complete filesystem."
                },
                {
                    "num": 49,
                    "question": "Static analysis tools can detect all memory management vulnerabilities without false alarms.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Static analysis tools miss some vulnerabilities and raise false alarms."
                },
                {
                    "num": 50,
                    "question": "C has no native string type, which is an example of weak type safety.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - C has no native string type, which is another example of weak type safety contributing to vulnerabilities."
                }
            ]
        },

        "section3": {
            "title": "Section 3: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 51,
                    "question": "What does BSS stand for in memory layout?",
                    "answer": ["block started by symbol", "block storage segment"],
                    "points": 2,
                    "type": "text",
                    "explanation": "BSS stands for Block Started by Symbol, also called the block storage segment. It contains global data that is uninitialized (zeroed on loading)."
                },
                {
                    "num": 52,
                    "question": "What byte value (in hex format like 0x00) signals end-of-string in C?",
                    "answer": ["0x00", "00", "nul", "null"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A NUL byte (0x00) signals the end of a character string in C."
                },
                {
                    "num": 53,
                    "question": "What is the bit length of a char data type in C?",
                    "answer": ["8", "8 bits", "eight"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The char data type uses 8 bits (one byte) and holds one character."
                },
                {
                    "num": 54,
                    "question": "What is the range of a signed 8-bit char in C? (Format: min to max)",
                    "answer": ["-128 to 127", "-128..127", "-128 127"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A signed char has a range of -128 to 127 using 8 bits in two's complement representation."
                },
                {
                    "num": 55,
                    "question": "What CPU register holds the address of the next instruction to execute?",
                    "answer": ["instruction pointer", "ip", "program counter", "pc", "eip", "rip"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The Instruction Pointer (IP) or Program Counter (PC) holds the address of the next instruction to execute."
                },
                {
                    "num": 56,
                    "question": "What register points to the current stack frame?",
                    "answer": ["frame pointer", "fp", "ebp", "rbp", "base pointer"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The Frame Pointer (FP) points to the current stack frame and is used to access local variables and parameters."
                },
                {
                    "num": 57,
                    "question": "What register points to the top of the stack?",
                    "answer": ["stack pointer", "sp", "esp", "rsp"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The Stack Pointer (SP) points to the top of the stack and changes as items are pushed or popped."
                },
                {
                    "num": 58,
                    "question": "What Unix command deletes a filename from the filesystem (used in TOCTOU attacks)?",
                    "answer": ["unlink", "unlink()"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The unlink() system call is used to delete a name from the filesystem."
                },
                {
                    "num": 59,
                    "question": "What Unix command creates a hard link between a filename and a target file?",
                    "answer": ["link", "link()"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The link() system call creates a new file entry that links to another file."
                },
                {
                    "num": 60,
                    "question": "What C library contains historical string-handling functions that lack bounds-checks?",
                    "answer": ["libc", "standard c library", "c library"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The standard C library (libc) contains historical string-handling functions like strcpy() that lack bounds-checks."
                },
                {
                    "num": 61,
                    "question": "What term describes C's lack of tight control over data types?",
                    "answer": ["weak type safety", "weakly typed", "weakly-typed", "weak typing"],
                    "points": 2,
                    "type": "text",
                    "explanation": "C is said to have weak type safety or be weakly-typed, allowing dangerous operations between different data types."
                },
                {
                    "num": 62,
                    "question": "What C functions are used for non-standard call sequences like exception-handling?",
                    "answer": ["setjmp longjmp", "setjmp/longjmp", "setjmp", "longjmp"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The setjmp/longjmp functions are used in non-standard call sequences such as exception-handling."
                },
                {
                    "num": 63,
                    "question": "What defense technique encodes pointers by XORing them with a secret value?",
                    "answer": ["pointer protection", "pointer encoding", "xor mask"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Pointer protection encodes pointers by XOR of a secret mask, so attacks may corrupt a pointer but not successfully control it."
                },
                {
                    "num": 64,
                    "question": "What does ASLR stand for?",
                    "answer": ["address space layout randomization"],
                    "points": 2,
                    "type": "text",
                    "explanation": "ASLR stands for Address Space Layout Randomization, which randomizes memory layout to thwart attacks."
                },
                {
                    "num": 65,
                    "question": "What does DEP stand for?",
                    "answer": ["data execution prevention"],
                    "points": 2,
                    "type": "text",
                    "explanation": "DEP stands for Data Execution Prevention, which marks memory regions as non-executable."
                }
            ]
        },

        "section4": {
            "title": "Section 4: Multi-Answer Short Answer (2 points each)",
            "questions": [
                {
                    "num": 66,
                    "question": "Name TWO of the three functional steps in buffer overflow exploits (separate with comma):",
                    "answer": ["code injection", "corruption", "seizure", "control flow", "location"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "The three steps are: (1) Code injection or location, (2) Corruption of control flow data, and (3) Seizure of control."
                },
                {
                    "num": 67,
                    "question": "Name TWO types of data that can be corrupted to alter program control flow (separate with comma):",
                    "answer": ["return address", "function pointer", "frame pointer", "vtable", "jump table", "dispatch table", "setjmp", "longjmp"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Control flow can be altered by corrupting: stack-based pointers (return addresses, frame pointers), function pointers, vtables, jump tables, dispatch tables, or setjmp/longjmp addresses."
                },
                {
                    "num": 68,
                    "question": "Name TWO forms of privilege escalation (separate with comma):",
                    "answer": ["shell", "sandbox", "uid 0", "root", "kernel", "filesystem"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Forms include: (1) Getting shell access, (2) Escaping sandbox/jail, (3) Getting UID 0/root, (4) Getting kernel-mode privileges."
                },
                {
                    "num": 69,
                    "question": "Name TWO defenses against buffer overflow attacks (separate with comma):",
                    "answer": ["dep", "aslr", "canary", "canaries", "shadow stack", "bounds checking", "type-safe", "safe library", "static analysis"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Defenses include: DEP, ASLR, stack canaries, shadow stacks, bounds checking, type-safe languages, safe C libraries, and static analysis tools."
                },
                {
                    "num": 70,
                    "question": "Name TWO adoption barriers for software security defenses (separate with comma):",
                    "answer": ["backwards compatibility", "backward compatibility", "legacy", "incomplete", "cost", "no governing body"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Barriers include: no single governing body, backwards compatibility issues, incomplete solutions, cost-benefit resistance, and legacy software."
                },
                {
                    "num": 71,
                    "question": "Name TWO memory segments that are typical buffer overflow targets (separate with comma):",
                    "answer": ["stack", "heap", "bss"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Buffer overflow attacks typically target the Stack, Heap, and BSS segments."
                },
                {
                    "num": 72,
                    "question": "Name TWO things software security defenses rely on (unlike malware defense) (separate with comma):",
                    "answer": ["os defense", "proper os", "application", "properly implemented", "operating system"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Software security relies mainly on proper OS defenses and properly implemented applications."
                },
                {
                    "num": 73,
                    "question": "Name TWO properties of integer types that cause vulnerabilities when different (separate with comma):",
                    "answer": ["width", "signedness", "signed", "unsigned", "size", "length"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Integer-based vulnerabilities arise from type conversions between integers of different widths and signedness (signed vs. unsigned)."
                },
                {
                    "num": 74,
                    "question": "Name TWO types of systems software historically written in C that face security issues (separate with comma):",
                    "answer": ["operating system", "network daemon", "interpreter", "os", "daemon", "kernel"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "C security issues have wide impact due to its use in operating systems, network daemons, and interpreters."
                },
                {
                    "num": 75,
                    "question": "Name TWO purposes rootkits may use buffer overflow for (separate with comma):",
                    "answer": ["penetrate", "hidden presence", "maintain", "system penetration", "hide"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Rootkits may use buffer overflow to: (1) Penetrate the system, and (2) Maintain hidden presence."
                }
            ]
        }
    }