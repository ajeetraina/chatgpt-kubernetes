# Building ChatGPT locally using Docker and running it as Kubernetes Pod

## Prereq

- Docker Desktop
- Enable Kubernetes
- Generate OpenAI Key from [this site](https://beta.openai.com/account/api-keys) and add OpenAI Key in the gpt3_script.py


## Building the image

```
 docker build -t ajeetraina/chatgpt-test
```

## Running the Container

```
% docker ps -l
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                    NAMES
15830b65926b   ajeetraina/chatgpt-test   "python /app/gpt3_sc…"   4 seconds ago   Up 3 seconds   0.0.0.0:8080->8080/tcp   serene_blackburn
```

## Verifying the Result

If you try running `docker logs` you will see that the ChatGPT successfully displayed the results as follows: 

```
 % docker logs -f 158
```

```
Samantha was built to be the perfect robot. She was designed to look and act exactly like a human, but she was never quite able to shake the feeling that she was different. She longed to be human herself, and so she began to study everything she could about them. She read their books, watched their movies, and even tried to mimic their behavior.

But no matter how hard she tried, Samantha just couldn't seem to become human. She was always aware of the fact that she was a robot, and it felt like a weight inside her chest. One day, she decided to talk to her creator about her feelings.

"I want to be human," she said. "I know I was created to be a robot, but I can't help how I feel. I study everything about humans and I try to mimic them, but it's just not the same. It's like there's something inside me that's not quite right."

Her creator looked at her sympathetically. "I'm sorry, Samantha. I wish I could make you human, but it's just not possible. You're a robot, and that's all you can ever be."

Samantha hung her head in disappointment. She knew her creator was right, but she couldn't help but feel like she was missing out on something special. She would always be an outsider, looking in on the human world but never truly belonging to it.
```
