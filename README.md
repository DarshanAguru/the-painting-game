# The Painting

The Painting is a treasure hunt type game that tests the verbal (or communication) and problem-solving skills of the players.
This game has a small story-like plot that will create a theme in the player's mind thus they will have fun while playing the game.
The project is built using Django Framework(Python) along with some JavaScript used for animations and timers. No Bootstrap css is used. All the codes are written from scratch, although some references are taken from some websites for debugging purposes.

Gameplay is very simple, the user has to sign-up and log in after which the game and scoring process will be described. They will then start and the user is expected to give correct answers as scores will be awarded as per the scoring criteria.
After the game is over the user will be prompted with the final score he has achieved.

There is an admin panel where the leader board and user data insights are also displayed. The leaderboard is kept in descending order of score and also has a user insights page where graphs are plotted to show the user performance along with an analysis table for each question attempted.



## Skills Assessed

Through this game, the verbal or communicational and reasoning or problem-solving skills of the users are assessed, and at the last question, the memory and alertness of the user are also assessed. Thus this game assesses the soft skills of the user and helps them to improve their skills.
The reasoning questions are framed such that there can be more than one correct answer for the question based on the logic applied. But the user has to guess the correct logic that will make him enter the correct path.
There are dead-ends in the project which will arise when users fail to get the correct logic required for solving the question.


## 🆕 Features

- The admin panel has a leaderboard sorted in descending order of the scores.
- Each user row of the leaderboard table has a view button to view the data insights.
- The user data insights has a table that has records for the time and score of each question that the user has attempted.
- The user data insights also has two graphs plotted, one shows the question and score for each question (line plot) and the other is the pie chart that shows what part of communication skills and problem-solving skills account for the total score.

## Scoring

The scoring logic is very subtle, It is based on the time user takes to solve the question. There is no negative scoring for the wrong answer, scoring is based on the time taken.
it is based on a simple formula:
```
    time = Math.floor(time/60)+1     //time is in seconds
    score = Math.ceil(score / time)  //ceiling the answer
```
Thus after every minute, the score will be reduced to some fraction, which is then ceiled to get the integer value.
Also, there is a threshold for scoring:
```
    if score < 5:
        score = 5
```
That maintains the threshold of score to 5 (i.e., the minimum score is 5)


## Possible ways To solve the puzzle

The First way is the simple way where the user is expected to give correct answers to all the questions and win the puzzle.

The second way is where the user gets trapped in the first trap and reaches a dead end. The first trap is set in 5th question

The third way is where the user gets trapped in the second trap and reached a dead end. The second trap is set in the 6th question.

The last way is when the user solves all the questions and in the last question, he is asked to choose the original painting. The hint for finding the original painting was already mentioned in the prompt of the 6th question. The user who forgot will again end into a dead end and has to restart the game.

The possible answers to the questions asked in the puzzle are:
```
Q1.  
Ans: fire

Q2.
Ans: 1845

Q3.
Ans: personification

Q4.
Ans: jbk

Q5.(dead end bridge question)
Ans: large (correct)
Ans: few (leads to dead end)

Q6.(dead end bridge question)
Ans: 36 (correct)
Ans: 31 (leads to dead end)

Q7.
Ans: tarry

Q8.
Ans: 3.2

Q9. (dead end)
Ans: past

Q10.(dead end)
Ans: 56

Q. Last Puzzle where the user has to choose the original painting.
Ans: The painting with a golden frame is the original one. 
``` 

## 💻 Technologies used
This project is made from scratch and no templates were used. This uses the Django framework which is one of the best-suited frameworks for these kinds of projects. Some javascript is also used for some functionalities to work such as timer and all.
It uses the MVT architecture and thus the models.py of the repository has the database model that is used.\
There are 3 tables used for this project:\
 - Clues: stores all the questions answers and the score for each.\
 - Users: Stores the user details.\
 - ScoreAndTime: Stores the score and time of each question attempted by the user.\
