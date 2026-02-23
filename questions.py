# Prompts the user for all specified details: title, description, installation, usage, license, author, and contact.
from InquirerPy import prompt
from InquirerPy.prompts.expand import ExpandChoice

def licensing_choices (_):
    return [
            ExpandChoice(key="m", name="MIT", value="MIT"),
            ExpandChoice(key="a", name="Apache2.0", value="Apache2.0"),
            ExpandChoice(key="b", name="BSD", value="BSD"),
            ExpandChoice(key="t", name="The Unlicense", value="The Unlicense"),
        ]
questions = [
    {
        "name":"title", "type": "input", "message": "Please provide the title of your Project", 
        "validate":   lambda results: len(results) > 0,
        "invalid_message": "Your title entry is blank, please give an answer", 
    },

    {
        "name":"description", "type": "input", "message": "Please provide a description of the project", "validate": lambda results: len(results) > 0,
        "invalid_message": "Your description entry is blank, please give an answer",
    },

    {
        "name":"installation", "type": "input", "message": "What steps were taken to make this software runnable?",
        "validate": lambda results: len(results) > 0,
        "invalid_message": "Your installation entry is blank, please give an answer",
    },

    {
        "name":"usage", "type": "input", "message": "How is this program designed to be used?",
        "validate": lambda results: len(results) > 0,
        "invalid_message": "Your usage entry is blank, please give an answer",
    },

    {
        "name":"license", "type": "expand", "choices": licensing_choices, "message": "What licensing do you have?",   
    },

    {
        "name":"author", "type": "input", "message": "Please provide name/s of author" 
    },

    {
        "name":"contact", "type": "input", "message": "Please give details of how to contact yourself.",
        "validate": lambda results: len(results) > 0,
        "invalid_message": "This field is required", 
    }
]
def collect_answers():
    return prompt(questions)

