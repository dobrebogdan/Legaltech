from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

en_text = "This case will be judged by the court next week."

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

tokenizer.src_lang = "en"

def translate_en_to_ro(english_text):
    encoded_english_text = tokenizer(english_text, return_tensors="pt")
    generated_romanian_tokens = model.generate(**encoded_english_text, forced_bos_token_id=tokenizer.get_lang_id("ro"))
    romanian_text = tokenizer.batch_decode(generated_romanian_tokens, skip_special_tokens=True)
    return romanian_text
