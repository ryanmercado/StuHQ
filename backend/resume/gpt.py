import requests
my_key = "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"
def generate_response(prompt):
    url = "https://api.openai.com/v1/engines/gpt-3.5-turbo/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 50  # Adjust max_tokens as needed
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def sendJobToGPT():
    # Send the job to GPT
    # Return the result
    str = input("Enter a prompt: ")
    print(generate_response(str))




if __name__ == "__main__":
    sendJobToGPT()