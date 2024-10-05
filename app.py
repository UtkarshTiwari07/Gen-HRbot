from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__, template_folder = "template")
CORS(app)

# Load model and tokenizer
model_dir = '//Users//amitgupta//Downloads// hrchatbot'  # Ensure this path points to the model directory
model = GPT2LMHeadModel.from_pretrained(model_dir)
tokenizer = GPT2Tokenizer.from_pretrained(model_dir)

class HRChatbot:
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
        self.model.eval()

    def get_response(self, question):
        prompt = f"<BOS> Question: {question} Answer:"
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt').to(self.device)

        try:
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_length=150,
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.7,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            response = self.tokenizer.decode(output[0], skip_special_tokens=True)
            answer = response.replace(prompt, "").strip()

            return answer if answer else "I'm sorry, I couldn't generate a relevant answer. Please try rephrasing your question."
        except Exception as e:
            return f"Error: {str(e)}"

chatbot = HRChatbot(model, tokenizer)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')
    response = chatbot.get_response(question)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
