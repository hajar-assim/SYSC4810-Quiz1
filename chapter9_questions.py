def get_human_centric_security_questions():
    """Returns Human-centric Security and Privacy questions"""
    return {
        "section1": {
            "title": "Section 1: Multiple Choice (2 points each)",
            "questions": [
                {
                    "num": 1,
                    "question": "What does the security design principle P10 (Least Surprise) emphasize?",
                    "options": {
                        "A": "Making security mechanisms as complex as possible",
                        "B": "Aligning designs with users' mental models and tailoring to target users' experience",
                        "C": "Surprising attackers with unexpected security measures",
                        "D": "Keeping all security mechanisms hidden from users"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P10 Least Surprise emphasizes aligning designs with users' mental models, tailoring to the experience of target users. Simpler, easier-to-use, usable mechanisms yield fewer surprises."
                },
                {
                    "num": 2,
                    "question": "According to P10 (Least Surprise), what is the problem with designs suited for trained experts?",
                    "options": {
                        "A": "They are too expensive to implement",
                        "B": "They may be unintuitive or trigger mistakes by typical end users",
                        "C": "They don't work with modern systems",
                        "D": "They are not secure enough"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Designs suited for trained experts but unintuitive or triggering mistakes by typical end users are problematic according to P10. The design should match the target users' experience level."
                },
                {
                    "num": 3,
                    "question": "What does the security design principle P11 (User Buy-in) focus on?",
                    "options": {
                        "A": "Making users pay for security features",
                        "B": "Designing systems that encourage users to behave securely",
                        "C": "Requiring users to sign security agreements",
                        "D": "Blocking users who don't follow security protocols"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P11 User Buy-in focuses on designing systems that encourage users to behave securely, rather than forcing compliance or punishing violations."
                },
                {
                    "num": 4,
                    "question": "What does P13 (Defence-in-Depth) recommend?",
                    "options": {
                        "A": "Using only one very strong security mechanism",
                        "B": "Placing a defence mechanism at each stage where one can be placed and avoiding single points of failure",
                        "C": "Focusing all security resources on the perimeter",
                        "D": "Relying primarily on user education"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "P13 Defence-in-Depth recommends placing a defence mechanism at each stage where one can be placed, avoiding single points of failure, and defence in breadth."
                },
                {
                    "num": 5,
                    "question": "In the comparison between Users and Attackers, which statement is TRUE about users?",
                    "options": {
                        "A": "Users are security-focused and vigilant",
                        "B": "Users focus on their primary task and treat security as a secondary task",
                        "C": "Users are well-educated about security threats",
                        "D": "Users are well-motivated to maintain security"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Users focus on their primary task, treating security as a secondary task. They are not vigilant, may misunderstand threats, and may misunderstand defences."
                },
                {
                    "num": 6,
                    "question": "According to the slides, what characteristics describe attackers?",
                    "options": {
                        "A": "Unmotivated, distracted, and poorly equipped",
                        "B": "Security-focused, intelligent, adaptable, well-educated, well-equipped, and well-motivated",
                        "C": "Similar to regular users in their approach",
                        "D": "Only focused on financial gain"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Attackers are characterized as security-focused, intelligent, adaptable, well-educated, well-equipped, and well-motivated - essentially the opposite of typical users regarding security focus."
                },
                {
                    "num": 7,
                    "question": "What is the 'Unmotivated User Property' in security?",
                    "options": {
                        "A": "Users who refuse to use any technology",
                        "B": "The fact that security is a secondary task for users, and education is not the magic solution",
                        "C": "Users who actively try to break security",
                        "D": "Users who only use security when paid to do so"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The Unmotivated User Property refers to security being a secondary task for users. Designers should not make assumptions, and education is not the magic solution."
                },
                {
                    "num": 8,
                    "question": "What is the 'Lack of Feedback Property' in security?",
                    "options": {
                        "A": "Users don't provide feedback on security systems",
                        "B": "Security systems don't collect user data",
                        "C": "Good feedback in security is complicated to provide",
                        "D": "Feedback loops are always negative"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The Lack of Feedback Property refers to the fact that good feedback in security is complicated to provide. Users often don't know if their security behaviors are effective."
                },
                {
                    "num": 9,
                    "question": "What is the 'Privacy Paradox'?",
                    "options": {
                        "A": "Privacy is impossible to achieve in the digital age",
                        "B": "Users' stated preferences and attitudes toward privacy do not match their behaviors",
                        "C": "Privacy and security are always in conflict",
                        "D": "Companies that promise privacy collect the most data"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The Privacy Paradox refers to the disconnect where users' stated preferences and attitudes toward privacy do not match their behaviors. Users say they are concerned about data collection but still provide personal info for small rewards."
                },
                {
                    "num": 10,
                    "question": "What is the 'Privacy Calculus'?",
                    "options": {
                        "A": "A mathematical formula to measure privacy",
                        "B": "Privacy as a trade-off where individuals weigh expected loss of privacy against potential gain of disclosure",
                        "C": "A method to calculate the cost of privacy breaches",
                        "D": "A regulation governing privacy calculations"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "Privacy Calculus views privacy as a trade-off where individuals weigh the expected loss of privacy against the potential gain of disclosure. However, the question remains whether this analysis is accurate."
                },
                {
                    "num": 11,
                    "question": "According to the slides, for security to succeed, how many users need to behave correctly vs. how many attackers need to succeed?",
                    "options": {
                        "A": "One user needs to behave correctly; all attackers need to succeed",
                        "B": "All users need to behave correctly; just one attacker needs to succeed",
                        "C": "Half the users need to behave correctly; half the attackers need to succeed",
                        "D": "No users need to behave correctly; no attackers will succeed"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The slides emphasize the asymmetry: ALL users need to behave correctly for security to work, but JUST ONE attacker needs to succeed to cause a breach."
                },
                {
                    "num": 12,
                    "question": "According to Alan F. Westin (quoted in the slides), privacy issues are fundamentally matters of:",
                    "options": {
                        "A": "Technology and encryption",
                        "B": "Values, interests and power",
                        "C": "Laws and regulations",
                        "D": "Corporate policies"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "According to Alan F. Westin, legal and policy scholar, 'privacy issues are fundamentally matters of values, interests and power.'"
                },
                {
                    "num": 13,
                    "question": "The problematic properties of security (unmotivated user and lack of feedback) apply to:",
                    "options": {
                        "A": "Only end-users",
                        "B": "Only security professionals",
                        "C": "Both end-users and potentially others (the slide questions if it's applicable only to end-users)",
                        "D": "Only attackers"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The slide poses the question 'Applicable only to end-users?' suggesting these problematic properties may apply more broadly than just end-users."
                },
                {
                    "num": 14,
                    "question": "The slide showing Signal vs WhatsApp data collection practices illustrates:",
                    "options": {
                        "A": "That all messaging apps collect the same data",
                        "B": "That users have choices about privacy based on the apps they use",
                        "C": "That WhatsApp collects no user data",
                        "D": "That Signal requires more personal information than WhatsApp"
                    },
                    "answer": "B",
                    "points": 2,
                    "explanation": "The comparison shows that Signal collects minimal data (only Contact Info not linked to identity) while WhatsApp collects extensive data linked to identity (purchases, location, contacts, identifiers, usage data, etc.), illustrating that users have choices."
                },
                {
                    "num": 15,
                    "question": "What does the slide about password meters suggest about security advice?",
                    "options": {
                        "A": "Password meters always give perfect advice",
                        "B": "Users should always follow password meter recommendations",
                        "C": "We may not always give users good or consistent advice",
                        "D": "Password meters are not useful at all"
                    },
                    "answer": "C",
                    "points": 2,
                    "explanation": "The slide asks 'Do we always give users good/consistent advice?' - suggesting that security advice (like password strength meters) may not always be reliable or consistent."
                }
            ]
        },

        "section2": {
            "title": "Section 2: True/False (1 point each)",
            "questions": [
                {
                    "num": 16,
                    "question": "According to P10 (Least Surprise), simpler and easier-to-use mechanisms yield fewer surprises for users.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - P10 states that simpler, easier-to-use, usable mechanisms yield fewer surprises."
                },
                {
                    "num": 17,
                    "question": "Education is presented as the magic solution to security problems with users.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The slides explicitly state that 'Education is not the magic solution!' under the Unmotivated User Property."
                },
                {
                    "num": 18,
                    "question": "Users typically focus on security as their primary task.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Users focus on their primary task, and security is a secondary task for them."
                },
                {
                    "num": 19,
                    "question": "Attackers are characterized as well-motivated and well-equipped.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The slides describe attackers as security-focused, intelligent, adaptable, well-educated, well-equipped, and well-motivated."
                },
                {
                    "num": 20,
                    "question": "The Privacy Paradox describes how users' stated privacy concerns match their actual behaviors.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The Privacy Paradox describes the opposite: users' stated preferences and attitudes toward privacy do NOT match their behaviors."
                },
                {
                    "num": 21,
                    "question": "In the Privacy Paradox, users are often willing to provide personal information for just a small reward.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Users say they are concerned about data collection, yet are still willing to provide personal info, often for just small rewards."
                },
                {
                    "num": 22,
                    "question": "Defence-in-Depth recommends relying on a single, very strong security mechanism.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Defence-in-Depth recommends placing defences at each stage where one can be placed and avoiding single points of failure."
                },
                {
                    "num": 23,
                    "question": "Users are typically vigilant about security threats according to the slides.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The slides indicate that users are 'Not vigilant' when it comes to security."
                },
                {
                    "num": 24,
                    "question": "The Privacy Calculus suggests that individuals weigh the expected loss of privacy against the potential gain of disclosure.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - Privacy Calculus is described as a trade-off where individuals weigh the expected loss of privacy against the potential gain of disclosure."
                },
                {
                    "num": 25,
                    "question": "Designers should make assumptions about users' security knowledge.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - Under the Unmotivated User Property, it states that 'Designers should not make assumptions.'"
                },
                {
                    "num": 26,
                    "question": "Good feedback in security systems is straightforward and easy to implement.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The Lack of Feedback Property states that 'Good feedback is complicated!'"
                },
                {
                    "num": 27,
                    "question": "P13 Defence-in-Depth also includes 'defence in breadth.'",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The slides mention Defence-in-Depth includes placing defences at each stage, avoiding single points of failure, 'And defence in breadth!'"
                },
                {
                    "num": 28,
                    "question": "Users may misunderstand both threats and defences according to the slides.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - The slides list that users 'Misunderstand threats' and 'Misunderstand defences' in the Users vs Attackers comparison."
                },
                {
                    "num": 29,
                    "question": "Signal collects more data linked to user identity than WhatsApp according to the comparison shown.",
                    "answer": "F",
                    "points": 1,
                    "explanation": "FALSE - The comparison shows Signal collects minimal data (Contact Info not linked to identity), while WhatsApp collects extensive data linked to identity."
                },
                {
                    "num": 30,
                    "question": "The accuracy of users' privacy calculus analysis is questioned in the slides.",
                    "answer": "T",
                    "points": 1,
                    "explanation": "TRUE - After describing Privacy Calculus, the slide asks 'But is this analysis accurate?' - questioning whether users make accurate privacy trade-off decisions."
                }
            ]
        },

        "section3": {
            "title": "Section 3: Scenario-Based Questions (3 points each)",
            "questions": [
                {
                    "num": 31,
                    "question": "A company implements a new security policy requiring 20-character passwords with special characters, numbers, and case changes, plus mandatory changes every 30 days. Employees start writing passwords on sticky notes. Which security principle does this scenario violate?",
                    "options": {
                        "A": "Defence-in-Depth - because there aren't enough security layers",
                        "B": "Least Surprise and User Buy-in - because the policy doesn't align with user mental models and doesn't encourage secure behavior",
                        "C": "Privacy Calculus - because users aren't weighing their options",
                        "D": "Privacy Paradox - because users claim to care about security"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This violates P10 Least Surprise (the complex requirements don't align with how users think about passwords) and P11 User Buy-in (users circumvent security rather than embracing it). The design doesn't encourage users to behave securely - it drives them to insecure workarounds."
                },
                {
                    "num": 32,
                    "question": "Sarah tells her friends she's very concerned about online privacy and refuses to use social media. However, she downloads every free app that asks for location access, contacts, and camera permissions to get discount coupons. This is an example of:",
                    "options": {
                        "A": "Privacy Calculus - she's making informed trade-offs",
                        "B": "Defence-in-Depth - she's using multiple security approaches",
                        "C": "Privacy Paradox - her stated privacy concerns don't match her behaviors",
                        "D": "Unmotivated User Property - she doesn't care about security"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "This is the Privacy Paradox: Sarah's stated preferences (very concerned about privacy) do not match her behaviors (giving extensive permissions for small rewards like discount coupons)."
                },
                {
                    "num": 33,
                    "question": "A bank requires customers to click through 5 security warnings before completing any online transaction. Over time, customers click through without reading them. This illustrates:",
                    "options": {
                        "A": "Effective Defence-in-Depth implementation",
                        "B": "The Lack of Feedback Property and why good feedback is complicated",
                        "C": "Successful User Buy-in",
                        "D": "The Privacy Calculus working correctly"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This illustrates the Lack of Feedback Property - excessive warnings become noise, and users habituate to clicking through them. Good feedback is complicated; too much feedback is as problematic as too little."
                },
                {
                    "num": 34,
                    "question": "An IT department creates a sophisticated encryption system that requires users to manage their own encryption keys, understand certificate chains, and manually verify signatures. The system is technically secure but rarely used correctly. Which property is most relevant here?",
                    "options": {
                        "A": "The system successfully implements Defence-in-Depth",
                        "B": "P10 Least Surprise is violated - designs suited for trained experts are unintuitive for typical end users",
                        "C": "The Privacy Paradox explains user behavior",
                        "D": "Users are demonstrating good Privacy Calculus"
                    },
                    "answer": "B",
                    "points": 3,
                    "explanation": "This violates P10 Least Surprise. The design is suited for trained experts but is unintuitive and triggers mistakes by typical end users. The design should be tailored to the experience of target users."
                },
                {
                    "num": 35,
                    "question": "A company's security team notices that their firewall, antivirus, intrusion detection, access controls, and encryption all failed to stop an attack because they all relied on the same authentication database that was compromised. This represents a failure of:",
                    "options": {
                        "A": "Privacy Paradox",
                        "B": "User Buy-in",
                        "C": "Defence-in-Depth - specifically the principle of avoiding single points of failure",
                        "D": "Least Surprise"
                    },
                    "answer": "C",
                    "points": 3,
                    "explanation": "This is a failure of Defence-in-Depth. While multiple security mechanisms were in place, they all had a single point of failure (the authentication database). P13 emphasizes avoiding single points of failure."
                }
            ]
        },

        "section4": {
            "title": "Section 4: Short Answer (2 points each)",
            "questions": [
                {
                    "num": 36,
                    "question": "What is the name of the principle (P10) that emphasizes aligning designs with users' mental models?",
                    "answer": ["least surprise", "principle of least surprise", "p10"],
                    "points": 2,
                    "type": "text",
                    "explanation": "P10 Least Surprise emphasizes aligning designs with users' mental models and tailoring to the experience of target users."
                },
                {
                    "num": 37,
                    "question": "What is the name of the principle (P11) about designing systems that encourage users to behave securely?",
                    "answer": ["user buy-in", "user-buy-in", "buy-in", "p11"],
                    "points": 2,
                    "type": "text",
                    "explanation": "P11 User Buy-in focuses on designing systems that encourage users to behave securely."
                },
                {
                    "num": 38,
                    "question": "What is the name of the principle (P13) about placing defences at each stage and avoiding single points of failure?",
                    "answer": ["defence-in-depth", "defense-in-depth", "defence in depth", "defense in depth", "p13"],
                    "points": 2,
                    "type": "text",
                    "explanation": "P13 Defence-in-Depth recommends placing a defence mechanism at each stage where one can be placed and avoiding single points of failure."
                },
                {
                    "num": 39,
                    "question": "What term describes when users' stated privacy preferences do not match their actual behaviors?",
                    "answer": ["privacy paradox", "paradox"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The Privacy Paradox describes the disconnect where users' stated preferences and attitudes toward privacy do not match their behaviors."
                },
                {
                    "num": 40,
                    "question": "What term describes privacy as a trade-off where individuals weigh expected loss against potential gain?",
                    "answer": ["privacy calculus", "calculus"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Privacy Calculus views privacy as a trade-off where individuals weigh the expected loss of privacy against the potential gain of disclosure."
                },
                {
                    "num": 41,
                    "question": "Name TWO characteristics of attackers mentioned in the Users vs Attackers comparison (separate with comma):",
                    "answer": ["security-focused", "intelligent", "adaptable", "well-educated", "well-equipped", "well-motivated", "educated", "equipped", "motivated"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Attackers are described as: security-focused, intelligent, adaptable, well-educated, well-equipped, and well-motivated."
                },
                {
                    "num": 42,
                    "question": "Name TWO characteristics of users mentioned in the Users vs Attackers comparison (separate with comma):",
                    "answer": ["primary task", "secondary task", "not vigilant", "misunderstand threats", "misunderstand defences", "misunderstand", "vigilant"],
                    "points": 2,
                    "type": "multi_text",
                    "explanation": "Users are characterized as: focusing on primary task, treating security as secondary task, not vigilant, misunderstanding threats, and misunderstanding defences."
                },
                {
                    "num": 43,
                    "question": "According to the slides, what is NOT the 'magic solution' to security problems with users?",
                    "answer": ["education", "training", "user education"],
                    "points": 2,
                    "type": "text",
                    "explanation": "The slides state 'Education is not the magic solution!' under the Unmotivated User Property."
                },
                {
                    "num": 44,
                    "question": "What type of task is security considered to be for typical users?",
                    "answer": ["secondary", "secondary task"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Security is a secondary task for users - they focus on their primary task while security takes a back seat."
                },
                {
                    "num": 45,
                    "question": "According to Alan F. Westin, privacy issues are fundamentally matters of values, interests and what?",
                    "answer": ["power"],
                    "points": 2,
                    "type": "text",
                    "explanation": "Alan F. Westin stated that 'privacy issues are fundamentally matters of values, interests and power.'"
                }
            ]
        }
    }