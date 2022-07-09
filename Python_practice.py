#print("Hello World")
#num_candidates = 3
# print(num_candidates)
"""
#num_candidate = 5
counties = ["Arapahoe", "Alameda", "Jefferson"]
# print(counties[i])

for county in counties:
    print(county)

for num in range(15):
    print(num)
for i in range(len(counties)):
    print(counties[i])
"""
"""    
if "Denver" not in counties:
    print(counties[1])
else:
    print(counties[0])
"""

"""
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.") 

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
"""
"""
x = 0
while x <= 5:
    print(x)
    x = x + 1
"""

""" counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# print(counties_dict['Denver']) """

"""
for county in counties_dict:
    #county = "Arapahoe"
    print("County " + county + " has " +
          str(counties_dict[county]) + " votes!")


for falak, hemali in counties_dict.items():
    print(falak, hemali)
"""
"""
voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for dict in voting_data:
    for key, value in dict.items():
        print(key, value)

"""
my_votes = 1000
total_votes = 5000
percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
print(f"I received {round(percentage_votes)}% of the total votes.")

candidate_votes = int(
    input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)
