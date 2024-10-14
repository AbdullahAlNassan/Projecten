import openai

openai.api_key = "sk-svcacct-ITWi955WYuJOW4hN9aG4ZvbmTuyPaYx_TUWScLu8dW8EhQjqCTdGm59S9t4txIec3JQxqT3BlbkFJnz2h5piog_CdqmXPi0QIJz9FL_26rRJc57MFZa1OCo25Zt37m0hxbC6TBmY5xc4cyhjAA"

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)




def parse_with_openai(dom_chunks, parse_description):
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = template.format(dom_content=chunk, parse_description=parse_description)

        try:
            # Vraag OpenAI om de informatie te parsen
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Je kunt ook "gpt-4" gebruiken als je dat hebt
                messages=[
                    {"role": "system", "content": "You are an expert text parser."},
                    {"role": "user", "content": prompt}
                ]
            )

            # Haal het antwoord van OpenAI op
            parsed_response = response['choices'][0]['message']['content']
            parsed_results.append(parsed_response)
            print(f"Parsed batch: {i} of {len(dom_chunks)}")

        except Exception as e:
            print(f"Error in batch {i}: {e}")
            parsed_results.append("")

    return "\n".join(parsed_results)