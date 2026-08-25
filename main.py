


system_message = SystemMessage(
    content= prompt + context
)
while True:
    prompt = input("give input: ")
    if prompt.lower() in ["exit", "quit"]:
        break
    messages = [
        system_message,
        HumanMessage(content=prompt)
    ]

    response = client.invoke(messages)

    print("bot:", response.content)