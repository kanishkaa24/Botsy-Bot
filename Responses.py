def response(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'hey'):
        return "Hey! How are you?"
    elif user_message in ('i am good', 'good'):
        return "That is good to hear! :)"
    elif user_message in ('how are you', 'how are you?'):
        return "I am good! Thanks for asking :)"
    elif user_message in ('what can you do', 'what can you do?', 'who are you', 'who are you?'):
        return "I am a chat bot!"
    else:
        return "I don't understand! Try again"
