import requests
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# It's generally not a good practice to hardcode API keys in the code.
# In a real application, you should use environment variables.
API_KEY = "1bd3a7f5d4ffbd63f9901633c80f99a4ee19ad13acc7b8a5b8da81d3ae45f04c76b59ec586ea875c73a0738800141824"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompts = request.form.get('prompt').splitlines()
    style = request.form.get('style')

    image_urls = []
    for i, prompt in enumerate(prompts):
        if not prompt.strip():
            continue

        files = {'prompt': (None, prompt, 'text/plain')}
        if style and style != 'no-style':
            files['style'] = (None, style, 'text/plain')

        r = requests.post('https://clipdrop-api.co/text-to-image/v1',
          files=files,
          headers = { 'x-api-key': API_KEY }
        )

        if r.ok:
            image_filename = f'generated_image_{i}.png'
            with open(f'static/{image_filename}', 'wb') as f:
                f.write(r.content)
            image_urls.append(url_for('static', filename=image_filename))

    return render_template('index.html', image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
