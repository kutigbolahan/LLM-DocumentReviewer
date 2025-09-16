import ollama

response = ollama.list()

res = ollama.chat(
    model="qwen3",
    stream=True,
    messages=[{
        "role":"user","content":"why is the sky blue"
    }]
)
#print(res.message.content)
for chunck in res:
    print(chunck.message.content, end="", flush=True)