from tkinter import Tk,Canvas,Button,Label,PhotoImage
import requests
import time
import html
incorrect_li = []
question_li = {}
THEME_COLOR = "#375362"
SCORE = 0


def get_question():
    global question_li
    response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
    response.raise_for_status()
    data = response.json()
    data = data["results"]
    ques = data[0]["question"]
    correct_ans = data[0]["correct_answer"]
    incorrect_ans = data[0]["incorrect_answers"]
    incorrect_ans = "".join(str(e) for e in incorrect_ans)
    question = html.unescape(ques)
    question_li = {
        "question":question,
        "correct answer":correct_ans,
        "incorrect answer":incorrect_ans
    }
    return question_li


def wrong_button():
    global SCORE
    corr = question_li["correct answer"]
    if corr == "False":
        canvas.itemconfig(rect, fill="green")
        root.update()
        SCORE += 1
        time.sleep(1)
        score_label.config(text=f"Score: {SCORE}")
        canvas.itemconfig(txt, text=get_question()["question"])
        root.update()
        canvas.itemconfig(rect, fill="white")
        root.update()
    else:
        canvas.itemconfig(rect, fill="red")
        incorrect_li.append(question_li)
        root.update()
        time.sleep(1)
        canvas.itemconfig(txt, text=get_question()["question"])
        root.update()
        canvas.itemconfig(rect, fill="white")
        root.update()


def right_button():
    global SCORE
    corr = question_li["correct answer"]
    if corr == "True":
        canvas.itemconfig(rect, fill="green")
        root.update()
        SCORE += 1
        time.sleep(1)
        score_label.config(text=f"Score: {SCORE}")
        canvas.itemconfig(txt, text=get_question()["question"])
        root.update()
        canvas.itemconfig(rect, fill="white")
        root.update()
    else:
        canvas.itemconfig(rect, fill="red")
        incorrect_li.append(question_li)
        root.update()
        time.sleep(1)
        canvas.itemconfig(txt, text=get_question()["question"])
        root.update()
        canvas.itemconfig(rect, fill="white")
        root.update()


root = Tk()
root.title("Achintya's Quiz")
root.config(background=THEME_COLOR, padx=20,pady=20)
q = get_question()
score_label = Label(root,text="Score: 0", font=("Ariel", 20, "bold"), background=THEME_COLOR, foreground="white")
score_label.grid(row=0, column=1)
canvas = Canvas(root, width=550, height=550, background=THEME_COLOR, highlightthickness=0)
rect = canvas.create_rectangle(50, 50, 450, 400 ,fill="white")
txt = canvas.create_text(250, 180, text=q["question"], fill="black", font=("Ariel", 20, "bold"), width=350)
canvas.grid(row=1, column=0,columnspan=2)
true_img = PhotoImage(file="images/true.png")
true_button = Button(image=true_img, width=200, height=100, background=THEME_COLOR, border=0, command=right_button)
true_button.grid(row=2,column=0)
false_img = PhotoImage(file="images/false.png")
false_button = Button(image=false_img, width=200, height=100, background=THEME_COLOR, border=0, command=wrong_button)
false_button.grid(row=2,column=1)
root.mainloop()

with open("incorrect.txt",mode="w") as file:
    for i in incorrect_li:
        file.write(f"{i}\n")
