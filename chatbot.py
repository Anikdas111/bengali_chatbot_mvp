from transformers import pipeline
chatbot = pipeline("text-generation", model='gpt2')
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit","quit"]:
        break
    response = chatbot(user_input, max_length=100, do_sample=True, temperature=0.7)
    print("Bot:", response[0] ['generated_text'])
