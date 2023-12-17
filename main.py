from game_data import data
import random
from art import logo, vs
import os
from tkinter import ttk
from tkinter import *

def close_win():
   game_window.destroy()
def disable_event():
   pass

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def show_correct_popup():
    correct_popup = Toplevel(game_window)
    correct_popup.title("Correct!")
    Label(correct_popup, text=f"Correct! Current score: {score}.").pack()
    correct_popup.after(1500, correct_popup.destroy)  # Close the popup after 1500 milliseconds (1.5 seconds)

def show_wrong_popup():
    wrong_popup = Toplevel(game_window)
    wrong_popup.title("Wrong!")
    Label(wrong_popup, text=f"Wrong one. Final score: {score}").pack()
    wrong_popup.after(1500, game_window.destroy)  # Close the main window after 1500 milliseconds (1.5 seconds)

def on_submit():
    guess = user_input.get().lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        global score
        score += 1
        score_label.config(text=f"Current score: {score}.")
        show_correct_popup()
    else:
        show_wrong_popup()

def next_round():
    global account_a, account_b
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()

    compare_label.config(text=f"Compare\n \nA: {format_data(account_a)}.\nAgainst\n\nB: {format_data(account_b)}")

score = 0
account_a = get_random_account()
account_b = get_random_account()

game_window = Tk()
game_window.title("Higher Lower Game")

vs_label = Label(game_window, text=logo)
vs_label.pack()

btn_close = ttk.Button(game_window, text ="Close Game",command=close_win)

compare_label = Label(game_window, text=f"Compare\n\nA: {format_data(account_a)}.\n\nAgainst\n\n B: {format_data(account_b)}")
compare_label.pack()

vs_label = Label(game_window, text=vs)
vs_label.pack()

user_input = Entry(game_window)
user_input.pack()

score_label = Label(game_window, text=f"Current score: {score}.")
score_label.pack()

submit_button = Button(game_window, text="Submit", command=on_submit)
submit_button.pack()

next_round_button = Button(game_window, text="Reroll question", command=next_round)
next_round_button.pack()

btn_close.pack()
game_window.protocol("WM_DELETE_WINDOW", disable_event)
game_window.mainloop()
