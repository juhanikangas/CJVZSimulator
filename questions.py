import random
import time
from select_menu import select_menu

questions = [
    {"question": "Is the Boeing 747 often referred to as the 'Queen of the Skies'?", "answers": ["Yes", "No"], "difficulty": "1"},
    {"question": "Does the Concorde hold the record for the fastest commercial airliner?", "answers": ["Yes", "No"], "difficulty": "1"},
    {"question": "Was the Lockheed SR-71 'Blackbird' primarily used for cargo transport purposes?", "answers": ["No", "Yes"], "difficulty": "1"},
    {"question": "Is the Cessna 172 'Skyhawk' typically used for military combat missions?", "answers": ["No", "Yes"], "difficulty": "1"},
    {"question": "What is the purpose of the 'black box' in an airplane?", "answers": ["It's used to record flight data and cockpit conversations for accident investigation and improving aviation safety.", "It's a top-secret compartment where airlines store their stash of in-flight peanuts and pretzels, ensuring they remain fresh for passengers.", "It contains a backup power source that can keep the plane flying for an additional hour in case of engine failure.", "It's a secure communication device used by the crew to relay information to air traffic control in case of a radio malfunction."], "difficulty": "3"},
    {"question": "What is the largest passenger airplane in the world?", "answers": ["Airbus 380", "Boeing 787 Supersized", "Lockheed Galaxy Express", "Douglas DC-10"], "difficulty": "3"},
    {"question": "Which aircraft is commonly used for airborne refueling of other aircraft and is known for its long, slender boom?", "answers": ["KC-135 Stratotanker", "Boeing B-52 Stratofortress", "Airbus A330 MRTT", "Lockheed C-130 Hercules"], "difficulty": "3"},
    {"question": "Which country's national flag carrier airline is known as 'Lufthansa'?", "answers": ["Germany", "France", "Netherlands", "Turkey"], "difficulty": "3"},
    {"question": "In aviation, what does 'ATC' stand for?", "answers": ["Air Traffic Control", "Aircraft Tracking Center", "Aviation Test Crew"], "difficulty": "2"},
    {"question": "In aviation, what does 'FAA' stand for?", "answers": ["Federal Aviation Administration", "Frequent Airline Adjustments", "Flying Advancement Association"], "difficulty": "2"},
    {"question": "Which U.S. airline's slogan is 'The Friendly Skies'?", "answers": ["United Airlines", "American Airlines", "Delta Airlines"], "difficulty": "2"},
    {"question": "What is the world's longest commercial non-stop flight route?", "answers": ["Singapore to New York", "London to Perth", "Auckland to Dubai"], "difficulty": "2"},
    {"question": "Which airport has the IATA code 'LHR,'", "answers": ["London Heathrow", "Lhasa Internation Airport", "Loch Ness Highlands Regional Airport", "Lahore Internation Airport"], "difficulty": "3"},
    {"question": "Do all airports have customs and immigration facilities for international flights?", "answers": ["No", "Yes"], "difficulty": "1"},
    {"question": "Are airplanes allowed to fly directly over the North Pole region on their routes?", "answers": ["Yes", "No"], "difficulty": "1"},
    {"question": "Is it possible for passengers to open the emergency exit doors of an airplane during flight?", "answers": ["No", "Yes"], "difficulty": "1"},
    {"question": "Are birds typically more problematic for airplane safety during the day compared to nighttime?", "answers": ["No", "Yes"], "difficulty": "1"},
    {"question": "Who is credited with inventing the first successful powered airplane, and in what year did this historic flight take place?", "answers": ["Orville and Wilbur Wright 1903", "Amelia Aviatoria 1907", "Jacob Veldhuyzen van Zanten 1911", "Charles Lindbergh 1909"], "difficulty": "3"},
    {"question": "What is the term for the area of an airport where aircraft are parked, loaded, and unloaded, and where passengers board and disembark?", "answers": ["Apron", "Flight Zone", "Aeroport", "Aircraft Alighting Area"], "difficulty": "3"},
    {"question": "Which iconic aircraft, often used for U.S. presidential travel, is known as 'Air Force One' when the President is on board?", "answers": ["Boeing 747", "Airbus 340", "Embraer EMB-135"], "difficulty": "2"}
]

def question(question_index):
    question = questions[question_index]
    answers = question["answers"].copy()
    correct_answer = answers[0]
    if "Yes" in answers:  # If the questions is not yes/no shuffle the answers
        answers = ["Yes", "No"]
    else:
        random.shuffle(answers)
    user_answer = select_menu(answers, question["question"])

    if user_answer == correct_answer:
        return True
    else:
        return False


def main():
    question_numbers = [i for i in range(5)]
    points = 0
    while question_numbers:
        random_index = random.randint(0, len(question_numbers) - 1)
        answer_correct = question(question_numbers[random_index])
        question_numbers.pop(random_index)
        if answer_correct:
            points += 1
    print(points)
    time.sleep(5)


main()
