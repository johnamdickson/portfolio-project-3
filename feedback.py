from datetime import date

def get_feedback():
    name_input = input('Please enter your name or leave blank to remain anonymous:\n')
    feedback_input = input('Please enter your feedback:\n')
    now = date.now()
    date_input = now.strftime("%d/%m/%Y, %H:%M:%S")