import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("=" * 80)
    print("SYSC 4810: Introduction to Network and Software Security")
    print("Chapter 1 Quiz - Fall 2024")
    print("=" * 80)
    print("Time Limit: 30 Minutes")
    print("Total Points: 100")
    print("=" * 80)
    print()

def countdown_timer(seconds):
    """Display countdown warning"""
    mins = seconds // 60
    secs = seconds % 60
    print(f"\n⏰ Time remaining: {mins:02d}:{secs:02d}")

def show_feedback(user_answer, correct_answer, is_correct, points_earned, total_points, explanation=""):
    """Show immediate feedback after each answer"""
    print("\n" + "-" * 80)
    if is_correct:
        print(f"✓ CORRECT! (+{points_earned} points)")
    else:
        print(f"✗ INCORRECT (0 points)")
        print(f"Your answer: {user_answer}")
        print(f"Correct answer: {correct_answer}")
    
    if explanation:
        print(f"\n💡 Explanation: {explanation}")
    
    print("-" * 80)
    input("\nPress ENTER to continue...")

def run_quiz():
    clear_screen()
    display_header()
    
    input("Press ENTER to begin the quiz...")
    start_time = time.time()
    time_limit = 30 * 60  # 30 minutes in seconds
    
    # Store user answers
    user_answers = {}
    score = 0
    total_points = 100
    
    # Quiz questions with answers, points, and explanations
    questions = {
        # SECTION 1: MULTIPLE CHOICE (2 points each)
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "The CIA Triad consists of which three security objectives?",
                    "options": {
                        "A": "Confidentiality, Integrity, Authentication",
                        "B": "Confidentiality, Integrity, Availability",
                        "C": "Confidentiality, Information disclosure, Availability",
                        "D": "Confidentiality, Integrity, Accountability"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The CIA Triad is the foundation of security: Confidentiality (data access control), Integrity (data accuracy), and Availability (resource accessibility)."
                },
                {
                    "num": 2,
                    "question": "Which of the following is an example of a passive attack?",
                    "options": {
                        "A": "Modifying messages sent between Alice and Bob",
                        "B": "Replaying authentication sequences",
                        "C": "Traffic analysis - observing frequency and length of messages",
                        "D": "Suppressing messages directed to a security audit service"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Passive attacks observe/monitor data without altering it. Traffic analysis observes patterns. Active attacks modify, suppress, or replay data."
                },
                {
                    "num": 3,
                    "question": "In asymmetric encryption, which key does Alice use to encrypt a message to Bob?",
                    "options": {
                        "A": "Bob's public key",
                        "B": "Bob's private key",
                        "C": "Alice's private key",
                        "D": "The shared secret key"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "For confidentiality in asymmetric encryption: encrypt with recipient's PUBLIC key, decrypt with recipient's PRIVATE key. Only Bob can decrypt with his private key."
                },
                {
                    "num": 4,
                    "question": "For digital signature generation, which key does Bob (the signer) use?",
                    "options": {
                        "A": "Bob's public key",
                        "B": "Bob's private key",
                        "C": "Alice's public key",
                        "D": "Alice's private key"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Digital signatures: Sign with sender's PRIVATE key, verify with sender's PUBLIC key. This proves the message came from Bob."
                },
                {
                    "num": 5,
                    "question": "Risk is calculated using which formula?",
                    "options": {
                        "A": "R = T + V",
                        "B": "R = T × V × C",
                        "C": "R = P × C",
                        "D": "R = V ÷ C"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Risk = Probability × Consequence. Some sources also show R = T×V×C (Threat × Vulnerability × Cost), but the lecture primarily used R = P×C."
                },
                {
                    "num": 6,
                    "question": "Which is NOT a component of adversary modeling?",
                    "options": {
                        "A": "Objectives (target assets/systems)",
                        "B": "Methods (attack techniques)",
                        "C": "Countermeasures",
                        "D": "Motivation"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Adversary modeling includes: Objectives, Methods, Capabilities, and Motivation. Countermeasures are part of the defense/security design, not adversary modeling."
                },
                {
                    "num": 7,
                    "question": "In the STRIDE threat modeling framework, what does the 'R' stand for?",
                    "options": {
                        "A": "Reconnaissance",
                        "B": "Repudiation",
                        "C": "Replay",
                        "D": "Request forgery"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "STRIDE: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Escalation of privilege."
                },
                {
                    "num": 8,
                    "question": "Which security design principle states that systems should deny access by default?",
                    "options": {
                        "A": "P1: Simplicity-and-necessity",
                        "B": "P2: Safe-defaults",
                        "C": "P4: Complete-mediation",
                        "D": "P6: Least-privilege"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P2: Safe-defaults means deny access by default, fail safe, use strong default passwords, and HTTPS by design."
                },
                {
                    "num": 9,
                    "question": "The principle 'Security by obscurity' is:",
                    "options": {
                        "A": "Recommended as a primary defense",
                        "B": "NOT recommended (violates P3: Open-design)",
                        "C": "Part of defense-in-depth",
                        "D": "Required for all systems"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P3: Open-design principle states security should NOT rely on obscurity. Systems should be secure even if the design is public."
                },
                {
                    "num": 10,
                    "question": "Which principle requires that every access to a resource must be checked for authorization?",
                    "options": {
                        "A": "P2: Safe-defaults",
                        "B": "P3: Open-design",
                        "C": "P4: Complete-mediation",
                        "D": "P5: Isolated-compartments"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "P4: Complete-mediation means every access must be checked through authentication and authorization, every time."
                },
                {
                    "num": 11,
                    "question": "The principle of P6: Least-privilege means:",
                    "options": {
                        "A": "Users should have minimal passwords",
                        "B": "Systems should have minimal features",
                        "C": "Grant only necessary permissions (e.g., don't distribute super accounts)",
                        "D": "Use the smallest possible encryption keys"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "P6: Least-privilege means give only the minimum permissions needed. Example: don't distribute super/admin accounts unnecessarily."
                },
                {
                    "num": 12,
                    "question": "P8: Small-trusted-bases advocates for:",
                    "options": {
                        "A": "Using only small software packages",
                        "B": "Microkernel architectures and separating algorithms from secrets",
                        "C": "Limiting the number of users",
                        "D": "Small network designs"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P8: Small-trusted-bases favors microkernel architectures (vs monolithic) and separating crypto algorithms from secrets. Smaller trusted base = easier to verify."
                },
                {
                    "num": 13,
                    "question": "Which principle states that designs should align with users' mental models?",
                    "options": {
                        "A": "P9: Time-tested tools",
                        "B": "P10: Least surprise",
                        "C": "P11: User-buy-in",
                        "D": "P12: Sufficient-work-factor"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P10: Least surprise means align with users' mental models, tailor to target users, make systems intuitive to avoid mistakes."
                },
                {
                    "num": 14,
                    "question": "P13: Defence-in-depth means:",
                    "options": {
                        "A": "Bury critical systems underground",
                        "B": "Use only the strongest single defense mechanism",
                        "C": "Place defense mechanisms at each stage to avoid single points of failure",
                        "D": "Focus only on network perimeter security"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "P13: Defence-in-depth means layered security - place defenses at each stage, avoid single points of failure. Also includes defense-in-breadth."
                },
                {
                    "num": 15,
                    "question": "P15: Data-type-verification requires:",
                    "options": {
                        "A": "Sanitizing all input regardless of source",
                        "B": "Only validating external inputs",
                        "C": "Only checking data types at compile time",
                        "D": "Trusting internal data sources"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "P15: Data-type-verification means sanitize ANY input, no matter where it came from. Never trust any input source."
                },
                {
                    "num": 16,
                    "question": "Which statement about testing and security is TRUE?",
                    "options": {
                        "A": "Complete security testing is possible with enough time",
                        "B": "Security testing is necessarily incomplete",
                        "C": "Passing all tests proves a system is secure",
                        "D": "Black box testing can find all vulnerabilities"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Testing is necessarily incomplete - we cannot test for unknown/unforeseen attacks. The universe of potential exploits is unknown."
                },
                {
                    "num": 17,
                    "question": "Security is described as 'unobservable' because:",
                    "options": {
                        "A": "Security mechanisms are always hidden",
                        "B": "We can observe security directly through metrics",
                        "C": "We cannot prove the absence of vulnerabilities",
                        "D": "Security testing is not allowed"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Security is unobservable - we cannot prove absence of vulnerabilities (like proving all swans are white). We only observe when security fails."
                },
                {
                    "num": 18,
                    "question": "Which is a reason why security is hard?",
                    "options": {
                        "A": "Defenders must protect all vulnerabilities; attackers need only find one",
                        "B": "Attackers follow strict rules and protocols",
                        "C": "Software complexity has decreased over time",
                        "D": "All developers receive extensive security training"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "Defender-attacker asymmetry: defenders must protect ALL attack surfaces, but attackers only need to find ONE weakness."
                },
                {
                    "num": 19,
                    "question": "The Internet threat model traditionally assumes:",
                    "options": {
                        "A": "End-points are trustworthy; communication links are under attacker control",
                        "B": "Both end-points and links are under attacker control",
                        "C": "End-points are compromised; links are secure",
                        "D": "Everything is secure by default"
                    },
                    "answer": "A",
                    "points": 2,
                    "explanation": "Traditional Internet threat model: end-points (client/server) are trusted, but communication links are insecure (attacker can eavesdrop, modify). This follows the historic cryptographer's model."
                },
                {
                    "num": 20,
                    "question": "Which is NOT one of the 'Why Security is Hard' factors?",
                    "options": {
                        "A": "Intelligent, adaptive adversary",
                        "B": "Defender-attacker asymmetry",
                        "C": "Simple, unchanging software",
                        "D": "User non-compliance"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "Software COMPLEXITY (not simplicity) is a major reason security is hard. Complexity is the enemy of security. Rapid pace of evolution also makes it harder."
                }
            ]
        },
        
        # SECTION 2: TRUE/FALSE (1 point each)
        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 21,
                    "question": "Authentication provides assurance that data or software is genuine.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "Authentication verifies identity/genuineness - that a principal, data, or software is what it claims to be."
                },
                {
                    "num": 22,
                    "question": "Authorization is the same as authentication.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Authentication = verifying identity ('who are you?'). Authorization = determining access rights ('what can you access?')."
                },
                {
                    "num": 23,
                    "question": "Accountability refers to the ability to identify principals responsible for past actions.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Accountability enables identifying who did what, crucial for forensics and non-repudiation."
                },
                {
                    "num": 24,
                    "question": "'Trusted' and 'trustworthy' mean the same thing in security contexts.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - 'Trusted' = HAS our confidence (we rely on it). 'Trustworthy' = DESERVES our confidence (actually secure)."
                },
                {
                    "num": 25,
                    "question": "A security policy specifies what is and is not allowed in a system.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Security policy specifies the design intent of rules and practices - what is and is not (supposed to be) allowed."
                },
                {
                    "num": 26,
                    "question": "A threat is the same as an attack.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Threat = potential/circumstances that might cause harm. Attack = deliberate execution of steps to cause a security violation."
                },
                {
                    "num": 27,
                    "question": "Controls and countermeasures are terms for the same concept.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Both terms refer to mechanisms that support and enforce security policies."
                },
                {
                    "num": 28,
                    "question": "Outsider attacks are launched without any prior special access to the target network.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Outsider attacks have no prior access. Insider attacks originate from parties with starting advantage/access."
                },
                {
                    "num": 29,
                    "question": "In qualitative risk assessment, C represents 'Cost or impact' and P represents 'Probability.'",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - In the risk matrix shown, C = cost/impact and P = probability, resulting in risk levels 1-5."
                },
                {
                    "num": 30,
                    "question": "Cost-benefit analysis helps with deciding security budgets.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Cost-benefit analysis weighs security investment costs against potential losses, helping budget decisions."
                },
                {
                    "num": 31,
                    "question": "Attack trees output a complete list of all possible attacks.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Attack trees produce extensive lists but usually INCOMPLETE. They help identify many attacks but cannot guarantee completeness."
                },
                {
                    "num": 32,
                    "question": "Checklists are best used as the sole method for threat modeling.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Checklists are best used as COMPLEMENTARY tools, not as the sole method. They help ensure known threats aren't overlooked but lack system-specific context."
                },
                {
                    "num": 33,
                    "question": "STRIDE's 'S' stands for 'Spoofing' - attempts to impersonate.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - S = Spoofing (impersonation of entities or things)."
                },
                {
                    "num": 34,
                    "question": "STRIDE's 'D' stands for 'Denial of service.'",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - D = Denial of service (impacting availability/quality through malicious actions)."
                },
                {
                    "num": 35,
                    "question": "Penetration testing traditionally uses white-box methods.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Pen testing TRADITIONALLY uses black-box methods. White-box pen testing increases chances of finding vulnerabilities but is not traditional."
                },
                {
                    "num": 36,
                    "question": "Certification requires third-party lab reviewing and can be costly and time-consuming.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Certification involves third-party evaluation, is costly/time-consuming, and requires re-certification even for small changes."
                },
                {
                    "num": 37,
                    "question": "Security evaluation is needed only once during a product's lifecycle.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Security analysis should begin early and continue iteratively throughout the product lifecycle, not just once."
                },
                {
                    "num": 38,
                    "question": "P1: Simplicity-and-necessity suggests minimizing attack surfaces.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - P1 advocates minimal installs, minimal functionality to minimize attack surfaces."
                },
                {
                    "num": 39,
                    "question": "P7: Modular-design favors monolithic kernel architectures.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - P7 favors object-oriented and fine-grained designs. The Tanenbaum vs Torvalds debate: P8 favors MICROkernel, not monolithic."
                },
                {
                    "num": 40,
                    "question": "P17: Trust-anchor-justification warns that trust anchors are dangerous and their trustworthiness must be ensured.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Trust anchors are dangerous single points of trust. Their trustworthiness must be carefully justified and verified."
                }
            ]
        },
        
        # SECTION 3: SCENARIO-BASED (3 points each)
        "section3": {
            "title": "Section 3: Scenario-Based Questions (3 points each)",
            "questions": [
                {
                    "num": 41,
                    "question": "Consider a firewall rule table. An external client (10.2.4.56) sends a UDP packet from port 1234 to an internal Kerberos server (172.24.31.1) on port 88. A rule states: 'In, External, Internal, UDP, >1023, 88, Permit.' Will this packet be permitted or denied?",
                    "options": {
                        "A": "Permitted",
                        "B": "Denied",
                        "C": "Depends on other rules",
                        "D": "Cannot determine"
                    },
                    "answer": "A",
                    "points": 3,
                    "explanation": "PERMITTED - The packet matches: Direction=In, Src=External (10.2.4.56), Dest=Internal (172.24.31.1), Protocol=UDP, Src Port=1234 (>1023), Dest Port=88. Rule action: Permit."
                },
                {
                    "num": 42,
                    "question": "In a house security policy: 'Only family members may remove objects.' An unlocked back door is a _______, and a stranger entering through it is an _______.",
                    "options": {
                        "A": "Vulnerability; Attack",
                        "B": "Threat; Vulnerability",
                        "C": "Attack; Security violation",
                        "D": "Security violation; Threat"
                    },
                    "answer": "A",
                    "points": 3,
                    "explanation": "Unlocked door = VULNERABILITY (weakness that can be exploited). Stranger entering and taking items = ATTACK (deliberate execution exploiting the vulnerability)."
                },
                {
                    "num": 43,
                    "question": "A web application uses a list of one-time passwords. A phishing site asks for multiple passwords from the list. This threat modeling failure demonstrates:",
                    "options": {
                        "A": "Successful defense-in-depth",
                        "B": "Failure to consider all attack vectors",
                        "C": "Proper adversary modeling",
                        "D": "Effective security policy"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This is an example of FAILED threat modeling - the designers didn't anticipate an attacker asking for MULTIPLE passwords from the list (via phishing), only anticipated single password leaks."
                },
                {
                    "num": 44,
                    "question": "Alice wants to send Bob a confidential message. Which encryption approach and key should she use?",
                    "options": {
                        "A": "Symmetric encryption with a shared secret key",
                        "B": "Asymmetric encryption with Alice's private key",
                        "C": "Asymmetric encryption with Bob's public key",
                        "D": "Either A or C"
                    },
                    "answer": "D",
                    "points": 3,
                    "explanation": "For CONFIDENTIALITY, both work: (A) Symmetric with shared secret key, or (C) Asymmetric with Bob's public key. Both ensure only Bob can decrypt. (B) would be for authentication/signatures, not confidentiality."
                },
                {
                    "num": 45,
                    "question": "An online bank disables transfers to prevent account compromise, but attackers purchase the bank's own products with stolen funds. This is an example of:",
                    "options": {
                        "A": "Successful threat modeling",
                        "B": "Failed threat modeling - wrong threats prioritized",
                        "C": "Effective risk mitigation",
                        "D": "Proper defense-in-depth"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "FAILED threat modeling - the bank focused on the wrong threat (transfers) but didn't consider attackers could still use funds to buy products. Demonstrates failure to consider all attack vectors."
                }
            ]
        },
        
        # SECTION 4: SHORT ANSWER (2 points each)
        "section4": {
            "title": "Section 4: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 46,
                    "question": "Name TWO attack types that are classified as ACTIVE attacks (separate with comma):",
                    "answer": ["denial of service", "replay", "masquerade", "modification"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Active attacks include: Denial of Service, Replay, Masquerade, Modification of Messages. (Passive attacks: Traffic Analysis, Release of Message Contents)"
                },
                {
                    "num": 47,
                    "question": "In diagram-driven threat modeling, what visual element is used to delimit trust domains?",
                    "answer": ["system gateways", "trust boundaries", "boundaries", "gateways", "rectangles"],
                    "points": 2,
                    "type": "text",
                    "explanation": "System gateways/trust boundaries are marked (often with rectangles) where system controls restrict or filter communications, delimiting trust domains."
                },
                {
                    "num": 48,
                    "question": "What does HP1: Security-by-design mean? (Brief answer)",
                    "answer": ["don't make security an independent layer", "integrate security from start", "security from design", "not added at end", "integrate from beginning"],
                    "points": 2,
                    "type": "text",
                    "explanation": "HP1: Security-by-design means do NOT make security an independent added layer at the end. Integrate security from the beginning of design."
                },
                {
                    "num": 49,
                    "question": "Name ONE way assurance is achieved:",
                    "answer": ["testing", "pen testing", "penetration testing", "formal modeling", "design practices", "sound design", "experience", "analysis", "code review"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Assurance comes from: sound design practices, testing (pen testing), formal modeling, ad hoc analysis, and heavy reliance on experience."
                },
                {
                    "num": 50,
                    "question": "According to the lecture, 'complexity is the enemy of _________.'",
                    "answer": ["security"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Complexity is the enemy of SECURITY. Software complexity makes systems harder to secure and analyze."
                }
            ]
        }
    }
    
    # Run through each section
    for section_key, section_data in questions.items():
        clear_screen()
        print("\n" + "=" * 80)
        print(section_data["title"])
        print("=" * 80 + "\n")
        
        for q in section_data["questions"]:
            # Check time
            elapsed = time.time() - start_time
            if elapsed > time_limit:
                print("\n⏰ TIME'S UP! Quiz auto-submitted.")
                break
            
            # Show time warning at 25 minutes
            if elapsed > 25 * 60 and elapsed < 25 * 60 + 5:
                countdown_timer(int(time_limit - elapsed))
            
            print(f"\nQuestion {q['num']}:")
            print(f"{q['question']}")
            
            # Multiple choice or scenario questions with options
            if "options" in q:
                print()
                for key, value in q["options"].items():
                    print(f"  {key}) {value}")
                print()
                while True:
                    answer = input("Your answer: ").strip().upper()
                    if answer in q["options"].keys():
                        user_answers[q['num']] = answer
                        is_correct = (answer == q['answer'])
                        points_earned = q['points'] if is_correct else 0
                        score += points_earned
                        
                        show_feedback(
                            answer,
                            q['answer'],
                            is_correct,
                            points_earned,
                            q['points'],
                            q.get('explanation', '')
                        )
                        break
                    else:
                        print("Invalid choice. Please enter a valid option.")
            
            # True/False questions
            elif q.get('points') == 1 and section_key == "section2":
                print()
                while True:
                    answer = input("Your answer (T/F): ").strip().upper()
                    if answer in ['T', 'F']:
                        user_answers[q['num']] = answer
                        is_correct = (answer == q['answer'])
                        points_earned = q['points'] if is_correct else 0
                        score += points_earned
                        
                        show_feedback(
                            answer,
                            q['answer'],
                            is_correct,
                            points_earned,
                            q['points'],
                            q.get('explanation', '')
                        )
                        break
                    else:
                        print("Invalid choice. Please enter T or F.")
            
            # Short answer
            else:
                print()
                answer = input("Your answer: ").strip().lower()
                user_answers[q['num']] = answer
                
                # Check if answer contains any of the acceptable answers
                points_earned = 0
                if q.get('type') == 'multi_text':
                    # Check if at least 2 acceptable answers in response
                    count = sum(1 for acceptable in q['answer'] if acceptable in answer)
                    if count >= 2:
                        points_earned = q['points']
                        is_correct = True
                    elif count == 1:
                        points_earned = q['points'] / 2
                        is_correct = False
                    else:
                        is_correct = False
                    
                    score += points_earned
                    correct_display = f"Any 2 of: {', '.join(q['answer'])}"
                    show_feedback(
                        answer,
                        correct_display,
                        is_correct,
                        points_earned,
                        q['points'],
                        q.get('explanation', '')
                    )
                    
                elif q.get('type') == 'text':
                    if any(acceptable in answer for acceptable in q['answer']):
                        points_earned = q['points']
                        is_correct = True
                    else:
                        is_correct = False
                    
                    score += points_earned
                    correct_display = f"Any of: {', '.join(q['answer'])}"
                    show_feedback(
                        answer,
                        correct_display,
                        is_correct,
                        points_earned,
                        q['points'],
                        q.get('explanation', '')
                    )
        
        # Check if time expired
        elapsed = time.time() - start_time
        if elapsed > time_limit:
            break
    
    # Display results
    clear_screen()
    print("\n" + "=" * 80)
    print("QUIZ COMPLETE!")
    print("=" * 80 + "\n")
    
    elapsed_time = time.time() - start_time
    mins = int(elapsed_time // 60)
    secs = int(elapsed_time % 60)
    
    print(f"Time taken: {mins} minutes and {secs} seconds")
    print(f"\nYour Score: {score}/{total_points}")
    percentage = (score / total_points) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Letter grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 85:
        grade = "A"
    elif percentage >= 80:
        grade = "A-"
    elif percentage >= 77:
        grade = "B+"
    elif percentage >= 73:
        grade = "B"
    elif percentage >= 70:
        grade = "B-"
    elif percentage >= 67:
        grade = "C+"
    elif percentage >= 63:
        grade = "C"
    elif percentage >= 60:
        grade = "C-"
    elif percentage >= 57:
        grade = "D+"
    elif percentage >= 53:
        grade = "D"
    elif percentage >= 50:
        grade = "D-"
    else:
        grade = "F"
    
    print(f"Letter Grade: {grade}")
    print("\n" + "=" * 80)
    
    # Show summary
    print(f"\n📊 QUIZ SUMMARY")
    print(f"Total Questions: 50")
    print(f"Points Earned: {score}/{total_points}")
    print(f"Time Used: {mins}m {secs}s of 30m")
    print("\n" + "=" * 80)

if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("Welcome to SYSC 4810 Chapter 1 Quiz")
    print("=" * 80)
    print("\nIMPORTANT:")
    print("- You have 30 minutes to complete this quiz")
    print("- Once started, the timer cannot be paused")
    print("- No extra time will be given if you start late")
    print("- Be specific in your answers")
    print("- You will receive immediate feedback after each answer")
    print("\n" + "=" * 80)
    
    ready = input("\nAre you ready to begin? (yes/no): ").strip().lower()
    if ready in ['yes', 'y']:
        run_quiz()
    else:
        print("\nQuiz cancelled. Come back when you're ready!")
                    