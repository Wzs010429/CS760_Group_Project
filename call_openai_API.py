import openai

def ai_function_generation(demo, context, question, requirements, model = "gpt-3.5-turbo"):
    # parse args to comma separated string
    messages = [{"role": "system",
                "content": demo},
                {"role": "user",
                "content": f"Propositions: ```{context}```\nQuestion: ```{question}```, ```{requirements}```"}]

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0
    )

    return response.choices[0].message["content"]

def ai_generation_adjustment(demo, code, error_message, model = "gpt-3.5-turbo"):
    # parse args to comma separated string
    messages = [{"role": "user",
                 "content": f"{demo}\n Here is the original code: ```{code}```\n And the exception that was thrown is: ```{error_message}```"}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message["content"]

def ai_generation_check(demo, question, model = "gpt-3.5-turbo"):
    # parse args to comma separated string
    messages = [{"role": "user",
                 "content": f"{demo}\n The sentence you are expected to decide is: ```{question}```"}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message["content"]


