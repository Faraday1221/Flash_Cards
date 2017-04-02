# Flash Cards
This is a very simple program to display questions and answers in flash card style format using python. The program expects to be executed from the command line, e.g.

    python flash_cards.py questions.yaml

The expected yaml format is as follows, note that the topics should be distinct.

    topic:
        q: question text
        a: answer text

The yaml file "questions.yaml" is left as template.

### Basic Functionality
Other than asking a question and then displaying the answer, the program will keep track of how many questions have been asked and answered correctly. It is up to the individual to decide if the answer was correct, recall "we are all responsible users". Questions marked as incorrect are put back into the question pool and can be revisited.

The program is very simple and performs as follows:
- reads in all questions from the yaml file and shuffles the order
- asks a question
- provides an answer
- asks the user to mark if they feel they have answered satisfactorily
- informs the user when all questions are covered
- allows the user to revisit all questions they marked as 'incorrect'
- provides a summary of questions asked and correct answers


### Simple Demo: 3 questions asked and answered
![Demo gif](https://github.com/Faraday1221/Flash_Cards/blob/master/demo.gif?raw=True)


### Version
This should be compatible with python 2 and 3 and runs just fine on OS X.

_note: the current program is set to display correctly in terminal, I have no idea if it will function as intended on a windows system. (Specifically the os package is using "clear" while windows takes "clc")_
