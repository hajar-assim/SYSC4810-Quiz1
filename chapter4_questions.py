  
def get_chapter_4_questions():
    """Returns Chapter 4 questions (Authentication Protocols and Key Establishment)"""
    return {
        # SECTION 1: MULTIPLE CHOICE (2 points each)
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "Why should we not simply submit a password for authentication?",
                    "options": {
                        "A": "Because passwords are too long",
                        "B": "Because it is not fresh, you don't know who you're submitting it to, and eavesdroppers could learn it",
                        "C": "Because hashing is required first",
                        "D": "Because two-factor authentication is always needed"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Simply submitting a password fails because: it's not fresh, you don't know who you're submitting it to (mutual authentication issue), and eavesdroppers could learn it. The goal is to prove knowledge without revealing the secret."
                },
                {
                    "num": 2,
                    "question": "What is the main purpose of authentication-only protocols?",
                    "options": {
                        "A": "To establish session keys for ongoing communication",
                        "B": "To authenticate identities without establishing session keys",
                        "C": "To encrypt all network traffic",
                        "D": "To prevent all types of attacks"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Authentication-only protocols authenticate but do not establish session keys. However, this is insufficient because an adversary could wait until authentication occurs then hijack the session."
                },
                {
                    "num": 3,
                    "question": "What is the main limitation of key transport when using public keys?",
                    "options": {
                        "A": "It's too slow",
                        "B": "It fails to achieve forward secrecy",
                        "C": "It requires symmetric encryption",
                        "D": "It cannot work over networks"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Key transport by encrypting a key with the other party's public key fails to achieve forward secrecy. If the encryption key is later revealed, tapped exchanges can be decrypted."
                },
                {
                    "num": 4,
                    "question": "What does 'ephemeral' mean in the context of session keys?",
                    "options": {
                        "A": "Permanent and reusable",
                        "B": "Temporary and short-lived for a single session",
                        "C": "Encrypted with public keys",
                        "D": "Stored for backup purposes"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Ephemeral keys are temporary and short-lived, used for a single session. This keeps their value low from an attacker's resource allocation perspective, unlike long-term keys which hold higher value."
                },
                {
                    "num": 5,
                    "question": "What is the main vulnerability of unauthenticated key establishment (like basic Diffie-Hellman)?",
                    "options": {
                        "A": "It's too computationally expensive",
                        "B": "It's vulnerable to active attackers like man-in-the-middle",
                        "C": "It doesn't work with prime numbers",
                        "D": "It requires pre-shared secrets"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Unauthenticated key establishment is fine with passive adversaries but vulnerable to active ones (e.g., middle-person/MitM attacks). You could be establishing a key with a different entity than intended."
                },
                {
                    "num": 6,
                    "question": "What does authenticated key establishment ensure?",
                    "options": {
                        "A": "Only that a key is established",
                        "B": "That the party authenticated is the same party the key is shared with",
                        "C": "That passwords are never used",
                        "D": "That encryption is not needed"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Authenticated key establishment pursues both key establishment and entity authentication within one integrated protocol to ensure that the party authenticated is the same party that the key is shared with."
                },
                {
                    "num": 7,
                    "question": "Why should keys not be reused across different parties and devices?",
                    "options": {
                        "A": "It makes encryption slower",
                        "B": "The more you use keys, the more prone to exposure they become and their value increases",
                        "C": "It violates password policies",
                        "D": "It requires more memory"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The more keys are used, the more prone to exposure they become, and their value increases (attackers willing to pour more resources). Secrets tend to 'leak' through various means like memory dumps, backups, etc."
                },
                {
                    "num": 8,
                    "question": "What is initial keying material?",
                    "options": {
                        "A": "The final session key",
                        "B": "Public or secret keys distributed during a registration phase, often out-of-band",
                        "C": "Temporary passwords",
                        "D": "Encrypted hash values"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Initial keying material (public or secret) is associated or distributed with identified parties during a registration phase, usually involving out-of-band means to establish shared secrets."
                },
                {
                    "num": 9,
                    "question": "What characterizes a strong secret versus a weak secret?",
                    "options": {
                        "A": "Strong secrets are longer than weak secrets",
                        "B": "Strong secrets are drawn from perfectly uniform random generation; weak secrets have skewed distributions",
                        "C": "Strong secrets use more encryption",
                        "D": "Weak secrets are always user-chosen"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Strong secrets are drawn from perfectly uniform randomness (probability 2^-t for t-bit key). Weak secrets have non-uniform distributions where some keys are more likely than others (e.g., user-chosen passwords)."
                },
                {
                    "num": 10,
                    "question": "In Trial 1 of authentication protocols (hashing a weak secret W), what is the main vulnerability?",
                    "options": {
                        "A": "Replay attack",
                        "B": "Offline guessing attack using H(W) as verifiable text",
                        "C": "Man-in-the-middle attack",
                        "D": "Brute force on the hash function"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Sending H(W) allows offline guessing attacks because the transmitted hash serves to identify if the guessed secret is correct by comparing hashes."
                },
                {
                    "num": 11,
                    "question": "In Trial 2 (hashing a strong secret S), what is the main attack?",
                    "options": {
                        "A": "Offline dictionary attack",
                        "B": "Replay attack - capturing and retransmitting H(S)",
                        "C": "Password cracking",
                        "D": "Session hijacking"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A replay attack works because capturing and transmitting H(S) later suffices - the attacker never needs to learn S. This also works with weak secret W from Trial 1."
                },
                {
                    "num": 12,
                    "question": "What is a nonce?",
                    "options": {
                        "A": "A permanent identifier",
                        "B": "A random number used once",
                        "C": "A type of encryption key",
                        "D": "A hash function"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A nonce means a random number used once. Types include: random numbers, sequence numbers, and timestamps."
                },
                {
                    "num": 13,
                    "question": "What property do timestamps provide that challenge-response does not?",
                    "options": {
                        "A": "Better security",
                        "B": "Timeliness assurance without requiring a challenge",
                        "C": "Stronger encryption",
                        "D": "Mutual authentication"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Timestamps give timeliness assurances without the challenge part of challenge-response and help enforce constraints in time-bounded protocols. However, they require time synchronization."
                },
                {
                    "num": 14,
                    "question": "What does a replay attack involve?",
                    "options": {
                        "A": "Breaking encryption",
                        "B": "Reusing a previously captured message in a later protocol run",
                        "C": "Guessing passwords",
                        "D": "Stealing private keys"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A replay attack involves reusing a previously captured message in a later protocol run. This is why freshness and nonces are important."
                },
                {
                    "num": 15,
                    "question": "What is a reflection attack?",
                    "options": {
                        "A": "Using mirrors to intercept signals",
                        "B": "Replaying a captured message back to the originating party",
                        "C": "Encrypting data twice",
                        "D": "Reversing hash functions"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A reflection attack involves replaying a captured message on the originating party, potentially causing them to authenticate themselves incorrectly."
                },
                {
                    "num": 16,
                    "question": "What is a relay attack?",
                    "options": {
                        "A": "Using multiple servers",
                        "B": "Forwarding a message in real time from a distinct protocol run",
                        "C": "Breaking encryption in stages",
                        "D": "Distributing keys"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A relay attack involves forwarding a message in real time from a distinct protocol run. Example: enemy aircraft impersonating friendly one by relaying responses."
                },
                {
                    "num": 17,
                    "question": "What does the Diffie-Hellman protocol accomplish?",
                    "options": {
                        "A": "Password encryption",
                        "B": "Establishing a shared secret over a public channel with no prior contact",
                        "C": "User authentication",
                        "D": "Certificate generation"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Diffie-Hellman (1976) allows two parties to establish a shared secret with no prior contact, no pre-shared keying material, over a channel readable by everyone. It relies on the difficulty of discrete logarithms."
                },
                {
                    "num": 18,
                    "question": "What is a generator g in the context of finite fields?",
                    "options": {
                        "A": "A random number",
                        "B": "An element where g^i (mod p) for all i generates all group elements",
                        "C": "A prime number",
                        "D": "An encryption key"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "If p is prime, a generator g exists such that g^i (mod p) for all i = [1,p-1] generates all group elements of the multiplicative group."
                },
                {
                    "num": 19,
                    "question": "What is a small subgroup attack in Diffie-Hellman?",
                    "options": {
                        "A": "Using small prime numbers",
                        "B": "Replacing exponentials with values that generate small subgroups, forcing K into a small searchable set",
                        "C": "Shortening the key length",
                        "D": "Using weak passwords"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "An attacker may replace exponentials (like g^a, g^b) with others that generate small subgroups, forcing the resulting key K into a small set that can be easily searched. Values like 0, 1, or p-1 should be ruled out."
                },
                {
                    "num": 20,
                    "question": "What is the main goal of PAKE (Password-Authenticated Key Exchange)?",
                    "options": {
                        "A": "To make passwords longer",
                        "B": "To provide authenticated key exchange using weak secrets (passwords) without providing verifiable text",
                        "C": "To eliminate the need for encryption",
                        "D": "To store passwords securely"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "PAKE aims to provide strong authenticated key exchange using weak secrets (passwords) while ensuring the exchange provides no verifiable text that would allow offline password guessing attacks."
                }
            ]
        },
        
        # SECTION 2: TRUE/FALSE (1 point each)
        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 21,
                    "question": "Authentication protocols differ from user authentication because they are machine-to-machine.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Authentication protocols are machine-to-machine, whereas user authentication involves human users."
                },
                {
                    "num": 22,
                    "question": "Having a common secret is sufficient for authentication without needing a protocol.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Having a common secret is one thing, but knowing how to use it to authenticate turns out to be a different story requiring proper protocols."
                },
                {
                    "num": 23,
                    "question": "Mutual authentication is commonly used in TLS web connections where browsers authenticate to servers.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Mutual authentication is not quite used in the web (TLS). If the browser needs to be authenticated, the user gets authenticated instead."
                },
                {
                    "num": 24,
                    "question": "Authentication by itself is sufficient for securing sessions.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Authentication by itself is not enough. An adversary could wait until authentication occurs then hijack the session. After authentication, we need to agree on shared keys for the session."
                },
                {
                    "num": 25,
                    "question": "Key transport via public key encryption achieves forward secrecy.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Key transport by encrypting with the other party's public key fails to achieve forward secrecy because tapped exchanges and a later revealed encryption key compromise past sessions."
                },
                {
                    "num": 26,
                    "question": "Ephemeral keys help maintain forward secrecy if they are properly deleted after use.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Ephemeral keys provide forward secrecy if the session secrets are fresh and securely deleted (unrecoverably removed from memory) after the session."
                },
                {
                    "num": 27,
                    "question": "Unauthenticated key establishment protocols are fine with passive adversaries but vulnerable to active ones.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Unauthenticated key establishment (like basic DH) works against passive adversaries but is vulnerable to active adversaries like man-in-the-middle attackers."
                },
                {
                    "num": 28,
                    "question": "Gluing together separate key establishment and entity authentication protocols works well.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Using separate key establishment and entity authentication protocols and gluing them together ends badly. Both functions should be pursued within one integrated protocol."
                },
                {
                    "num": 29,
                    "question": "Keys used for data at rest (storage) should be backed up despite potential risks.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Keys for securing data at rest should be backed up because hardware failure could cause permanent data loss, unlike communication keys where you can just establish a new key and retransmit."
                },
                {
                    "num": 30,
                    "question": "The more a key is used, the less valuable it becomes to attackers.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The more you use keys, the more prone to exposure they become AND the more their value increases (attackers are willing to pour more financial resources into breaking them)."
                },
                {
                    "num": 31,
                    "question": "Initial keying material is typically established through out-of-band means.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - A registration phase using out-of-band means is needed to associate or distribute initial keying material with identified parties."
                },
                {
                    "num": 32,
                    "question": "For a key of length t bits drawn from uniform randomness, the guessing probability is 2^-t.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - For a key of length t bits from perfectly uniform randomness, the probability of guessing is 2^-t and the space is 2^t."
                },
                {
                    "num": 33,
                    "question": "User-chosen passwords typically have uniform distribution across the password space.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - User-chosen passwords are weak secrets with non-uniform, highly skewed distributions. Some passwords are more likely than others."
                },
                {
                    "num": 34,
                    "question": "Sending H(W) for a weak password W is vulnerable to offline guessing attacks.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The hash H(W) serves as verifiable text, allowing attackers to guess W offline and verify by comparing hashes."
                },
                {
                    "num": 35,
                    "question": "A replay attack can work even with strong secrets.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Replay attacks work by capturing and retransmitting authentication messages (like H(S)) without needing to learn the secret S itself."
                },
                {
                    "num": 36,
                    "question": "Sequence numbers require unpredictability like random numbers.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - In some cases uniqueness is required, not unpredictability. Sequence numbers provide uniqueness but must be monitored for overflows."
                },
                {
                    "num": 37,
                    "question": "Timestamps require time synchronization between communicating parties.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Timestamps require time synchronization, raising questions about precision requirements, trusted time sources, and secure synchronization methods."
                },
                {
                    "num": 38,
                    "question": "A reflection attack involves replaying a message to the originating party.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - A reflection attack involves replaying a captured message on the originating party who sent it."
                },
                {
                    "num": 39,
                    "question": "Diffie-Hellman requires pre-shared keying material between parties.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Diffie-Hellman allows establishing a shared secret with no prior contact and no pre-shared keying material."
                },
                {
                    "num": 40,
                    "question": "Basic Diffie-Hellman provides authentication by default.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - DH is unauthenticated by default. It works against passive attackers but not active ones. You could be establishing keys with a different entity."
                }
            ]
        },
        
        # SECTION 3: SHORT ANSWER (2 points each)
        "section3": {
            "title": "Section 3: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 41,
                    "question": "What does it mean to 'prove knowledge of a secret without revealing it'?",
                    "answer": ["proof of knowledge", "challenge response", "zero knowledge", "cryptographic proof", "authentication without disclosure"],
                    "points": 2,
                    "type": "text",
                    "explanation": "This means demonstrating possession of a secret through cryptographic means (like challenge-response) without actually transmitting the secret itself, keeping the element of secrecy local."
                },
                {
                    "num": 42,
                    "question": "What property is lost when using key transport with public keys, where tapped exchanges and later revealed keys compromise past sessions?",
                    "answer": ["forward secrecy", "perfect forward secrecy", "pfs", "forward security"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Forward secrecy - the property that disclosure of long-term secret keys does not compromise the secrecy of earlier session keys."
                },
                {
                    "num": 43,
                    "question": "What term describes keys that are temporary and used only for a single session?",
                    "answer": ["ephemeral", "ephemeral keys", "session keys", "temporary keys", "short-lived"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Ephemeral keys are temporary/short-lived and used for single sessions, helping maintain low value and supporting forward secrecy when properly deleted."
                },
                {
                    "num": 44,
                    "question": "What does PAKE stand for?",
                    "answer": ["password-authenticated key exchange", "password authenticated key exchange", "pake"],
                    "points": 2,
                    "type": "text",
                    "explanation": "PAKE = Password-Authenticated Key Exchange, protocols designed to provide authenticated key exchange using weak secrets (passwords)."
                },
                {
                    "num": 45,
                    "question": "What term describes a random number used once in authentication protocols?",
                    "answer": ["nonce", "number used once"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A nonce is a number used once. Types include random numbers, sequence numbers, and timestamps."
                },
                {
                    "num": 46,
                    "question": "What attack involves reusing a previously captured message in a later protocol run?",
                    "answer": ["replay", "replay attack", "replaying"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A replay attack involves capturing and reusing a previously transmitted message, which is why freshness mechanisms like nonces are essential."
                },
                {
                    "num": 47,
                    "question": "What type of attack involves forwarding a message in real time from a distinct protocol run?",
                    "answer": ["relay", "relay attack", "relaying"],
                    "points": 2,
                    "type": "text",
                    "explanation": "A relay attack forwards messages in real time from distinct protocol runs. Example: enemy aircraft relaying friendly responses."
                },
                {
                    "num": 48,
                    "question": "In Diffie-Hellman, what mathematical problem makes it hard for attackers to compute the shared secret from g^a and g^b?",
                    "answer": ["discrete logarithm", "discrete log", "discrete logarithm problem", "dlog"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The discrete logarithm problem - given g^a and g^b, an attacker cannot efficiently compute a or b, and thus cannot compute g^(ab)."
                },
                {
                    "num": 49,
                    "question": "For a prime p, what term describes the set of non-zero elements [1, p-1]? (Mathematical notation acceptable)",
                    "answer": ["multiplicative group", "z*p", "z star p", "z* sub p", "multiplicative group mod p"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The multiplicative group Z*_p consists of non-zero elements [1,p-1] of the finite field modulo prime p."
                },
                {
                    "num": 50,
                    
                    "question": "What property must the exchange lack to prevent offline password guessing in PAKE protocols?",
                    "answer": ["verifiable text", "verifiable", "verification", "verifiability"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The exchange must provide no verifiable text - no data that allows an attacker to verify password guesses offline by checking if decryption/computation produces recognizable results."
                }
            ]
        }
    }