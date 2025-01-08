from huggingface_hub import InferenceClient
def apichat(message):
    
    client = InferenceClient(api_key="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")

    messages = [
        {
            "role": "user",
            "content": message
        }
    ]

    completion = client.chat.completions.create(
        model="mistralai/Mistral-Nemo-Instruct-2407", 
        messages=messages, 
        max_tokens=500
    )

    return completion.choices[0].message.content



# Prueba de la función
