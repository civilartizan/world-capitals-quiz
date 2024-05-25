import random
import os

# The quiz data. Keys are states and values are their capitals.

capitals = {
    'China': 'Beijing',
    'India': 'New Delhi',
    'United States': 'Washington, D.C.',
    'Indonesia': 'Jakarta',
    'Pakistan': 'Islamabad',
    'Brazil': 'Brasília',
    'Nigeria': 'Abuja',
    'Bangladesh': 'Dhaka',
    'Russia': 'Moscow',
    'Mexico': 'Mexico City',
    'Japan': 'Tokyo',
    'Ethiopia': 'Addis Ababa',
    'Philippines': 'Manila',
    'Egypt': 'Cairo',
    'Vietnam': 'Hanoi',
    'DR Congo': 'Kinshasa',
    'Turkiye': 'Ankara',
    'Iran': 'Tehran',
    'Germany': 'Berlin',
    'Thailand': 'Bangkok',
    'United Kingdom': 'London',
    'France': 'Paris',
    'Italy': 'Rome',
    'Tanzania': 'Dodoma',
    'South Africa': 'Pretoria',
    'Myanmar': 'Naypyidaw',
    'South Korea': 'Seoul',
    'Colombia': 'Bogotá',
    'Kenya': 'Nairobi',
    'Spain': 'Madrid',
    'Argentina': 'Buenos Aires',
    'Sudan': 'Khartoum',
    'Ukraine': 'Kyiv',
    'Uganda': 'Kampala',
    'Iraq': 'Baghdad',
    'Poland': 'Warsaw',
    'Canada': 'Ottawa',
    'Morocco': 'Rabat',
    'Uzbekistan': 'Tashkent',
    'Saudi Arabia': 'Riyadh',
    'Malaysia': 'Kuala Lumpur',
    'Afghanistan': 'Kabul',
    'Venezuela': 'Caracas',
    'Peru': 'Lima',
    'Angola': 'Luanda',
    'Ghana': 'Accra',
    'Mozambique': 'Maputo',
    'Yemen': 'Sanaa',
    'Nepal': 'Kathmandu',
    'Madagascar': 'Antananarivo'
}

# Create the "quizzes-and-answers" directory if it doesn't exist
os.makedirs('quizzes-and-answers', exist_ok=True)

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open(os.path.join('quizzes-and-answers', 'capitalsquiz%s.txt' % (quizNum + 1)), 'w')
    answerKeyFile = open(os.path.join('quizzes-and-answers', 'capitalsquiz_answers%s.txt' % (quizNum + 1)), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerKeyFile.close()