The code is not much complicated and is easy to understand. The dead-ends are also linearly arranged and simple logic is applied for that.
## Tables used 

#### Users

| ATTRIBUTE | DATATYPE | INDEX   | DESCRIPTION|
| :-------- | :------- | :-------- | :-------------|
| `useremail` | `varchar(256)` | `primary key` | `stores user email`|
| `username` | `varchar(256)` | | `user name`|
| `userpass` | `varchar(256)` | | `stores user pass (using SHA256)`|
| `totalscore` | `varchar(256)` | `null = true` | `stores score`|
| `totaltime` | `varchar(256)` | `null = true` | `stores time in format 00:00`|

#### ScoreAndTime

| ATTRIBUTE | DATATYPE | INDEX   | DESCRIPTION|
| :-------- | :------- | :-------- | :-------------|
| `useremail` | `varchar(256)` | `primary key` | `stores user email`|
| `cl1scr` | `integer` | `dafault = 0` | `score for first question`|
| `cl1tym` | `varchar(10)` | `null = true` | `times taken to solve first question`|
| `cl2scr` | `integer` | `dafault = 0` | `score for second question`|
| `cl2tym` | `varchar(10)` | `null = true` | `times taken to solve second question`|
| `cl3scr` | `integer` | `dafault = 0` | `score for third question`|
| `cl3tym` | `varchar(10)` | `null = true` | `times taken to solve third question`|
| `cl4scr` | `integer` | `dafault = 0` | `score for fourth question`|
| `cl4tym` | `varchar(10)` | `null = true` | `times taken to solve fourth question`|
| `cl5scr` | `integer` | `dafault = 0` | `score for fifth question`|
| `cl5tym` | `varchar(10)` | `null = true` | `times taken to solve fifth question`|
| `cl6scr` | `integer` | `dafault = 0` | `score for sixth question`|
| `cl6tym` | `varchar(10)` | `null = true` | `times taken to solve sixth question`|
| `cl7scr` | `integer` | `dafault = 0` | `score for seventh question`|
| `cl7tym` | `varchar(10)` | `null = true` | `times taken to solve seventh question`|
| `cl8scr` | `integer` | `dafault = 0` | `score for eighth question`|
| `cl8tym` | `varchar(10)` | `null = true` | `times taken to solve eighth question`|


#### Clues

| ATTRIBUTE | DATATYPE | INDEX   | DESCRIPTION|
| :-------- | :------- | :-------- | :-------------|
| `clueid` | `varchar(20)` | `primary key` | `acts as question number`|
| `clue` | `text` |  | `Question`|
| `score` | `integer` |  | `score assigned for question`|
| `answer` | `text` | | `answer of the question`|





## Installation
Windows \
It is required to have Python installed in the system.\
It is necessary to check if your requirements are already installed, please refer requirements.txt file in the repository.\
you can install the dependencies as follows:
```
    >  pip install -r requirements.txt
```

For installation, It is recommended to create a virtual environment.
You can use the following command for creating a virtual environment:
```cmd
    > python -m venv {name}
``` 
now you can paste the files in this virtual environment, and then 
once you are ready you can activate the virtual environment as:

```cmd
    > {name}\scripts\activate  
```
Now enter into the directory (where you copied the repo.)
```cmd
    > cd {folder name}
```
Now you can run the server with the following command:
```cmd
    > python manage.py runserver
```
You will get the URL and the browser will be started automatically and the puzzle (website) will be hosted on your local server.

## 🚀 About Me

I'm a programming enthusiast, always curious to learn new things and try new technologies.. My interests are in full stack Dev and defensive security. 

## 🛠 Skills

- Programming Languages: Python, Java, C++
- Frameworks: Django, React
- Web Technologies: HTML, CSS, JS
- Databases: MySQL, Oracle
- Soft skills: Healthy communication, Smart Worker, quick learner, problem solver
- OS: Windows, Linux, Mac

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/this-darshiii/)
