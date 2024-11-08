from transformers import T5ForConditionalGeneration, T5Tokenizer

def generator(generator_model, tokenizer_model, retrieved_doc):
    generator = T5ForConditionalGeneration.from_pretrained(generator_model)  # Generation model
    tokenizer = T5Tokenizer.from_pretrained(tokenizer_model )
    
    input_text = f"Summarize the following: {retrieved_doc}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = generator.generate(input_ids, max_length=50, num_beams=5, early_stopping=True)
    generated_response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return generated_response

