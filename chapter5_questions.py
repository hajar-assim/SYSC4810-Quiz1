def get_chapter_5_questions():
    """Returns Chapter 5: Operating Systems Security and Access Control questions"""
    return {
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "What is the primary purpose of memory isolation in operating systems?",
                    "options": {
                        "A": "To speed up program execution",
                        "B": "To prevent one process from writing into another's memory",
                        "C": "To increase available RAM",
                        "D": "To enable faster disk access"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Memory isolation prevents one process from writing into another's memory, protecting both against benign errors and malicious programs."
                },
                {
                    "num": 2,
                    "question": "In the memory descriptor register mechanism, what does the 'base' value represent?",
                    "options": {
                        "A": "The total memory size available",
                        "B": "The highest physical memory address accessible",
                        "C": "The lowest physical memory address accessible to the active process",
                        "D": "The number of processes running"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The base value represents the lowest physical memory address accessible to the active process, while the bound specifies how many addressable words from that point."
                },
                {
                    "num": 3,
                    "question": "Which entity is responsible for loading the memory descriptor register?",
                    "options": {
                        "A": "Any user program",
                        "B": "Only the supervisor program",
                        "C": "The hardware automatically",
                        "D": "The network driver"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Only the supervisor program can load the descriptor register. The supervisor program has its privileged bit set, giving it this capability."
                },
                {
                    "num": 4,
                    "question": "What is a major disadvantage of simple memory-range protection using descriptor registers?",
                    "options": {
                        "A": "It's too slow for modern systems",
                        "B": "It provides an all-or-nothing mode with no fine-grained sharing",
                        "C": "It requires too much hardware",
                        "D": "It doesn't work with virtual memory"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The main disadvantage is providing an all-or-nothing mode - either full access as supervisor or no cross-process sharing at all. It lacks fine-grained sharing of memory."
                },
                {
                    "num": 5,
                    "question": "In memory segments, what does a segment descriptor contain?",
                    "options": {
                        "A": "Only the segment number",
                        "B": "Only the word offset",
                        "C": "Physical starting address, current size, and access control indicator",
                        "D": "User password and encryption key"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Each segment descriptor contains a segment's physical starting address, current size, and an access control indicator specifying permission bits for the memory segment."
                },
                {
                    "num": 6,
                    "question": "In segment access control indicators, what does the X bit represent when set to 1?",
                    "options": {
                        "A": "The segment may be written into",
                        "B": "The segment is executable",
                        "C": "Only the supervisor has read access",
                        "D": "All access attempts trap to supervisor"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "When X=1, the segment is executable. Usually when X=1, W=0 since code is typically not self-modifying."
                },
                {
                    "num": 7,
                    "question": "What is the purpose of the F (fault) bit in segment descriptors?",
                    "options": {
                        "A": "To indicate file system errors",
                        "B": "To mark segments for garbage collection",
                        "C": "To cause all access attempts to trap to supervisor, overriding other bits",
                        "D": "To enable faster access"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "When F=1, all access attempts trap to supervisor. This overrides all other bits in the access control indicator."
                },
                {
                    "num": 8,
                    "question": "What determines process access privileges in Unix-like systems?",
                    "options": {
                        "A": "Process ID (PID)",
                        "B": "User ID (UID)",
                        "C": "MAC address",
                        "D": "IP address"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The UID is the primary basis for granting access privileges to resources. PIDs are used for OS-internal purposes like scheduling."
                },
                {
                    "num": 9,
                    "question": "According to the reference monitor concept, what must validate all references to programs, data, or devices?",
                    "options": {
                        "A": "The user",
                        "B": "The network firewall",
                        "C": "A list of authorized types of reference based on user/program function",
                        "D": "The CPU cache"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The reference monitor concept states that all references must be validated against a list of authorized types of reference based on user and/or program function."
                },
                {
                    "num": 10,
                    "question": "What does an Access Control Entry (ACE) A(i, j) specify?",
                    "options": {
                        "A": "The IP address of subject i",
                        "B": "The permissions subject i has to object j",
                        "C": "The encryption key for object j",
                        "D": "The password for user i"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Access control entry A(i, j) specifies the permissions that subject i has to object j in the access matrix model."
                },
                {
                    "num": 11,
                    "question": "What are the three requirements for a reference validation mechanism according to security requirements?",
                    "options": {
                        "A": "Fast, cheap, and reliable",
                        "B": "Tamper-proof, always invoked, and verifiable",
                        "C": "Encrypted, compressed, and distributed",
                        "D": "Open source, documented, and tested"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The reference validation mechanism must be tamper-proof, always invoked (not circumventable), and verifiable (small enough to be subject to complete analysis and tests)."
                },
                {
                    "num": 12,
                    "question": "What is a capabilities list (C-list)?",
                    "options": {
                        "A": "A list of all users in the system",
                        "B": "A decomposition of the access matrix by row, detailing all access privileges a subject holds",
                        "C": "A list of all objects in the system",
                        "D": "A list of encryption algorithms"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A capabilities list is derived from a row of the access matrix, providing a list of tuples (j, A(i,j)) that details all access privileges subject i holds."
                },
                {
                    "num": 13,
                    "question": "What is the main advantage of the ugo (user-group-other) permission model over ACLs?",
                    "options": {
                        "A": "More expressive permissions",
                        "B": "Fixed-size metadata entries saving storage and processing time",
                        "C": "Better security",
                        "D": "Easier to implement ACLs on top of it"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The ugo model allows fixed-size filesystem metadata entries, saving storage and processing time. ACLs may involve arbitrary-length lists."
                },
                {
                    "num": 14,
                    "question": "In Unix, what does UID=0 signify?",
                    "options": {
                        "A": "A regular user",
                        "B": "A guest account",
                        "C": "A superuser process with access to all file resources",
                        "D": "A disabled account"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "A process running with UID=0 is a superuser process, granted access to all file resources independent of protection settings."
                },
                {
                    "num": 15,
                    "question": "When a user process requests access to a file, in what order are permission checks made?",
                    "options": {
                        "A": "Others, group, user",
                        "B": "Group, user, others",
                        "C": "User, group, others",
                        "D": "Random order"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Permission checks are made in sequence: user, then group, then others. The first qualifying category determines privileges."
                },
                {
                    "num": 16,
                    "question": "What does the setuid bit do when set on an executable file?",
                    "options": {
                        "A": "Makes the file read-only",
                        "B": "Temporarily sets the executing process's userid to the file owner's userid",
                        "C": "Encrypts the file",
                        "D": "Deletes the file after execution"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "When a setuid executable runs, the OS temporarily sets the process's effective userid to that of the file's owner, allowing access to resources the calling process might not otherwise have."
                },
                {
                    "num": 17,
                    "question": "What is the purpose of the sticky bit (t-bit) on a directory?",
                    "options": {
                        "A": "To make files in the directory read-only",
                        "B": "To prevent deletion or renaming of files owned by other users",
                        "C": "To encrypt all files in the directory",
                        "D": "To compress files automatically"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The sticky bit on a directory prevents deletion or renaming of files owned by other users. Only the directory owner and root can still delete files."
                },
                {
                    "num": 18,
                    "question": "For directory permissions, what does the X permission allow?",
                    "options": {
                        "A": "Listing directory contents",
                        "B": "Modifying directory contents",
                        "C": "Traversing and searching the directory",
                        "D": "Deleting the directory"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "For directories, X allows traversing and searching the directory, including setting it as the working directory and accessing files' inode metadata."
                },
                {
                    "num": 19,
                    "question": "What happens when a symbolic link's target file is deleted?",
                    "options": {
                        "A": "The symbolic link is automatically deleted",
                        "B": "The symbolic link becomes stale and cannot be resolved",
                        "C": "The symbolic link still works",
                        "D": "The system crashes"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "When the target file of a symbolic link is deleted, the symlink becomes stale (broken) and cannot be resolved, while a hardlink would still work."
                },
                {
                    "num": 20,
                    "question": "In RBAC (Role-Based Access Control), how are permissions assigned?",
                    "options": {
                        "A": "Directly to individual users",
                        "B": "Based on user roles, with each role having pre-assigned permissions",
                        "C": "Based on file creation time",
                        "D": "Randomly by the system"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "In RBAC, permissions are assigned based on user roles. A user is assigned one or more roles, and each role has pre-assigned permissions that determine the user's access."
                }
            ]
        },

        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 21,
                    "question": "In Unix, a process identifier (PID) is the primary basis for granting access privileges to resources.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The UID (User ID) is the primary basis for granting access privileges. PIDs are used for OS-internal purposes like scheduling."
                },
                {
                    "num": 22,
                    "question": "The supervisor program runs with the privileged bit set.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - A supervisor program has its privileged bit set, which allows it to perform restricted operations like loading the descriptor register."
                },
                {
                    "num": 23,
                    "question": "In the ugo model, if a file owner doesn't have read permission but 'others' does, the owner can still read the file.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Permission checks are made in sequence (user, group, others). If the owner category doesn't grant permission, access is denied even if others would grant it."
                },
                {
                    "num": 24,
                    "question": "The security kernel concept has been widely implemented in mainstream operating systems.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The security kernel is still uncommon more than 50 years after its conceptualization. Mainstream OSes remain typically monolithic."
                },
                {
                    "num": 25,
                    "question": "Multiple users sharing the same username is considered good security practice.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Sharing the same username is poor security hygiene as it hinders accountability. Protection groups are the preferred alternative for sharing resources."
                },
                {
                    "num": 26,
                    "question": "A process's effective UID (eUID) determines privileges on resource access requests.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The eUID determines privileges on resource access requests and is used to set file owner on created files."
                },
                {
                    "num": 27,
                    "question": "The string 'root' is what determines superuser permissions in Unix.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - It is the UID value of 0, not the string name 'root', that determines superuser permissions."
                },
                {
                    "num": 28,
                    "question": "In Unix, deleting a hardlinked file by specifying a particular directory entry always deletes the file content.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The file content (including inode) is deleted only when its link-count drops to zero. Other hardlinks may still reference the file."
                },
                {
                    "num": 29,
                    "question": "A setuid program owned by root is of special interest to attackers.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Setuid programs, especially when owned by root, are high-value targets for attackers as they run with elevated privileges."
                },
                {
                    "num": 30,
                    "question": "The W permission alone on a directory allows altering its contents.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - W permission on a directory allows altering contents only when X permission is also held. W alone is insufficient."
                },
                {
                    "num": 31,
                    "question": "In Multics and Unix, everything was treated as a file to simplify input-output operations.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - This design simplifies I/O operations across peripheral devices. For example, printing is done by writing bytes to an address identified with a printing device."
                },
                {
                    "num": 32,
                    "question": "A child process gets a new UID when created via fork().",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The child inherits the parent's userids (rUID, eUID, sUID) but gets a new process ID (PID)."
                },
                {
                    "num": 33,
                    "question": "DAC (Discretionary Access Control) allows resource owners to determine permissions for their resources.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - In DAC, it is at the resource owner's discretion what permissions to grant others regarding that resource."
                },
                {
                    "num": 34,
                    "question": "The reference monitor must be circumventable to allow for emergency access.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - One of the key requirements for the reference validation mechanism is that it must be always invoked (not circumventable)."
                },
                {
                    "num": 35,
                    "question": "The umask's on bits (1) specify permissions to remove from default permissions.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The umask's on bits specify permissions to remove from default permissions. For example, if umask is 022 and default is 666, the result is 644."
                },
                {
                    "num": 36,
                    "question": "An Access Control List (ACL) is derived from a column of the access matrix.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - An ACL is derived from a column of the access matrix, listing all subjects permitted access to a particular object."
                },
                {
                    "num": 37,
                    "question": "Hardlinking directories is encouraged in Unix systems.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Hardlinking directories is discouraged or disallowed for technical reasons, such as the potential to create directory loops."
                },
                {
                    "num": 38,
                    "question": "The M (mode) bit in segment descriptors is valid only when X=1.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The M bit, which sets supervisor mode when executing a segment, is valid only when X=1 (the segment is executable)."
                },
                {
                    "num": 39,
                    "question": "A world-writable root-owned setuid executable is considered a serious security vulnerability.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - This is extremely dangerous because any process could replace the contents with malicious code that would run with root privileges."
                },
                {
                    "num": 40,
                    "question": "RBAC is purely a MAC (Mandatory Access Control) system.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - RBAC is neither purely MAC nor DAC. It assigns permissions based on roles, which reflects how permissions are often assigned in larger organizations."
                }
            ]
        },

        "section3": {
            "title": "Section 3: Scenario-Based Questions (3 points each)",
            "questions": [
                {
                    "num": 41,
                    "question": "Alice and Bob belong to group 'wonderland'. Charlie does not. Given file permissions: rw-r----- alice wonderland foo.txt, what permissions does Charlie have?",
                    "options": {
                        "A": "Read and write",
                        "B": "Read only",
                        "C": "No permissions",
                        "D": "Execute only"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "Charlie is not the owner (alice) and not in group wonderland, so he falls into 'others' category which has no permissions (---) in this case."
                },
                {
                    "num": 42,
                    "question": "A file has permissions -rwsr-xr-x owned by root. When a regular user executes this file, what privileges will the process have?",
                    "options": {
                        "A": "The regular user's normal privileges",
                        "B": "Root privileges due to the setuid bit",
                        "C": "No privileges",
                        "D": "Only read privileges"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "The 's' in the owner's execute position indicates setuid is set. When executed, the process's effective UID becomes root's UID, granting root privileges."
                },
                {
                    "num": 43,
                    "question": "If the default permission for regular files is 666 and umask is 027, what will be the initial permission of a newly created file?",
                    "options": {
                        "A": "666",
                        "B": "640",
                        "C": "644",
                        "D": "600"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "666 (binary: 110 110 110) minus umask 027 (binary: 000 010 111) = 640 (rw-r-----). The umask removes permissions from the default."
                },
                {
                    "num": 44,
                    "question": "A directory has permissions drwxrwxrwt. What does the 't' in the last position indicate?",
                    "options": {
                        "A": "The directory is temporary",
                        "B": "The sticky bit is set, preventing users from deleting others' files",
                        "C": "The directory is encrypted",
                        "D": "All files are executable"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "The 't' indicates the sticky bit is set. This prevents users from deleting or renaming files owned by other users, commonly used on /tmp."
                },
                {
                    "num": 45,
                    "question": "User Alice creates a symlink: ln -s /home/alice/secret.txt /tmp/link. If Alice later deletes /home/alice/secret.txt, what happens when Bob tries to access /tmp/link?",
                    "options": {
                        "A": "Bob can read the file normally",
                        "B": "The symlink is automatically deleted",
                        "C": "The symlink fails because the target cannot be resolved",
                        "D": "Bob gets the old file contents from cache"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "When a symlink's target is deleted, the symlink becomes stale and cannot be resolved. Unlike hardlinks, symlinks depend on the target pathname existing."
                }
            ]
        },

        "section4": {
            "title": "Section 4: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 46,
                    "question": "What does DBR stand for in memory segment management?",
                    "answer": ["descriptor base register", "dbr"],
                    "points": 2,
                    "type": "text",
                    "explanation": "DBR stands for Descriptor Base Register, which points to the descriptor segment of the active process."
                },
                {
                    "num": 47,
                    "question": "What does ACL stand for in access control?",
                    "answer": ["access control list", "acl"],
                    "points": 2,
                    "type": "text",
                    "explanation": "ACL stands for Access Control List, which is derived from a column of the access matrix and lists all subjects permitted access to an object."
                },
                {
                    "num": 48,
                    "question": "What does RBAC stand for?",
                    "answer": ["role-based access control", "role based access control", "rbac"],
                    "points": 2,
                    "type": "text",
                    "explanation": "RBAC stands for Role-Based Access Control, where permissions are assigned based on user roles rather than individual identities."
                },
                {
                    "num": 49,
                    "question": "What does MAC stand for in access control?",
                    "answer": ["mandatory access control", "mac"],
                    "points": 2,
                    "type": "text",
                    "explanation": "MAC stands for Mandatory Access Control, where a security policy administrator defines for every object which subjects have which permissions."
                },
                {
                    "num": 50,
                    "question": "What does DAC stand for?",
                    "answer": ["discretionary access control", "dac"],
                    "points": 2,
                    "type": "text",
                    "explanation": "DAC stands for Discretionary Access Control, where resource owners decide what permissions to grant others."
                },
                {
                    "num": 51,
                    "question": "What command is used to set Access Control Lists on files in Unix? (provide the command name only)",
                    "answer": ["setfacl"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The setfacl command is used to set ACLs on files, e.g., setfacl -m u:bob:r foo"
                },
                {
                    "num": 52,
                    "question": "What command is used to view Access Control Lists on files in Unix? (provide the command name only)",
                    "answer": ["getfacl"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The getfacl command is used to view ACLs on files."
                },
                {
                    "num": 53,
                    "question": "What does eUID stand for?",
                    "answer": ["effective userid", "effective user id", "effective uid", "euid"],
                    "points": 2,
                    "type": "text",
                    "explanation": "eUID stands for effective userid, which determines privileges on resource access requests."
                },
                {
                    "num": 54,
                    "question": "Name TWO types of accesses in the access matrix model (separate with comma):",
                    "answer": ["read", "write", "execute", "wakeup", "terminate", "search", "delete"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Types of accesses include: read, write (for data/memory), execute (for code), wakeup, terminate (for processes), search (for directories), and delete (for files)."
                },
                {
                    "num": 55,
                    "question": "Name TWO supporting functions required by the reference monitor (separate with comma):",
                    "answer": ["authentication", "hardware", "physical security", "input-output security", "communication", "trustworthy"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "The reference monitor requires: trustworthy authentication, properly operating hardware, physical security, and security of I/O communication paths."
                }
            ]
        }
    }