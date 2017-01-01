# Flash Cards
This is a very simple program to display questions and answers in flash card style format using python. The program expects to be executed from the command line, e.g.

    python flash_cards.py questions.yaml

The expected yaml format is as follows:

    topic:
        q: question text
        a: answer text

The yaml file "questions.yaml" is left as template



_note: the current program is set to display correctly in terminal, I have no idea if it will function as intended on a windows system. (Specifically the os package is using "clear" while windows takes "clc")_
