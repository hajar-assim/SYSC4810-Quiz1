def get_chapter_2_questions():
    """Returns Chapter 2 questions"""
    return {
        # SECTION 1: MULTIPLE CHOICE (2 points each)
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "In symmetric encryption, the encryption key k and decryption key k' are:",
                    "options": {
                        "A": "Different keys generated independently",
                        "B": "The same key (k = k')",
                        "C": "Public and private key pairs",
                        "D": "One is derived from a hash of the other"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Symmetric encryption uses the same key for both encryption and decryption (k = k'), also called secret-key encryption."
                },
                {
                    "num": 2,
                    "question": "Which of the following is an example of a symmetric encryption algorithm?",
                    "options": {
                        "A": "RSA",
                        "B": "AES",
                        "C": "Diffie-Hellman",
                        "D": "Elliptic Curve Cryptography"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "AES (Advanced Encryption Standard) is a symmetric encryption algorithm. RSA and ECC are asymmetric, and Diffie-Hellman is for key exchange."
                },
                {
                    "num": 3,
                    "question": "For a key of size n bits, how many expected trials are needed for a brute-force attack?",
                    "options": {
                        "A": "n",
                        "B": "2^n",
                        "C": "2^(n-1)",
                        "D": "n^2"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "On average, you'd need to try half the key space, which is 2^(n-1) trials for an n-bit key."
                },
                {
                    "num": 4,
                    "question": "Which attack model involves the attacker having access to both plaintext and corresponding ciphertext?",
                    "options": {
                        "A": "Ciphertext-only attack",
                        "B": "Known-plaintext attack",
                        "C": "Chosen-plaintext attack",
                        "D": "Chosen-ciphertext attack"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Known-plaintext attack: attacker has CT-PT pairs and tries to recover unknown PT or key from another CT."
                },
                {
                    "num": 5,
                    "question": "The Vernam cipher (one-time pad) is:",
                    "options": {
                        "A": "Computationally secure",
                        "B": "Information-theoretically secure",
                        "C": "Vulnerable to known-plaintext attacks",
                        "D": "Based on RSA encryption"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "One-time pads are information-theoretically secure (unbreakable even with unlimited computing power) when used correctly."
                },
                {
                    "num": 6,
                    "question": "What is the main practical limitation of one-time pads?",
                    "options": {
                        "A": "They are too slow",
                        "B": "Key distribution and key length requirements",
                        "C": "They only work with small messages",
                        "D": "They are vulnerable to frequency analysis"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "One-time pads require keys as long as the message and secure key distribution, making them impractical for most uses."
                },
                {
                    "num": 7,
                    "question": "Electronic Code-Book (ECB) mode is considered insecure because:",
                    "options": {
                        "A": "It's too slow for modern applications",
                        "B": "Identical plaintext blocks produce identical ciphertext blocks",
                        "C": "It requires too much memory",
                        "D": "It can only encrypt small messages"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "ECB encrypts each block independently with the same key, so identical plaintext blocks produce identical ciphertext, revealing patterns."
                },
                {
                    "num": 8,
                    "question": "In CBC (Cipher-Block Chaining) mode, what is used to ensure different ciphertext for identical plaintext?",
                    "options": {
                        "A": "A counter value",
                        "B": "An initialization vector (IV)",
                        "C": "A different key for each block",
                        "D": "A hash function"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "CBC uses a random initialization vector (IV) and chains blocks together by XORing each plaintext block with the previous ciphertext block."
                },
                {
                    "num": 9,
                    "question": "Which cipher mode allows for parallel encryption and decryption?",
                    "options": {
                        "A": "CBC",
                        "B": "CTR",
                        "C": "Both A and B",
                        "D": "Neither A nor B"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "CTR (Counter) mode allows parallelization of both encryption and decryption. CBC only allows parallel decryption."
                },
                {
                    "num": 10,
                    "question": "In asymmetric encryption, to send a confidential message to Bob, Alice should encrypt with:",
                    "options": {
                        "A": "Alice's private key",
                        "B": "Alice's public key",
                        "C": "Bob's private key",
                        "D": "Bob's public key"
                    },
                    "answer": "D",
                    "points": 2,
                    "explanation": "For confidentiality: encrypt with recipient's PUBLIC key, only recipient can decrypt with their PRIVATE key."
                },
                {
                    "num": 11,
                    "question": "For n parties to communicate securely using symmetric encryption, how many keys are needed?",
                    "options": {
                        "A": "n",
                        "B": "2n",
                        "C": "n(n-1)/2",
                        "D": "n^2"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Each pair needs a unique shared key, requiring n(n-1)/2 keys. Asymmetric encryption only needs 2n keys (public/private pair per person)."
                },
                {
                    "num": 12,
                    "question": "What is the primary advantage of hybrid encryption?",
                    "options": {
                        "A": "It's more secure than pure asymmetric encryption",
                        "B": "It combines the speed of symmetric encryption with the key distribution benefits of asymmetric",
                        "C": "It uses shorter keys",
                        "D": "It doesn't require any key management"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Hybrid encryption uses asymmetric encryption to securely exchange a symmetric key, then uses faster symmetric encryption for the actual data."
                },
                {
                    "num": 13,
                    "question": "A digital signature is created by:",
                    "options": {
                        "A": "Encrypting with the sender's public key",
                        "B": "Encrypting with the sender's private key",
                        "C": "Encrypting with the recipient's public key",
                        "D": "Hashing the message"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Digital signatures: sign with sender's PRIVATE key (signing key), verify with sender's PUBLIC key (verification key)."
                },
                {
                    "num": 14,
                    "question": "Which property is NOT provided by digital signatures?",
                    "options": {
                        "A": "Data origin authentication",
                        "B": "Data integrity",
                        "C": "Confidentiality",
                        "D": "Non-repudiation"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Digital signatures provide authentication, integrity, and non-repudiation, but NOT confidentiality (anyone can verify a signature)."
                },
                {
                    "num": 15,
                    "question": "Cryptographic hash functions produce:",
                    "options": {
                        "A": "Variable-length output",
                        "B": "Fixed-length output",
                        "C": "Encrypted data",
                        "D": "Reversible transformations"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Cryptographic hash functions take arbitrary-length input and produce fixed-length output (hash value/message digest)."
                },
                {
                    "num": 16,
                    "question": "Preimage resistance (H1) means:",
                    "options": {
                        "A": "Given h, it's infeasible to find any m where H(m) = h",
                        "B": "Given m1, it's infeasible to find m2 where H(m1) = H(m2)",
                        "C": "It's infeasible to find any collision",
                        "D": "The hash is irreversible"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "Preimage resistance (one-way property): given hash value h, infeasible to find any message m that produces that hash."
                },
                {
                    "num": 17,
                    "question": "Collision resistance (H3) means:",
                    "options": {
                        "A": "Given m, you can't find H(m)",
                        "B": "Given m1, you can't find different m2 with same hash",
                        "C": "You can't find ANY two different messages with the same hash",
                        "D": "Hashes are unique"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Collision resistance: infeasible to find ANY pair of distinct inputs m1, m2 such that H(m1) = H(m2)."
                },
                {
                    "num": 18,
                    "question": "Which hash function is currently recommended for security-critical applications?",
                    "options": {
                        "A": "MD5",
                        "B": "SHA-1",
                        "C": "SHA-256 or SHA-3",
                        "D": "All of the above"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "SHA-256 (SHA-2 family) and SHA-3 are currently recommended. MD5 and SHA-1 are deprecated due to vulnerabilities."
                },
                {
                    "num": 19,
                    "question": "Message Authentication Codes (MAC) require:",
                    "options": {
                        "A": "Only the message as input",
                        "B": "Message and a secret key",
                        "C": "Public and private key pairs",
                        "D": "A hash function only"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "MACs are computed using both the message and a secret key shared between sender and receiver."
                },
                {
                    "num": 20,
                    "question": "Compared to digital signatures, MACs are:",
                    "options": {
                        "A": "Slower but more secure",
                        "B": "Faster but don't provide non-repudiation",
                        "C": "Less secure overall",
                        "D": "Require public key infrastructure"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "MACs use symmetric crypto (faster) but can't provide non-repudiation since the key is shared. Best for continuous data streams."
                }
            ]
        },
        
        # SECTION 2: TRUE/FALSE (1 point each)
        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 21,
                    "question": "Encryption algorithms are typically kept secret.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Encryption algorithms are typically non-secrets (public). Security relies on the key, not algorithm secrecy."
                },
                {
                    "num": 22,
                    "question": "Computational security assumes attackers have unlimited computing resources.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Computational security assumes attackers have FIXED computational resources, making brute-force infeasible."
                },
                {
                    "num": 23,
                    "question": "The Vernam cipher (one-time pad) is perfectly secret when used correctly.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - One-time pads are perfectly secret: observing ciphertext gives no information about plaintext (except length)."
                },
                {
                    "num": 24,
                    "question": "In ECB mode, errors in one ciphertext block affect multiple plaintext blocks during decryption.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - In ECB, errors only affect the corresponding block. Errors don't propagate."
                },
                {
                    "num": 25,
                    "question": "CBC mode encryption can be parallelized.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - CBC encryption cannot be parallelized (depends on previous block). Decryption CAN be parallelized."
                },
                {
                    "num": 26,
                    "question": "CTR mode allows both parallel encryption and parallel decryption.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - CTR mode allows parallelization of both encryption and decryption since blocks are independent."
                },
                {
                    "num": 27,
                    "question": "Asymmetric encryption is generally faster than symmetric encryption.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Asymmetric encryption is much slower than symmetric, which is why hybrid encryption is commonly used."
                },
                {
                    "num": 28,
                    "question": "Digital signatures provide confidentiality for the message content.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Digital signatures provide authentication, integrity, and non-repudiation, but NOT confidentiality."
                },
                {
                    "num": 29,
                    "question": "Collision resistance (H3) implies second-preimage resistance (H2).",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - If you can't find ANY collision, you certainly can't find a collision for a specific given message."
                },
                {
                    "num": 30,
                    "question": "MD5 is currently recommended for security-critical applications.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - MD5 is widely deprecated due to collision vulnerabilities. Use SHA-256 or SHA-3 instead."
                },
                {
                    "num": 31,
                    "question": "Cryptographic hash functions are reversible transformations.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Hash functions are one-way (preimage resistant). You cannot reverse a hash to get the original message."
                },
                {
                    "num": 32,
                    "question": "For a good hash function, changing a single input bit should change about 50% of output bits.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Good hash functions exhibit avalanche effect: small input changes cause unpredictable, large output changes."
                },
                {
                    "num": 33,
                    "question": "MACs provide non-repudiation.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - MACs don't provide non-repudiation because the key is shared; either party could have created the MAC."
                },
                {
                    "num": 34,
                    "question": "MACs on their own ensure message freshness and prevent replay attacks.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - MACs verify integrity and authentication but don't prevent replay. Additional mechanisms (nonces, timestamps) are needed."
                },
                {
                    "num": 35,
                    "question": "In the RSA algorithm, the public key consists of {e, n}.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - RSA public key is PU = {e, n}, private key is PR = {d, n}, where n = pq (product of two primes)."
                },
                {
                    "num": 36,
                    "question": "Hybrid encryption uses asymmetric encryption for the entire message.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Hybrid uses asymmetric encryption only for the symmetric key, then symmetric encryption for the message payload."
                },
                {
                    "num": 37,
                    "question": "A chosen-plaintext attack is more powerful than a known-plaintext attack.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Chosen-plaintext allows attacker to choose specific plaintexts and see resulting ciphertexts, providing more control."
                },
                {
                    "num": 38,
                    "question": "AES is a block cipher with a block length of 128 bits.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - AES has a fixed block length of 128 bits and supports key lengths of 128, 192, or 256 bits."
                },
                {
                    "num": 39,
                    "question": "DES has a key length of 128 bits.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - DES has a key length of only 56 bits (too short by modern standards), which is why it was replaced by AES."
                },
                {
                    "num": 40,
                    "question": "Birthday paradox makes finding collisions easier than finding preimages.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Due to birthday paradox, collision attacks require roughly 2^(n/2) operations vs 2^n for preimage attacks on n-bit hashes."
                }
            ]
        },
        
        # SECTION 3: SHORT ANSWER (2 points each)
        "section3": {
            "title": "Section 3: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 41,
                    "question": "Name TWO types of attack models where the adversary is ACTIVE (separate with comma):",
                    "answer": ["chosen-plaintext", "chosen-ciphertext", "chosen plaintext", "chosen ciphertext"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Active adversary attack models: Chosen-plaintext attack and Chosen-ciphertext attack. (Passive: Ciphertext-only, Known-plaintext)"
                },
                {
                    "num": 42,
                    "question": "What does AES stand for?",
                    "answer": ["advanced encryption standard", "aes"],
                    "points": 2,
                    "type": "text",
                    "explanation": "AES = Advanced Encryption Standard, the current standard symmetric encryption algorithm (Rijndael, 1998)."
                },
                {
                    "num": 43,
                    "question": "In CTR mode, what must be ensured about the IV + counter value to maintain security?",
                    "answer": ["never repeat", "never repeats", "unique", "must not repeat", "no repeat"],
                    "points": 2,
                    "type": "text",
                    "explanation": "In CTR mode, IV + i must NEVER repeat across encryptions with the same key to maintain security."
                },
                {
                    "num": 44,
                    "question": "What is the formula used in the Vernam cipher (one-time pad)?",
                    "answer": ["c = m xor k", "m xor k", "c=m⊕k", "xor"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Vernam cipher uses XOR: c = m ⊕ k (ciphertext = message XOR key), where key length = message length."
                },
                {
                    "num": 45,
                    "question": "Name ONE cryptographic property that hash functions must satisfy:",
                    "answer": ["preimage resistance", "one-way", "second-preimage resistance", "collision resistance", "one way"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Hash functions must satisfy: H1 (preimage/one-way), H2 (second-preimage resistance), H3 (collision resistance)."
                },
                {
                    "num": 46,
                    "question": "To verify a digital signature, whose public key do you use?",
                    "answer": ["sender", "signer", "sender's", "signer's"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Verify signature using sender's/signer's PUBLIC (verification) key. Signature created with sender's PRIVATE (signing) key."
                },
                {
                    "num": 47,
                    "question": "What type of encryption (symmetric or asymmetric) is used in MACs?",
                    "answer": ["symmetric", "secret key"],
                    "points": 2,
                    "type": "text",
                    "explanation": "MACs use symmetric encryption with a shared secret key, making them much faster than digital signatures."
                },
                {
                    "num": 48,
                    "question": "Why is ECB mode considered insecure?",
                    "answer": ["identical blocks", "same plaintext", "patterns", "identical plaintext blocks produce identical ciphertext"],
                    "points": 2,
                    "type": "text",
                    "explanation": "ECB is insecure because identical plaintext blocks produce identical ciphertext blocks, revealing patterns (e.g., ECB penguin)."
                },
                {
                    "num": 49,
                    "question": "What does IV stand for in cipher modes like CBC?",
                    "answer": ["initialization vector", "init vector"],
                    "points": 2,
                    "type": "text",
                    "explanation": "IV = Initialization Vector, a random value used to ensure different ciphertext for identical plaintext in modes like CBC."
                },
                {
                    "num": 50,
                    "question": "Information-theoretic security means security even against adversaries with _______ computing power:",
                    "answer": ["unlimited", "infinite", "unbounded", "unbound"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Information-theoretic security (like one-time pads) is secure even against adversaries with unlimited/unbounded computing power."
                }
            ]
        }
    }
