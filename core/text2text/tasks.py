from celery import shared_task
from transformers import pipeline

# Load the template and tokenizer
generator = pipeline("text-generation", model='distilgpt2')

@shared_task
def get_response(user_input):
    # Perform the text generation synchronously
    res = generator(
        user_input,
        max_length=30,
        num_return_sequences=2,
    )
    print(res[0]['generated_text'])
    return res[0]['generated_text']
