import time
import keyboard
from random import randint


def roll_d20():
    x = randint(1, 20)
    if x == 20:
        return 1
    else:
        return 0


def nope():
    denial_messages = [
        "Not in the mood...",
        "I don't think so",
        "Stop telling me what to do",
        "I not listening... LALALALALA",
        "Nope, not happening",
        "Sorry, not interested",
        "Not today, thanks",
        "I'll pass on that",
        "Maybe another time",
        "I'd rather not",
        "Let's not and say we did",
        "Not feeling it",
        "I'm good, thanks",
        "That's a hard no from me",
        "I respectfully decline",
        "I'd prefer not to",
        "I'll take a rain check",
        "I'll have to think about it",
        "I'm not up for it",
        "I'll have to pass",
        "Not my cup of tea",
        "Not gonna happen",
        "I'm allergic to that idea",
        "I'll pass this time",
        "Nope",
        "Nah",
        "No",
        "Maybe some other time",
        "Meh",
        "I'm not really feeling it right now",
        "I'm afraid that's not possible",
        "I don't see that happening",
        "I'm not up for that",
        "I'm not in the mood for that",
        "I'm not really into it",
        "I think I'll sit this one out",
        "I'll have to respectfully decline",
        "I'm not up to it at the moment",
        "I'm not keen on that idea",
        "I don't feel like it",
        "That's a negative",
        "I'll have to pass on that one",
        "I'm not up for that right now",
        "I'm not feeling very enthusiastic about that",
        "I'd rather not if that's okay",
        "I'm going to have to say no to that",
        "I'll have to give that a miss",
        "I'm not really up for it",
        "I'm not really into that sort of thing",
        "I'm not really up for that right now",
        "I'm going to have to decline",
        "That's not really my thing",
        "I'm not really feeling up to it",
        "I'm not really feeling that",
        "I'm going to have to pass on that one",
        "I'm going to have to say no to that idea",
        "That's not really what I had in mind",
        "I don't think that's for me",
        "I'm not really interested in that",
        "I'm going to have to give that one a miss",
        "I don't think I'll be able to make it",
        "I don't really feel like doing that",
        "I don't think I'm up for that",
        "I don't think I'll be able to do that",
        "I don't think that's a good idea for me",
        "I'm not really feeling up to that",
        "I don't really feel like it today",
        "I don't think that's something I can do",
        "I don't think I'll be able to go along with that",
        "I don't really feel like it right now",
        "I'm not really feeling up to that right now",
        "I'm not really feeling up to that idea",
        "I don't think I'll be able to do that right now",
        "I don't think that's something I can do right now",
        "I don't think I'm in the mood for that right now",
        "I don't think that's something I can commit to right now",
        "I'm not really feeling up to that at the moment",
        "I don't think I'll be able to go along with that right now",
        "I don't think that's something I can commit to at the moment"
    ]
    print(f'\n> {denial_messages[randint(0, 77)]}')


def yep():
    acceptance_messages = [
        "Fine, whatever",
        "Okay, but I'm NOT happy about it",
        "Alright, but I WILL NOT enjoy it",
        "Fine, have it your way",
        "OK, YOU'VE WON, STOP PRESSING IT",
        "I guess so, but I'm NOT thrilled",
        "Sure, but I WILL NOT like it",
        "Alright, if I have to",
        "Okay, but DO NOT expect me to be happy",
        "Fine, I give in"
    ]
    print(f'\n> {acceptance_messages[randint(0, 8)]}')


def exit_on_esc():
    print("Press ESC to exit.")
    while True:
        keyboard.wait('esc')
        answer = roll_d20()
        if answer == 0:
            nope()
        else:
            yep()
            time.sleep(3)
            print(f'\nTHE SYSTEM IS SHUTTING DOWN', end='', flush=True)
            for i in range(1, randint(5, 60)):
                print('.', end='', flush=True)
                time.sleep(1)
            print(f'\n\n> Still there?')
            keyboard.wait('esc')
            print('\n> Fuck.')
            break


exit_on_esc()
