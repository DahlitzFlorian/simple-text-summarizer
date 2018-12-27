# Simple Text Summarizer #
## Description ##
This repository contains a simple text summarizer written in Python.
It's inspired by a [Medium article](https://towardsdatascience.com/write-a-simple-summarizer-in-python-e9ca6138a08e)
from Jody LeCompte.

version 1.0

## Third-Party Libraries ##
- [nltk](https://github.com/nltk/nltk/)<br>
Make sure to further install _punkt_ and _stopwords_ via the REPL:
```python
>>> import nltk
>>> nltk.download("punkt")
>>> nltk.download("stopwords")
```

If you run into an SSL Error, make sure to install your certificates using the following command:
```bash
/Applications/Python 3.6/Install Certificates.command
```
where 2.6 has to be replaced by your used version of Python 3. [Further information](https://stackoverflow.com/a/42890688/6707020).