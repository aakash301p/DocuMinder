# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
#
# llm = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen3-8B",
#     task="text-generation",
#     max_new_tokens=512,
#     do_sample=False,
#     provider="auto"
# )
#
# chat_model = ChatHuggingFace(llm=llm)
#
#
# while True:
#     prompt = input("give input:")
#     response = chat_model.invoke(prompt)
#     print(response.content)
