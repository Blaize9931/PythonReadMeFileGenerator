# Prompts the user for all specified details: title, description, installation, usage, license, author, and contact.
from InquirerPy import prompt
from InquirerPy.prompts.expand import ExpandChoice

def licensing_choices (_):
    return [
            ExpandChoice(key="m", name="MIT", value="MIT")
        ]
questions = [
    {
        "name":"title", "type": "input", "message": "Please provide the title of your Project"
    },

    {
        "name":"description", "type": "editor", "message": "Please provide a description of the project"
    },

    {
        "name":"installation", "type": "editor", "message": "What steps were taken to make this software runnable?"
    },

    {
        "name":"usage", "type": "editor", "message": "How is this program designed to be used?"
    },

    {
        "name":"license", "type": "expand", "choices": licensing_choices, "message": "What licensing do you have?",   
    },

    {
        "name":"author", "type": "input", "message": "Please provide name/s of author" 
    },

    {
        "name":"contact", "type": "input", "message": "Please give details of how to contact yourself." 
    }
]
def collect_answers():
    return prompt(questions)

