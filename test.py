from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Replace "MODEL_NAME" with the actual name of the pretrained tactic generator model.
tactic_generator_model_name = "kaiyuy/leandojo-lean3-tacgen-byt5-small"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(tactic_generator_model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(tactic_generator_model_name)

# Example proof state
state = "P Q R : Prop,\nh : P → Q,\nhq : Q → R,\nhqr : P\n⊢ R"
tokenized_state = tokenizer(state, return_tensors="pt")

# # Generate a single tactic.
# tactic_ids = model.generate(tokenized_state.input_ids, max_length=1024)
# tactic = tokenizer.decode(tactic_ids[0], skip_special_tokens=True)
# print("Generated Tactic:")
# print(tactic)

# Generate multiple tactics via beam search.
tactic_candidates_ids = model.generate(
    tokenized_state.input_ids,
    max_length=1024,
    num_beams=4,
    length_penalty=0.0,
    do_sample=False,
    num_return_sequences=4,
    early_stopping=False,
)
tactic_candidates = tokenizer.batch_decode(
    tactic_candidates_ids, skip_special_tokens=True
)
print("\nGenerated Tactic Candidates:")
for tac in tactic_candidates:
    print(tac)
