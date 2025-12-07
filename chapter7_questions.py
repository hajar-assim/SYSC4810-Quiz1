def get_chapter_7_questions():
    """Returns Chapter 7: Malicious Software (Malware) questions"""
    return {
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "What is the definition of malware?",
                    "options": {
                        "A": "Any software that contains bugs or errors",
                        "B": "Software intentionally designed to have effects contrary to the best interests of users",
                        "C": "Software that runs slowly on a computer",
                        "D": "Any software downloaded from the internet"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Malware is software intentionally designed or deployed to have effects contrary to the best interests of users, including potential damage related to resources or systems. Harmful software due to unintentional design or implementation errors is NOT considered malware."
                },
                {
                    "num": 2,
                    "question": "Which of the following is NOT a way computers typically get infected with malware?",
                    "options": {
                        "A": "Drive-by downloads from compromised websites",
                        "B": "Clicking on links in phishing emails",
                        "C": "Reading a plain text email without attachments",
                        "D": "Downloading executables that have been repackaged with malware"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Simply reading a plain text email without attachments or links is generally safe. Malware spreads through executable content, malicious links, compromised downloads, and exploiting vulnerabilities - not plain text content."
                },
                {
                    "num": 3,
                    "question": "Why is malware identification considered an undecidable problem?",
                    "options": {
                        "A": "Because malware is always encrypted",
                        "B": "Because what constitutes malware depends on context, not functionality alone",
                        "C": "Because computers are not fast enough to analyze all software",
                        "D": "Because users cannot agree on what is harmful"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Malware identification is undecidable because context determines whether software is malicious. For example, SSH server software is not generally malware, but becomes malicious if installed by an attacker for covert access."
                },
                {
                    "num": 4,
                    "question": "What is a key difference between how viruses and worms spread?",
                    "options": {
                        "A": "Viruses spread over networks while worms require human action",
                        "B": "Viruses require some form of human action while worms spread automatically over networks",
                        "C": "Viruses only affect Windows while worms affect all operating systems",
                        "D": "Viruses encrypt files while worms delete them"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Viruses spread aided by human action (e.g., inserting USB, clicking email attachments) and infect host programs. Worms propagate automatically and continuously without user interaction, spreading across machines over networks by exploiting vulnerabilities."
                },
                {
                    "num": 5,
                    "question": "What is a 'drive-by download'?",
                    "options": {
                        "A": "A download that occurs while driving a vehicle",
                        "B": "Software installation that occurs from a site visit without user knowledge",
                        "C": "A download that requires multiple clicks to complete",
                        "D": "A download from a USB drive"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A drive-by download is when a site visit results in software installation without user knowledge. This typically exploits browser vulnerabilities or applications that browsers invoke to process content."
                },
                {
                    "num": 6,
                    "question": "Which virus stage defines the functionality delivered by the malware?",
                    "options": {
                        "A": "Dormancy",
                        "B": "Propagation",
                        "C": "Trigger condition",
                        "D": "Payload"
                    },
                    "answer": "D",
                    "points": 2,
                    "explanation": "The Payload stage defines the functionality delivered by the malware. This can range from non-critical (e.g., an image walking across the screen) to severe (e.g., erasing files or damaging hardware)."
                },
                {
                    "num": 7,
                    "question": "What made the CIH Chernobyl virus particularly destructive?",
                    "options": {
                        "A": "It could only spread through email",
                        "B": "It demonstrated malware can cause hardware damage by writing to system BIOS firmware",
                        "C": "It was the first virus ever created",
                        "D": "It required administrator access to run"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "CIH demonstrated that malware can cause hardware as well as software damage. It overwrote critical hard disk sectors and attempted to write to the system BIOS firmware, causing machines to not start and requiring Flash BIOS chip replacement."
                },
                {
                    "num": 8,
                    "question": "Why was the CIH virus also called 'Spacefiller'?",
                    "options": {
                        "A": "It filled disk space with junk files",
                        "B": "It inserted into unused bytes within files and split itself across files as necessary",
                        "C": "It displayed images of outer space",
                        "D": "It only infected files with extra space at the end"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "CIH was called Spacefiller because it inserted into unused bytes within files (in file formats that pad up to block boundaries) and split itself across such files as necessary, defeating anti-virus programs that look for files whose length changes."
                },
                {
                    "num": 9,
                    "question": "What is a polymorphic virus?",
                    "options": {
                        "A": "A virus that only infects one type of file",
                        "B": "A virus with encrypted body and decryptor that changes across infections using a mutation engine",
                        "C": "A virus that spreads through multiple networks",
                        "D": "A virus that targets multiple operating systems"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A polymorphic virus has a fixed encrypted body with per-instance keys, but changes its decryptor portion across infections using a mutation engine. Strong forms use a 'mini-compiler' that creates new decryptor instances by combining functionally equivalent machine instructions."
                },
                {
                    "num": 10,
                    "question": "How does a metamorphic virus differ from a polymorphic virus?",
                    "options": {
                        "A": "Metamorphic viruses use stronger encryption",
                        "B": "Metamorphic viruses use no encryption and rewrite their entire code per-infection",
                        "C": "Metamorphic viruses only target Linux systems",
                        "D": "Metamorphic viruses spread faster than polymorphic viruses"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Metamorphic viruses use no encryption and no decryptor portion. On a per-infection basis, they rewrite their own code, mutating both their body (infection and payload functionality) and the mutation engine itself."
                },
                {
                    "num": 11,
                    "question": "What is a Trojan horse in the context of malware?",
                    "options": {
                        "A": "A virus that spreads through email",
                        "B": "Software that delivers malicious functionality instead of, or in addition to, intended functionality",
                        "C": "A worm that attacks network infrastructure",
                        "D": "Malware that encrypts user files"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A Trojan horse is software that delivers malicious functionality instead of, or in addition to, intended functionality. The term specifically refers to when the installation of software with extra functionality is 'voluntarily' accepted by the user."
                },
                {
                    "num": 12,
                    "question": "Which statement about Trojan horses is CORRECT?",
                    "options": {
                        "A": "A Trojan horse is a type of virus",
                        "B": "A Trojan horse is a destructive program, not a virus",
                        "C": "A Trojan horse spreads automatically over networks",
                        "D": "A Trojan horse always requires administrator privileges"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A Trojan horse is a destructive program, not a virus. If malware is silently installed without end-user knowledge or actions, it is not called a Trojan. The term specifically refers to voluntary acceptance of software with hidden malicious functionality."
                },
                {
                    "num": 13,
                    "question": "In asymmetric file-locking ransomware, what happens to the symmetric key (k) after encrypting the victim's files?",
                    "options": {
                        "A": "It is stored on the victim's computer in plain text",
                        "B": "It is encrypted with a public key, then the plaintext k is deleted",
                        "C": "It is sent directly to the attacker unencrypted",
                        "D": "It is embedded in each encrypted file"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "In asymmetric file-locking ransomware, the attacker creates a per-victim symmetric key k to encrypt files, then encrypts k with the public key, and deletes the plaintext k and original files. Only the attacker's private key can recover k."
                },
                {
                    "num": 14,
                    "question": "What is a zero-day exploit?",
                    "options": {
                        "A": "An attack that takes zero days to execute",
                        "B": "An attack taking advantage of a vulnerability unknown to developers, users, and the public",
                        "C": "An attack that only works on the first day of the month",
                        "D": "An attack that requires no user interaction"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A zero-day exploit (0-day) is an attack taking advantage of a software vulnerability unknown to developers of the target software, users, and the informed public. The day a vulnerability becomes known is the first day (the attack precedes it)."
                },
                {
                    "num": 15,
                    "question": "What is the primary reason zero-day attacks are particularly dangerous?",
                    "options": {
                        "A": "They spread faster than other attacks",
                        "B": "They always cause hardware damage",
                        "C": "The element of surprise and extra time this buys attackers before fixes are available",
                        "D": "They only target critical infrastructure"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The big deal about zero-days is the element of surprise and extra time this buys attackers. Unlike non-zero-day attacks where fixes may be available, with zero-days, fixes are still steps away from even being available."
                },
                {
                    "num": 16,
                    "question": "What is a botnet?",
                    "options": {
                        "A": "A collection of antivirus programs",
                        "B": "A collection of compromised devices that attackers communicate with",
                        "C": "A network of security researchers",
                        "D": "A type of firewall protection"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A botnet is a collection of compromised devices that attackers often communicate with. Ransomware attackers frequently communicate with large numbers of compromised devices forming a botnet."
                },
                {
                    "num": 17,
                    "question": "Which detection method identifies malware by detecting sequences of actions pre-identified as suspicious?",
                    "options": {
                        "A": "Signature-based detection",
                        "B": "Behavioral signatures",
                        "C": "Hash-based allowlisting",
                        "D": "Code signing verification"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Behavioral signatures identify malware by detecting sequences of actions pre-identified as suspicious, such as system calls, attempts to disable certain programs, or massive file deletions. This may require pre-running in an emulated environment."
                },
                {
                    "num": 18,
                    "question": "What is the 'append to host file' virus insertion technique?",
                    "options": {
                        "A": "The virus overwrites the entire host file",
                        "B": "The virus adds itself to the end and changes the jump target to execute virus code first",
                        "C": "The virus adds itself to the beginning of the file",
                        "D": "The virus inserts itself into unused bytes within the file"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "In the append method, the virus adds itself to the end of the host file. The original jump target is changed to be the first line of the appended virus code, and the virus code ends by jumping to the original start point."
                },
                {
                    "num": 19,
                    "question": "Why do worms tend to spread faster than viruses?",
                    "options": {
                        "A": "Worms use stronger encryption",
                        "B": "Worms have no dormant stage and propagate automatically without user interaction",
                        "C": "Worms are smaller in file size",
                        "D": "Worms only target server computers"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Having no dormant stage, worms tend to spread faster than viruses. They propagate automatically and continuously without user interaction, leveraging network protocols and daemons."
                },
                {
                    "num": 20,
                    "question": "What is the best practice defense against ransomware?",
                    "options": {
                        "A": "Using strong passwords",
                        "B": "Installing antivirus software",
                        "C": "Regular backups",
                        "D": "Disabling email attachments"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The best practice defense against ransomware is regular backups. Even if malware is removed, encrypted files remain unavailable without the decryption key, making backups essential for recovery."
                },
                {
                    "num": 21,
                    "question": "What is significant about the Brain virus of 1986?",
                    "options": {
                        "A": "It was the first virus to spread through email",
                        "B": "It is commonly cited as the first PC virus and was a boot sector virus",
                        "C": "It was the first virus to use encryption",
                        "D": "It was the first virus to cause hardware damage"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The Brain virus is commonly cited as the first PC virus. It was a boot sector virus that spread via floppy disks. Interestingly, its binary contained contact information for the Pakistani brothers who wrote it."
                },
                {
                    "num": 22,
                    "question": "In an encrypted virus, which part remains unmodified and can be targeted for detection?",
                    "options": {
                        "A": "The payload",
                        "B": "The encryption key",
                        "C": "The decryptor portion",
                        "D": "The virus body"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "In an encrypted virus, execution requires first decrypting the virus body by a small decryptor portion that remains unmodified. Detection can be done using string-matching against this decryptor part."
                },
                {
                    "num": 23,
                    "question": "What type of vulnerabilities do worms typically exploit compared to viruses?",
                    "options": {
                        "A": "Worms exploit software vulnerabilities like buffer overflows; viruses tend to abuse software features or use social engineering",
                        "B": "Worms only use social engineering; viruses exploit technical vulnerabilities",
                        "C": "Both exploit the same types of vulnerabilities",
                        "D": "Worms exploit hardware vulnerabilities; viruses exploit software vulnerabilities"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "Worms exploit software vulnerabilities (e.g., buffer overflows) while viruses tend to abuse software features or use social engineering. This is why worms are also called network worms or network viruses."
                },
                {
                    "num": 24,
                    "question": "What is a mass-mailing worm-virus?",
                    "options": {
                        "A": "A virus that only infects mail servers",
                        "B": "Email-based malware that combines virus and worm properties",
                        "C": "A worm that deletes all emails",
                        "D": "Spam email without malicious content"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Email-based malware that combines virus and worm properties is called an email virus, email worm, or mass-mailing worm-virus. It spreads through email-related file infection, attachments, and features of clients and infrastructure."
                },
                {
                    "num": 25,
                    "question": "Why does overwriting a host file with virus code complicate virus removal?",
                    "options": {
                        "A": "The virus becomes encrypted",
                        "B": "A removal tool will not have the original program file content available to restore",
                        "C": "The virus spreads to backup files",
                        "D": "The operating system prevents file deletion"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "When a virus overwrites the host file starting from the top, it destroys the host program. This complicates virus removal because a removal tool will not have the original program file content available to restore."
                }
            ]
        },

        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 26,
                    "question": "Harmful software caused by design or implementation errors is considered malware.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Harmful software is the bigger class, encompassing software causing unintentional damage due to design or implementation errors, but this is NOT within the scope of malware. Malware is INTENTIONALLY designed to have harmful effects."
                },
                {
                    "num": 27,
                    "question": "Malware runs without the explicit approval of the user.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - By definition, malware runs without the explicit approval of the user. This is a key characteristic that distinguishes malware from legitimate software."
                },
                {
                    "num": 28,
                    "question": "Computer firmware and hardware cannot be malicious.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Computer firmware and hardware may be malicious, depending on how firmware is provided and updated, and controls within the hardware supply chain."
                },
                {
                    "num": 29,
                    "question": "Viruses typically check if a file is already infected because infecting only new files is more effective.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Viruses typically check if a file is already infected. Infecting only new files is more effective for spreading and avoiding detection."
                },
                {
                    "num": 30,
                    "question": "Worms can cause denial of service (DoS) even when that is not their end-goal.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Because worms spread automatically and continuously, they are more likely to overload network communications channel capacity, causing DoS even when that is not their end-goal."
                },
                {
                    "num": 31,
                    "question": "Email-based malware always requires opening an attachment to spread.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Email-based malware typically requires a user action such as opening an email client or reading a message (not necessarily opening an attachment), and may involve social engineering."
                },
                {
                    "num": 32,
                    "question": "The shift-and-prepend virus technique increases file length.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - In the shift-and-prepend technique, the virus is inserted at the front after shifting the original file, which increases file length."
                },
                {
                    "num": 33,
                    "question": "Overwriting virus code at the interior of a file evades virus-scanning tools that only check the start of files.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Overwriting at interior evades virus-scanning tools that only check the start of files, though it still damages the original program."
                },
                {
                    "num": 34,
                    "question": "Placing virus code in the boot sector executes it before the operating system.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Placing virus code in the boot sector executes it before the OS, which is why code written into the Master Boot Record (MBR) is an attractive target for viruses."
                },
                {
                    "num": 35,
                    "question": "Denylist-type malware detection can protect against new, unknown malware.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The denylist-type mechanism (signature-based detection) protects against known malware, but NOT new malware. It requires signatures to be created from known malware first."
                },
                {
                    "num": 36,
                    "question": "A strong polymorphic virus uses a 'mini-compiler' to create new decryptor instances.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - A strong form of polymorphic virus uses a 'mini-compiler' that creates new decryptor instances by combining functionally equivalent sets of machine instructions."
                },
                {
                    "num": 37,
                    "question": "Virus detection tools may pre-run executables in emulators to detect polymorphic viruses.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Virus detection tools pre-run executables in emulators to detect polymorphic viruses. Once the static body is revealed after decryption, it is detectable by string-matching."
                },
                {
                    "num": 38,
                    "question": "If malware is silently installed without end-user knowledge or actions, it is called a Trojan horse.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - If malware is silently installed without end-user knowledge or actions, we do NOT call it a Trojan. The term Trojan specifically refers to when software installation is 'voluntarily' accepted."
                },
                {
                    "num": 39,
                    "question": "Removing ransomware from an infected system restores access to encrypted files.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Removing ransomware does NOT solve the problem. Encrypted files remain unavailable without the decryption key."
                },
                {
                    "num": 40,
                    "question": "Ransomware payment is typically demanded in hard-to-trace forms like Bitcoin or pre-paid cash vouchers.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Payment is demanded in hard-to-trace, non-reversible forms such as pre-paid cash vouchers or digital currencies. There has been a dramatic increase in ransomware in parallel with Bitcoin."
                },
                {
                    "num": 41,
                    "question": "Non-encrypting ransomware may disable OS debug modes like safe mode or safe boot.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Other non-encrypting ransomware may deny user access to OS functionality until ransom is paid, or disable OS debug modes (e.g., safe mode or safe boot)."
                },
                {
                    "num": 42,
                    "question": "In non-zero-day attacks, software fixes are typically available but remain undeployed.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - In non-zero-day attacks, vulnerabilities are known, exploits have been seen 'in the wild', software fixes and updates are available, and yet for various reasons the fixes remain undeployed."
                },
                {
                    "num": 43,
                    "question": "Better user education is sufficient to prevent all malware infections.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Better user education helps but is difficult, costly, never-ending, and insufficient against many malware tactics including persuasive social engineering."
                },
                {
                    "num": 44,
                    "question": "Code signing architectures can help verify that executable content is from known sources before installation.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Code signing architectures that test, before installing or running, that executable content (and updates) is from known sources can help prevent malware installation."
                },
                {
                    "num": 45,
                    "question": "A virus with an external decryption key may retrieve the key from a networked device using DNS lookup.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The key could be retrieved from a networked device whose address is obtained through a level of indirection, such as a search engine query or a DNS look-up with frequently-changed name-address mapping."
                }
            ]
        },

        "section3": {
            "title": "Section 3: Scenario-Based Questions (3 points each)",
            "questions": [
                {
                    "num": 46,
                    "question": "A security analyst notices that an SSH server has been installed on a company workstation that normally doesn't require remote access. The server was not authorized by IT. What does this scenario best illustrate about malware detection?",
                    "options": {
                        "A": "SSH servers are always malware",
                        "B": "What constitutes malware depends on context, not functionality alone",
                        "C": "All network services should be blocked",
                        "D": "Workstations cannot be infected with malware"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This illustrates that malware identification depends on context, not functionality alone. SSH server software is not generally viewed as malware, but this changes if it is installed by an attacker for covert access to a system."
                },
                {
                    "num": 47,
                    "question": "An organization's computers are infected with malware that encrypted all files and demands payment in cryptocurrency. After removing the malware, users still cannot access their files. What should the organization have done to prepare for this scenario?",
                    "options": {
                        "A": "Installed stronger firewalls",
                        "B": "Used longer passwords",
                        "C": "Maintained regular backups",
                        "D": "Trained users to recognize phishing emails"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "Regular backups are the best practice defense against ransomware. Even after removing the malware, encrypted files remain unavailable without the decryption key, making backups essential for data recovery."
                },
                {
                    "num": 48,
                    "question": "A user downloads what appears to be a free screen saver. The screen saver works as expected, but unknown to the user, it is also recording keystrokes and sending them to an external server. What type of malware is this?",
                    "options": {
                        "A": "Computer worm",
                        "B": "Boot sector virus",
                        "C": "Trojan horse",
                        "D": "Polymorphic virus"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "This is a Trojan horse - software that delivers malicious functionality (keylogging) in addition to intended functionality (screen saver). The user 'voluntarily' installed the software, which had hidden malicious capabilities."
                },
                {
                    "num": 49,
                    "question": "An antivirus program fails to detect a virus even though the virus body contains known malicious code. Analysis shows the virus uses different decryption routines on each infected file. What type of virus is this?",
                    "options": {
                        "A": "Simple encrypted virus",
                        "B": "Polymorphic virus",
                        "C": "Boot sector virus",
                        "D": "Macro virus"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This is a polymorphic virus, which has fixed encrypted bodies with per-instance keys but changes its decryptor portions across infections using a mutation engine. This defeats simple string-matching detection."
                },
                {
                    "num": 50,
                    "question": "A new vulnerability is discovered in a popular web browser. Attackers are already exploiting it, but no patch exists yet. Security teams are scrambling to develop countermeasures. What type of attack is this?",
                    "options": {
                        "A": "Social engineering attack",
                        "B": "Denial of service attack",
                        "C": "Zero-day exploit",
                        "D": "Man-in-the-middle attack"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "This is a zero-day exploit - an attack taking advantage of a vulnerability unknown to developers and users before being exploited. The day a vulnerability becomes known is the first day (the attack precedes it), and fixes are still steps away from being available."
                }
            ]
        },

        "section4": {
            "title": "Section 4: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 51,
                    "question": "What are the four stages in the lifecycle of a virus?",
                    "answer": ["dormancy", "propagation", "trigger", "payload"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "The four stages of a virus are: (1) Dormancy - until the host program runs, (2) Propagation - when and how it spreads, (3) Trigger condition - controls when the payload is executed, (4) Payload - defines the functionality delivered by the malware."
                },
                {
                    "num": 52,
                    "question": "What term describes software that delivers malicious functionality instead of, or in addition to, its intended functionality?",
                    "answer": ["trojan horse", "trojan", "trojan horses"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A Trojan horse is software that delivers malicious functionality instead of, or in addition to, intended functionality. The term specifically refers to when software installation is 'voluntarily' accepted by the user."
                },
                {
                    "num": 53,
                    "question": "What is the term for a collection of compromised devices that attackers communicate with?",
                    "answer": ["botnet", "bot net", "botnets"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A botnet is a collection of compromised devices that attackers communicate with. Ransomware attackers often communicate with large numbers of compromised devices forming a botnet."
                },
                {
                    "num": 54,
                    "question": "Name TWO methods that viruses can use to insert themselves into program files (e.g., shift and prepend, append, overwrite from top, overwrite at interior).",
                    "answer": ["shift and prepend", "prepend", "append", "overwrite", "overwrite from top", "overwrite at interior", "interior"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Viruses can insert themselves into programs using: (1) Shift and prepend - insert at front after shifting original, (2) Append to host file - add to end and change jump target, (3) Overwrite from top - destroy host program, (4) Overwrite at interior - evade scanners that only check file start."
                },
                {
                    "num": 55,
                    "question": "What is the term for a virus that uses no encryption and rewrites its entire code on each infection?",
                    "answer": ["metamorphic", "metamorphic virus"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A metamorphic virus uses no encryption and no decryptor portion. On a per-infection basis, it rewrites its own code, mutating both its body (infection and payload functionality) and the mutation engine itself."
                },
                {
                    "num": 56,
                    "question": "Name TWO ways malware can be detected according to the lecture (e.g., signatures, behavioral, allowlist/hash).",
                    "answer": ["signature", "signatures", "behavioral", "behavior", "allowlist", "hash", "tripwire", "digital signature", "code signing"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Malware detection methods include: (1) Malware signatures from object code, (2) Behavioral signatures detecting suspicious action sequences, (3) Allowlist programs by checking hash (e.g., Tripwire) or valid digital signature of a trusted party."
                },
                {
                    "num": 57,
                    "question": "What type of attack exploits a vulnerability that is unknown to developers and users?",
                    "answer": ["zero-day", "zero day", "0-day", "0 day", "zeroday"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A zero-day exploit (0-day) is an attack taking advantage of a software vulnerability unknown to developers, users, and the informed public. The day a vulnerability becomes known is the first day."
                },
                {
                    "num": 58,
                    "question": "What is the name of the 1986 boot sector virus commonly cited as the first PC virus?",
                    "answer": ["brain", "brain virus"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The Brain virus of 1986 is commonly cited as the first PC virus. It was a boot sector virus that spread via floppy disks and occasionally destroyed the floppy's FAT."
                },
                {
                    "num": 59,
                    "question": "What type of malware extorts users by preventing access to their files through encryption?",
                    "answer": ["ransomware", "file locker", "crypto ransomware", "cryptolocker"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Ransomware (specifically file lockers) prevents access to files by encryption and asks users to pay money for a decryption key that allows file recovery."
                },
                {
                    "num": 60,
                    "question": "Name TWO characteristics that distinguish worms from viruses.",
                    "answer": ["automatic", "automatically", "network", "no dormant", "no user", "without user", "vulnerability", "buffer overflow"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Worms differ from viruses in that: (1) They propagate automatically without user interaction, (2) They spread over networks rather than infecting host programs, (3) They exploit software vulnerabilities rather than abusing features or social engineering, (4) They have no dormant stage."
                }
            ]
        }
    }