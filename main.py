import time
import os

# Import chapter question modules
from chapter1_questions import get_chapter_1_questions
from chapter2_questions import get_chapter_2_questions
from chapter3_questions import get_chapter_3_questions
from chapter4_questions import get_chapter_4_questions
from chapter5_questions import get_chapter_5_questions
from chapter6_questions import get_chapter_6_questions
from chapter7_questions import get_chapter_7_questions
from chapter8_questions import get_chapter_8_questions
from chapter9_questions import get_chapter_9_questions

# ============================================================================
# CHAPTER CONFIGURATION
# ============================================================================
# To add a new chapter:
# 1. Create a new chapterX_questions.py file with get_chapter_X_questions() function
# 2. Import it above
# 3. Add an entry to the CHAPTERS dictionary below
# ============================================================================
CHAPTERS = {
    1: {
        'number': 1,
        'title': 'Chapter 1',
        'function': get_chapter_1_questions
    },
    2: {
        'number': 2,
        'title': 'Chapter 2',
        'function': get_chapter_2_questions
    },
    3: {
        'number': 3,
        'title': 'Chapter 3',
        'function': get_chapter_3_questions
    },
    4: {
        'number': 4,
        'title': 'Chapter 4',
        'function': get_chapter_4_questions
    },
    5: {
        'number': 5,
        'title': 'Chapter 5',
        'function': get_chapter_5_questions
    },
    6: {
        'number': 6,
        'title': 'Chapter 6',
        'function': get_chapter_6_questions
    },
    7: {
        'number': 7,
        'title': 'Chapter 7',
        'function': get_chapter_7_questions
    },
    8: {
        'number': 8,
        'title': 'Chapter 8',
        'function': get_chapter_8_questions
    },
    9: {
        'number': 9,
        'title': 'Chapter 9',
        'function': get_chapter_9_questions
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(chapter_selection):
    print("=" * 80)
    print("SYSC 4810: Introduction to Network and Software Security")

    if chapter_selection == "0":
        # All chapters
        chapter_titles = " & ".join([str(ch) for ch in sorted(CHAPTERS.keys())])
        print(f"Chapters {chapter_titles} Combined Quiz - Fall 2024")
    else:
        # Single chapter
        chapter_num = int(chapter_selection)
        if chapter_num in CHAPTERS:
            print(f"{CHAPTERS[chapter_num]['title']} Quiz - Fall 2024")

    print("=" * 80)
    print("Time Limit: 75 Minutes")
    print("Total Points: 100")
    print("=" * 80)
    print()

def countdown_timer(seconds):
    """Display live timer"""
    mins = seconds // 60
    secs = seconds % 60
    print(f"⏰ Time remaining: {mins:02d}:{secs:02d}", end=" | ")

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

def merge_questions(*chapter_question_dicts):
    """Merge questions from multiple chapters dynamically

    Args:
        *chapter_question_dicts: Variable number of chapter question dictionaries

    Returns:
        Merged dictionary with all questions from all chapters
    """
    merged = {}

    # Collect all unique section keys from all chapters
    all_sections = set()
    for chapter_q in chapter_question_dicts:
        all_sections.update(chapter_q.keys())

    # Process each section
    for section in all_sections:
        # Get title from first chapter that has this section
        title = None
        for chapter_q in chapter_question_dicts:
            if section in chapter_q:
                title = chapter_q[section]["title"]
                break

        merged[section] = {
            "title": title,
            "questions": []
        }

        # Add questions from each chapter with appropriate numbering offset
        for chapter_q in chapter_question_dicts:
            if section in chapter_q:
                offset = len(merged[section]["questions"])
                for q in chapter_q[section]["questions"]:
                    q_copy = q.copy()
                    q_copy["num"] = q["num"] + offset
                    merged[section]["questions"].append(q_copy)

    return merged

def select_chapter():
    """Let user select which chapter(s) to be quizzed on"""
    clear_screen()
    print("=" * 80)
    print("SYSC 4810: Quiz Chapter Selection")
    print("=" * 80)
    print("\nWhich chapter(s) would you like to be quizzed on?")

    # Dynamically generate menu from CHAPTERS configuration
    chapter_nums = sorted(CHAPTERS.keys())
    all_chapters_str = ", ".join(str(ch) for ch in chapter_nums[:-1]) + f" & {chapter_nums[-1]}"
    print(f"  0) All Chapters ({all_chapters_str})")

    for chapter_num in chapter_nums:
        print(f"  {chapter_num}) {CHAPTERS[chapter_num]['title']} only")

    print("=" * 80)

    # Generate valid choices
    valid_choices = ['0'] + [str(ch) for ch in chapter_nums]
    choices_display = ", ".join(valid_choices)

    while True:
        choice = input(f"\nEnter your choice ({choices_display}): ").strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter {choices_display}.")

def run_quiz():
    # Chapter selection
    chapter_selection = select_chapter()

    clear_screen()
    display_header(chapter_selection)

    input("Press ENTER to begin the quiz...")
    start_time = time.time()
    time_limit = 75 * 60  #75 minutes in seconds

    # Get questions based on selection - dynamically using CHAPTERS configuration
    if chapter_selection == "0":
        # All chapters - get all chapter questions and merge them
        all_chapter_questions = []
        for chapter_num in sorted(CHAPTERS.keys()):
            chapter_func = CHAPTERS[chapter_num]['function']
            if chapter_func:
                all_chapter_questions.append(chapter_func())
        questions = merge_questions(*all_chapter_questions)
    else:
        # Single chapter
        chapter_num = int(chapter_selection)
        if chapter_num in CHAPTERS and CHAPTERS[chapter_num]['function']:
            questions = CHAPTERS[chapter_num]['function']()
    
    # Store user answers
    user_answers = {}
    score = 0
    total_points = sum(q["points"] for section in questions.values() 
                       for q in section["questions"])
    
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

            # Show live timer before each question
            countdown_timer(int(time_limit - elapsed))
            print(f"Question {q['num']}:")
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
    total_questions = sum(len(section["questions"]) for section in questions.values())
    print(f"\n📊 QUIZ SUMMARY")
    print(f"Total Questions: {total_questions}")
    print(f"Points Earned: {score}/{total_points}")
    print(f"Time Used: {mins}m {secs}s of 30m")
    print("\n" + "=" * 80)



if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("Welcome to SYSC 4810 Quiz System")
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