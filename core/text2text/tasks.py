from celery import shared_task
from transformers import pipeline, set_seed

# Load the template and tokenizer
generator = pipeline("text-generation", model='gpt2')


@shared_task
def get_response(user_input):
    # Perform the text generation synchronously
    set_seed(42)
    res = generator(
        user_input,
        max_length=20,
        num_return_sequences=5,     
    )

    # Access the 'generated_text' key from the dictionary and remove user_input
    generated_text = res
   
    cleaned_text1 = generated_text[0]['generated_text'].replace(user_input, '')
    cleaned_text2 = generated_text[1]['generated_text'].replace(user_input, '')
    cleaned_text3 = generated_text[2]['generated_text'].replace(user_input, '')
    cleaned_text4 = generated_text[3]['generated_text'].replace(user_input, '')
    cleaned_text5 = generated_text[4]['generated_text'].replace(user_input, '')
    
    resultat = cleaned_text1 + ' ' + cleaned_text2 + ' ' + cleaned_text3 + ' ' + cleaned_text4 + ' ' + cleaned_text5
    
    return resultat
