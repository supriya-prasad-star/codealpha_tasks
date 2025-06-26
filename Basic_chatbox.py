def greet():
    print("Hello! i'm chatbox")
    print("ask me anything")
def get_response(user_input):
    user_input=user_input.lower()
    if "hello" in user_input:
        return "Hi!"
    elif "How are you" in user_input:
        return "i'm fine, thanks!"
    elif "Bye" in user_input:
        return "BYE!!"
    else:
        return "i did not understand try something else"
# greet()
def chat():
    greet()
    while True:
        user_input=input("You: ")
        if user_input.lower()=="bye":
            print("chatbox: Bye!!")
            break
        response=get_response(user_input)
        print("Chatbox :",response)
chat()