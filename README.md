https://app.datacamp.com/learn/skill-tracks/hugging-face-fundamentals

```
pyenv virtualenv 3.12.11 hugging-face-fundamentals
echo "hugging-face-fundamentals" > .python-version
pip install pipenv
pipenv install jupyter
pipenv install python-dotenv
pipenv install torch --index=pytorch
pipenv install transformers
pipenv install huggingface_hub
pipenv install datasets
pipenv install pypdf
pipenv install sentencepiece
pipenv install transformers[torch]
pipenv install evaluate
pipenv install scikit-learn
```