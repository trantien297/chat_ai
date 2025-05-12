from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM
with model.chat_session() as session:
    print('############################################')
    print('GPT4All Screen - Open')
    print('############################################')
    print('Llama AI: How are you today? Can I help you?')

    while True:
        user_input = input("You: ")  # User input
        
        if user_input.lower() == "exit":
            print("Bot: Goodbye! See you again.")
            break  # Thoát vòng lặp nếu người dùng gõ 'exit'
        
        # Bot phản hồi dựa trên câu hỏi của người dùng
        response = session.generate(user_input, max_tokens=1024)
        
        print("Llama AI: ", response)  #

    #print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
    print('############################################')
    print('GPT4All Screen - Close')
    print('############################################')