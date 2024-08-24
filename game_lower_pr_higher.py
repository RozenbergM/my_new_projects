import random
from art import logo, vs
from game_data import data


def score_increase(point):
    """+1 point (If chose the correct answer)"""
    return point + 1


used_data = []
score = 0

# randomly choose "a" object
object_choice = random.choice(data)
used_data.append(object_choice)
a_object_data = f"{object_choice['name']}, a {object_choice['description']}, from {object_choice['country']}"
compare_a = f"Compare A: {a_object_data}"
a_followers = object_choice['follower_count']

print(logo)
print(compare_a)


def game():
    """Main game function"""
    global a_followers
    global score
    global used_data
    global a_object_data
    global object_choice
    print(vs)

    object_choice = random.choice(data)
    while object_choice in used_data:
        object_choice = random.choice(data)

    used_data.append(object_choice)

    b_object_data = (f"{object_choice['name']}, a {object_choice['description']}, "
                     f"from {object_choice['country']}")
    compare_b = f"Compare B: {b_object_data}"

    b_followers = object_choice['follower_count']
    print(compare_b)

    right_answer = max(a_followers, b_followers)
    user_answer = input("\nWho has more followers? Type 'a' or 'b'\n").lower()

    if user_answer == "a":
        user_answer = a_followers
        answer_data = a_object_data
    elif user_answer == "b":
        user_answer = b_followers
        answer_data = b_object_data
    else:
        print(f"Sorry, that's wrong. Game Over. Your score:{score}")
        return

    if user_answer == right_answer:
        score = score_increase(score)

        a_followers = right_answer
        a_object_data = answer_data

        print("\n" * 10)
        print(f"Correct, +1. Your score: {score}\n")
        print(logo)
        print(f"Compare A: {a_object_data}")
        game()
    else:
        print("\n" * 10)
        print(logo)
        print(f"Wrong. Game over. Your score:{score}")
        return


game()
