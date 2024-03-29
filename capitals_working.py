import random
states = [
    {
        "name": "Alabama",
        "capital": "Montgomery",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Alaska",
        "capital": "Juneau",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Arizona",
        "capital": "Phoenix",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Arkansas",
        "capital": "Little Rock",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "California",
        "capital": "Sacramento",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Colorado",
        "capital": "Denver",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Connecticut",
        "capital": "Hartford",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Delaware",
        "capital": "Dover",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Florida",
        "capital": "Tallahassee",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Georgia",
        "capital": "Atlanta",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Hawaii",
        "capital": "Honolulu",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Idaho",
        "capital": "Boise",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Illinois",
        "capital": "Springfield",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Indiana",
        "capital": "Indianapolis",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Iowa",
        "capital": "Des Moines",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Kansas",
        "capital": "Topeka",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Kentucky",
        "capital": "Frankfort",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Louisiana",
        "capital": "Baton Rouge",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Maine",
        "capital": "Augusta",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Maryland",
        "capital": "Annapolis",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Massachusetts",
        "capital": "Boston",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Michigan",
        "capital": "Lansing",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Minnesota",
        "capital": "St. Paul",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Mississippi",
        "capital": "Jackson",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Missouri",
        "capital": "Jefferson City",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Montana",
        "capital": "Helena",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Nebraska",
        "capital": "Lincoln",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Nevada",
        "capital": "Carson City",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "New Hampshire",
        "capital": "Concord",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "New Jersey",
        "capital": "Trenton",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "New Mexico",
        "capital": "Santa Fe",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "New York",
        "capital": "Albany",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "North Carolina",
        "capital": "Raleigh",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "North Dakota",
        "capital": "Bismarck",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Ohio",
        "capital": "Columbus",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Oklahoma",
        "capital": "Oklahoma City",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Oregon",
        "capital": "Salem",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Pennsylvania",
        "capital": "Harrisburg",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Rhode Island",
        "capital": "Providence",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "South Carolina",
        "capital": "Columbia",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "South Dakota",
        "capital": "Pierre",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Tennessee",
        "capital": "Nashville",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Texas",
        "capital": "Austin",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Utah",
        "capital": "Salt Lake City",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Vermont",
        "capital": "Montpelier",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Virginia",
        "capital": "Richmond",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Washington",
        "capital": "Olympia",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "West Virginia",
        "capital": "Charleston",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Wisconsin",
        "capital": "Madison",
        "correct": 0,
        "incorrect": 0
    }, {
        "name": "Wyoming",
        "capital": "Cheyenne",
        "correct": 0,
        "incorrect": 0
    }
]

# We will need to make a loop through the states. 
# We need to tally the scores. 
#Create play again option. 
# add corrrect and incorrect keys for each of the dictionaries
# need a get random feature.
# if counter equals 50 we have code to reset the game.

print('Welcome, do you want to play a game?')
random.shuffle(states) 
print(states[0]["name"])


correct_answer = 0
wrong_answer = 0
index = 0

def wrong_sort(state):
    return state['incorrect']

while index <= len(states):
    if index == len(states):
        ask = input('Continue? Yes/No: ')
        if ask == "Yes":
            correct_answer = 0
            wrong_answer = 0
            index = 0
            random.shuffle(states)
            states.sort(reverse=True, key=wrong_sort)
            print(states)
        else:
            break
    hint = states[index]["capital"]
    print(f'Correct Answer: {correct_answer} | Wrong Answer {wrong_answer}')
    print(f'Guess the capital of this state {states[index]["name"]}')
    print(f'HINT!!! The first three letters are {hint[:3]}')
    user_guess = input('Input the correct capital for the state listed: ')
    if user_guess == states[index]["capital"]:
        print("You got that right!")
        correct_answer += 1
        states[index]["correct"] += 1
    else:
        print("You're an idiot!")
        wrong_answer += 1
        states[index]["incorrect"] += 1
    index += 1
print(f'Correct Answer: {correct_answer} | Wrong Answer {wrong_answer}')


## way to quit
## run the loop again

