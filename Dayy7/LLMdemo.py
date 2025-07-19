# llm is used in gen AI to generate the text , image based on prompt
# we have to use llm model like gpt,huggingface,diffuser,gemini
# we have to use gpt model to generate text
# we have to use open AI  library
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"  # or use "gpt2-medium", "gpt2-large", "gpt2-xl"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# to get the input from user using prompt
model = GPT2LMHeadModel.from_pretrained(model_name)

# to get the input from user using prompt
user_input = input("enter your message to search :")
# to encode the given inputinto tokenized
# the tokenizer is basically used to generatethe right meaning of given prompt
user_input_tokenized = tokenizer(user_input, return_tensors="pt")
# Generate text using tokinzer input
output = model.generate(
    user_input_tokenized["input_ids"],
    max_length=100,
    num_return_sequences=1,
    no_repeat_ngram_size=2,
    early_stopping=True,
)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
