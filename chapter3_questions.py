def get_chapter_3_questions():
    """Returns Chapter 3 questions (User Authentication - up to slide 33)"""
    return {
        # SECTION 1: MULTIPLE CHOICE (2 points each)
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "Authentication is best described as:",
                    "options": {
                        "A": "The process of granting access rights to resources",
                        "B": "The process of using supporting evidence to corroborate an asserted identity",
                        "C": "The process of encrypting user credentials",
                        "D": "The process of establishing identity without an explicit assertion"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Authentication is the process of using supporting evidence (credentials) to corroborate an asserted identity. It's a single test to verify if provided credentials match the stored template."
                },
                {
                    "num": 2,
                    "question": "Identification (recognition) differs from authentication in that:",
                    "options": {
                        "A": "It requires a password",
                        "B": "It's a one-to-many process without an explicit identity assertion",
                        "C": "It's faster than authentication",
                        "D": "It only works with biometrics"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Identification is a one-to-many process (e.g., picking out a criminal in a crowd, matching a fingerprint to its owner) without an explicit identity having been asserted first."
                },
                {
                    "num": 3,
                    "question": "Which authentication category does a password belong to?",
                    "options": {
                        "A": "What you have",
                        "B": "What you know",
                        "C": "What you are/do",
                        "D": "Where you are"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Passwords fall under 'What you know' category of authentication, along with PINs and other memorized secrets."
                },
                {
                    "num": 4,
                    "question": "Two-factor authentication (2FA) typically requires:",
                    "options": {
                        "A": "Two passwords from the same category",
                        "B": "Methods from two different authentication categories",
                        "C": "Two biometric methods",
                        "D": "Two devices"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "2FA typically requires methods from two different categories to provide independent protection (e.g., password + hardware token)."
                },
                {
                    "num": 5,
                    "question": "When storing passwords, the system should store:",
                    "options": {
                        "A": "Cleartext passwords for quick verification",
                        "B": "Password hashes H(pi)",
                        "C": "Encrypted passwords using symmetric encryption",
                        "D": "Passwords in a secure database only"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Systems should store password hashes H(pi) using a publicly known one-way hash function, not cleartext passwords which expose all passwords if the file is stolen."
                },
                {
                    "num": 6,
                    "question": "A targeted attack is:",
                    "options": {
                        "A": "An attack aimed at breaking into any account",
                        "B": "An attack specifically aimed at pre-identified users",
                        "C": "Always an online attack",
                        "D": "Less dangerous than a trawling attack"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "A targeted attack is specifically aimed at pre-identified users (often one), while trawling attacks aim to break into any account by trying many accounts (breadth-first)."
                },
                {
                    "num": 7,
                    "question": "In a pre-computed dictionary attack, the attacker:",
                    "options": {
                        "A": "Tries passwords online against the server",
                        "B": "Creates a table of (hj, wj) pairs and compares with stolen password hashes",
                        "C": "Uses social engineering only",
                        "D": "Bypasses the authentication mechanism entirely"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Pre-computed dictionary attacks involve creating a table T of pairs (hj, wj) where hj = H(wj), then comparing with stolen password file hashes to find matches."
                },
                {
                    "num": 8,
                    "question": "Password capture attacks include all EXCEPT:",
                    "options": {
                        "A": "Shoulder-surfing",
                        "B": "Keyloggers",
                        "C": "Brute-force guessing",
                        "D": "Phishing"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Password capture attacks intercept or observe passwords (shoulder-surfing, keyloggers, phishing, pharming). Brute-force guessing is a password-guessing attack, not a capture attack."
                },
                {
                    "num": 9,
                    "question": "Password composition policies primarily aim to:",
                    "options": {
                        "A": "Prevent all types of attacks",
                        "B": "Provide higher resilience to simple password-guessing attacks",
                        "C": "Protect against capture attacks",
                        "D": "Make passwords easier to remember"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Password policies (complexity requirements) only provide higher resilience to simple password-guessing attacks. They don't protect against capture attacks and users often make predictable modifications."
                },
                {
                    "num": 10,
                    "question": "Online password-guessing attacks are primarily limited by:",
                    "options": {
                        "A": "CPU power of the attacker",
                        "B": "Network bandwidth and rate limiting",
                        "C": "Password hash strength",
                        "D": "Operating system security"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Online password-guessing attacks are limited by network bandwidth and can be defended against using rate limiting (throttling), though this can lock out legitimate users."
                },
                {
                    "num": 11,
                    "question": "The purpose of password salting is to:",
                    "options": {
                        "A": "Make passwords taste better",
                        "B": "Slow down all password attacks equally",
                        "C": "Make trawling dictionary attacks harder by requiring tables for each salt value",
                        "D": "Eliminate the need for strong passwords"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Password salting stores (ui, si, H(pi,si)) where si is a random salt. This makes trawling attacks harder by a factor of 2^t (requiring tables for each salt), though targeted attacks with known salt aren't slowed."
                },
                {
                    "num": 12,
                    "question": "Iterated hashing (password stretching) works by:",
                    "options": {
                        "A": "Hashing the password multiple times: H^d(pi)",
                        "B": "Using longer hash functions",
                        "C": "Adding more salt",
                        "D": "Storing multiple password hashes"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "Iterated hashing computes H(…H(H(pi))) = H^d(pi), hashing d times. This slows attacks by factor d (e.g., d=1000), and can be adjusted as computing power increases."
                },
                {
                    "num": 13,
                    "question": "A pepper (secret salt) differs from regular salt because:",
                    "options": {
                        "A": "It uses a different hash function",
                        "B": "It is not stored and must be guessed during verification",
                        "C": "It's only used for strong passwords",
                        "D": "It's stored encrypted"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Pepper is like salt but NOT stored. System stores H(pi,ri), erases ri, then must try all possible r* values during verification until finding a match, slowing down both legitimate verification and attacks."
                },
                {
                    "num": 14,
                    "question": "User-chosen passwords typically result in:",
                    "options": {
                        "A": "Uniform distribution across password space",
                        "B": "Predictable clustering and highly skewed distribution",
                        "C": "Maximum security",
                        "D": "Random distribution"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "User-chosen passwords exhibit predictable clustering and highly skewed distributions. Attackers exploit this by trying more popular (higher probability) passwords first."
                },
                {
                    "num": 15,
                    "question": "System-assigned random passwords provide:",
                    "options": {
                        "A": "Better usability than user-chosen passwords",
                        "B": "Protection against brute-force at cost of usability",
                        "C": "Guaranteed security against all attacks",
                        "D": "Easier memorization"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "System-assigned random passwords create uniform distribution (password space b^n), making brute-force the best attack strategy, but suffer from poor usability (violates P11: User-buy-in)."
                },
                {
                    "num": 16,
                    "question": "Password denylists are used to:",
                    "options": {
                        "A": "Block users from the system",
                        "B": "Prevent selection of most-popular weak passwords",
                        "C": "Store forbidden usernames",
                        "D": "Encrypt passwords"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Denylists contain most-popular passwords from known distributions. Proactive password checking disallows passwords on the denylist during password selection."
                },
                {
                    "num": 17,
                    "question": "Which defensive measure makes a stolen password hash file less useful for offline attacks?",
                    "options": {
                        "A": "Rate limiting",
                        "B": "MAC on password hashes",
                        "C": "Account lockout",
                        "D": "CAPTCHA"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Adding a MAC to password hashes means stolen hash files become useless since attackers can't verify guesses without the MAC key. Rate limiting and lockout defend against online attacks."
                },
                {
                    "num": 18,
                    "question": "Account recovery using secret questions typically fails because:",
                    "options": {
                        "A": "Questions are too complex",
                        "B": "Answers change over time, are socially discoverable, and recovery occurs long after answers were set",
                        "C": "They're more secure than passwords",
                        "D": "Users always remember correct answers"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Secret questions fail because: recovery occurs long after answers were set, answers change over time (favorite movie), answers are vulnerable to social engineering/guessing, and users sometimes intentionally give wrong answers."
                },
                {
                    "num": 19,
                    "question": "Which is an advantage of passwords over other authentication methods?",
                    "options": {
                        "A": "They cannot be shared",
                        "B": "They're free, simple, already understood, and easy to change",
                        "C": "They provide perfect security",
                        "D": "They never need to be reset"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Password advantages: simple/understood, 'free' (no extra hardware), no physical device to carry, quick login, easy to change/recover, well-understood failure modes, no new third party trust needed, easily delegated."
                },
                {
                    "num": 20,
                    "question": "Biometric authentication is NOT appropriate for:",
                    "options": {
                        "A": "Local device unlock",
                        "B": "Remote authentication over the Internet",
                        "C": "Physical access control",
                        "D": "Airport border control"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Biometrics are non-secret and rely on trusted input channels (fingerprint isn't from a glass!), making them unsuitable for remote Internet authentication where the input channel can't be trusted."
                }
            ]
        },
        
        # SECTION 2: TRUE/FALSE (1 point each)
        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 21,
                    "question": "Authentication and authorization are the same thing.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Authentication verifies identity ('who are you?'), while authorization determines access rights ('what can you access?'). Authentication can be a step toward authorization."
                },
                {
                    "num": 22,
                    "question": "Two-stage authentication means user-to-device authentication followed by device-to-web authentication.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Two-stage authentication refers to the process where a user first authenticates to their device, then the device authenticates to a web service."
                },
                {
                    "num": 23,
                    "question": "Storing passwords in cleartext is vulnerable to insider threats.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Cleartext passwords expose all passwords if the file is stolen and are especially vulnerable to insider threats who have system access."
                },
                {
                    "num": 24,
                    "question": "In a trawling attack, the attacker targets a specific pre-identified user.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Trawling (breadth-first) attacks aim to break into ANY account by trying many/all accounts. Targeted attacks aim at pre-identified users."
                },
                {
                    "num": 25,
                    "question": "If hi = hj in a dictionary attack, then wj is guaranteed to be the actual password pi.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Hash collisions mean wj might not be the actual password pi, but wj will WORK as the password for login since H(wj) = H(pi) = hi."
                },
                {
                    "num": 26,
                    "question": "Password composition policies provide protection against password capture attacks.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Password complexity policies do NOT protect against capture attacks (keyloggers, phishing, shoulder-surfing). They only help against simple guessing attacks."
                },
                {
                    "num": 27,
                    "question": "Rate limiting can lock out legitimate users as a side effect.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Rate limiting (throttling) can cause denial of service to legitimate users as an unintended consequence of defending against online password-guessing attacks."
                },
                {
                    "num": 28,
                    "question": "Offline password-guessing attacks are limited by network bandwidth.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Offline attacks (after stealing password file) are limited only by computational resources, not network bandwidth. Online attacks are limited by bandwidth."
                },
                {
                    "num": 29,
                    "question": "Password salting prevents targeted on-the-fly attacks when the salt is known.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Salt doesn't increase time-cost of on-the-fly targeted attacks when salt si is available (from insider or stolen file). Salt primarily defends against pre-computed trawling attacks."
                },
                {
                    "num": 30,
                    "question": "Iterated hashing should ideally be combined with salting.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Iterated hashing (password stretching) is ideally combined with salting for comprehensive defense against offline attacks."
                },
                {
                    "num": 31,
                    "question": "Password pepper (secret salt) slows down legitimate user verification.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Pepper requires the system to sequentially try all R possible values during verification, slowing both legitimate verification and attacks by factor R."
                },
                {
                    "num": 32,
                    "question": "Attackers using password distributions try more popular passwords first.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Attackers tailor guessing strategies by trying higher estimated probability (more popular) passwords first, exploiting the skewed distribution of user-chosen passwords."
                },
                {
                    "num": 33,
                    "question": "System-assigned random passwords are more usable than user-chosen passwords.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - System-assigned random passwords have poor usability (hard to remember), violating P11: User-buy-in, though they provide better security against guessing."
                },
                {
                    "num": 34,
                    "question": "Proactive password cracking involves the system trying to crack its own users' passwords.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Proactive password cracking means the system attempts to crack its own users' passwords using background computing; users with cracked passwords are notified to change them."
                },
                {
                    "num": 35,
                    "question": "Passwords are easily delegated, which is both a benefit and a security drawback.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Password delegation (to spouse/secretary) is an underrated benefit, but retraction of delegation is rarely done, creating a security drawback."
                },
                {
                    "num": 36,
                    "question": "Secret question answers should be treated as secrets like passwords.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Secret questions often fail because answers are treated casually, but they should be protected as secrets since they provide account access."
                },
                {
                    "num": 37,
                    "question": "Passwords require no trust in a new third party compared to some other authentication methods.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Passwords require no trust in third parties beyond client/server organizations. Public-key certificates, in contrast, require trusting external certificate authorities."
                },
                {
                    "num": 38,
                    "question": "Adding a MAC to password hashes makes stolen hash files useless for offline attacks.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - MAC on password hashes means attackers can't verify password guesses from a stolen hash file without the MAC secret key, rendering the file useless."
                },
                {
                    "num": 39,
                    "question": "Biometric authentication relies on characteristics being secret.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Biometrics are NON-secret. They rely on trusted input channels providing assurance the sample is 'tightly bound' to the user present (not from a glass of water!)."
                },
                {
                    "num": 40,
                    "question": "Biometric modalities include both physical and behavioral characteristics.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Biometric modalities include physical (fingerprints, facial recognition, iris, hand geometry, retinal scan) and behavioral (gait, typing rhythm, mouse patterns) characteristics."
                }
            ]
        },
        
        # SECTION 3: SHORT ANSWER (2 points each)
        "section3": {
            "title": "Section 3: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 41,
                    "question": "Name TWO of the four authentication categories (separate with comma):",
                    "answer": ["what you know", "what you have", "where you are", "what you are", "what you do", "know", "have", "are", "do"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "The four authentication categories are: What you know, What you have, Where you are, and What you are/do (biometrics - physical or behavioral)."
                },
                {
                    "num": 42,
                    "question": "What does 2FA stand for?",
                    "answer": ["two-factor authentication", "two factor authentication", "2fa", "two factor"],
                    "points": 2,
                    "type": "text",
                    "explanation": "2FA = Two-factor authentication, using two methods from different categories (both must succeed) to provide independent protection."
                },
                {
                    "num": 43,
                    "question": "When a system stores (username, H(password)), what must it do to verify a user-entered password p?",
                    "answer": ["hash", "compute hash", "h(p)", "hash the entered password", "compute h(p) and compare"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The system computes H(p) for the entered password and compares it with the stored hash value to verify if they match."
                },
                {
                    "num": 44,
                    "question": "Name ONE type of password capture attack:",
                    "answer": ["shoulder-surfing", "keylogger", "phishing", "pharming", "social engineering", "middle-person", "proxy attack", "malware", "sticky note"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Password capture attacks include: shoulder-surfing, hardware/software keyloggers, client malware, proxy/middle-person attacks, phishing, social engineering, pharming, observing written passwords."
                },
                {
                    "num": 45,
                    "question": "In password salting, is the salt value si stored in cleartext or encrypted?",
                    "answer": ["cleartext", "clear text", "clear", "plaintext", "plain text", "unencrypted"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Salt si is stored in cleartext to enable verification. The system stores (ui, si, H(pi,si)) with si readable to allow computing H(p,si) for verification."
                },
                {
                    "num": 46,
                    "question": "What is the main practical limitation of one-time pads that makes them similar to password management problems?",
                    "answer": ["key distribution", "key length", "distribution", "key management", "length", "key size"],
                    "points": 2,
                    "type": "text",
                    "explanation": "One-time pads require keys as long as the message and secure key distribution, creating management problems similar to passwords (need to securely share/store the long key)."
                },
                {
                    "num": 47,
                    "question": "For an n-character password from alphabet of size b, how many possible passwords exist (password space size)?",
                    "answer": ["b^n", "bn", "b**n", "b to the n", "b raised to n"],
                    "points": 2,
                    "type": "text",
                },{
                    "num": 48,
                    "question": "What does SSO stand for in authentication?",
                    "answer": ["single sign-on", "single sign on", "sso"],
                    "points": 2,
                    "type": "text",
                    "explanation": "SSO = Single sign-on, architecture allowing users to authenticate once and access multiple services without re-authenticating separately for each."
                },
                {
                    "num": 49,
                    "question": "In SSO systems, what are the third parties called that create authenticators from initial authentication? (Abbreviation acceptable)",
                    "answer": ["identity provider", "idp", "identity providers", "idps"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Identity Providers (IdPs) are the third parties that access credentials or create authenticators (data tokens) from initial authentication for later identity representations."
                },
                {
                    "num": 50,
                    "question": "Why are biometrics considered non-secret?",
                    "answer": ["publicly observable", "visible", "can be observed", "not secret", "non secret", "observable", "left behind"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Biometrics are non-secret because they can be publicly observed or obtained (fingerprints on glasses, face in photos). They rely on trusted input channels, not secrecy."
                }
            ]
        }
    }