print("Chatbot")
print ("Simple chatbot app")
while True:
  user=input("User : ").lower()
  if user in ["hey","hi", "hello"]:
    print("Chatbot: Hi There How are you")
  elif "fine" in user or "good" in user:
    print("chatbot : that's grate , how can I help you today")
  elif "what is python programming" in user:
    print("chatbot: python is a high level , interpreted programming language . widely used for web development")
  elif "bye" in user:
    print("chatbot :  Good bye!")
    break
  else:
    print("sorry I did't understand plz ask something")