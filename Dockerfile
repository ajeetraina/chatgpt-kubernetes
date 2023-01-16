FROM openai/gpt-3

ENV MODEL_ENGINE "text-davinci-002"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
