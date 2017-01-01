"""
Flash Cards Introduction
------------------------
A simple flash card program that takes an input yaml file structured as
follows and asks questions until all questions are completed to satisfaction

The program expects to be executed from the command line, e.g.

    python flash_cards.py questions.yaml

The expected yaml format is as follows:

    topic:
        q: question text
        a: answer text
"""


from __future__ import print_function
import os
import sys
import yaml

def read_yaml_file(filename):
    with open(filename,'r') as f:
        yaml_data = f.read()
    return yaml.load(yaml_data)

def prompt_user(input_statement):
    'selects the appropriate way to prompt the user based on python version'
    if sys.version_info > (3,0):
        _ = input(input_statement)
        return _
    else:
        _ = raw_input(input_statement)
        return _

def ask_questions(all_topics):
    """this will ask the user the questions on the flash cards
       then show the appropriate answer. If a question is marked as
       'correct' it will not be asked again, otherwise it will remain
       in the list of questions to ask.

       all_topics expects a list of keys related to all flash_card questions
    """
    num_asked = 0
    num_correct = 0

    # we use the while loop to revisit questions marked incorrect
    while len(all_topics) > 0:
        for topic in tuple(all_topics):

            # clear screen & ask question
            os.system('clear')
            print('\n'*3,data[topic]['q'])
            prompt_user('\n\n...press any key to see the answer ')


            # show the answer
            print('\n'*3,data[topic]['a'])
            status = prompt_user('\n\nDid you answer correctly? Press "y" or "n"\n').strip().lower()
            # status = str(input('\n\nDid you answer correctly? Press "y" or "n"\n')).strip().lower()

            # ask if the question should be asked again
            if status == "y":
                all_topics.remove(topic)
                num_correct += 1

            num_asked += 1

        # count the questions asked and correct answers
        status = '{0} questions asked, {1} answered correctly'.format(num_asked,num_correct)

        # if all answers are marked correct stop asking questions
        # give the user a change to stop after all questions asked
        os.system('clear')
        if len(all_topics) == 0:
            print("All questions have been asked and answered correctly.")
            print(status)
            return
        else:
            print('\n\n\nAll questions have been asked at least once.')
            kill = prompt_user('\nWould you like to stop now? Press "y" or "n"\n').strip().lower()
            # kill = str(input('Would you like to stop now? Press "y" or "n"\n')).strip().lower()
            if kill == "y":
                print(status)
                return


if __name__ == '__main__':
    # read in the questions from a yaml file and ask questions
    filename_ = sys.argv[1]
    data = read_yaml_file(filename_)
    ask_questions(list(data.keys()))
