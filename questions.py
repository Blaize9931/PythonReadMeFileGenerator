# Prompts the user for all specified details: title, description, installation, usage, license, author, and contact.
from InquirerPy import prompt

questions [
    {
        "name":"title", "type": "input", "message": "Please provide the title of your Project"
    },

    {
        "name":"description", "type": "editor", "message": "Please provide a description of the project", "validate": ""
    },

    {
        "name":"installation", "type": "editor", "message": "What steps were taken to make this software runnable?", "validate": ""
    },

    {
        "name":"usage", "type": "editor", "message": "How is this program designed to be used?", "validate": ""
    },

    {
        "name":"license", "type": "expand", "message": "What licensing do you have?", "validate": ""
    },

    {
        "name":"author", "type": "input", "message": "Please provide name/s of author", "validate": ""
    },

    {
        "name":"Contact", "type": "input", "message": "Please give details of how to contact yourself.", "validate": ""
    }
]