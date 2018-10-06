# sotawhat

This script runs using Python 3.

## Setup

```
git clone https://github.com/justanhduc/sotawhat.git
```

First, install the required packages. This script only requires ``nltk`` and ``pyspellchecker``.

```bash
$ pip3 install -r requirements.txt
```

Then install the module

```
cd sotawhat
pip3 install .
```

## Known bugs and fix

If you run the error that the package ``punkt`` doesn't exist, download it by going into your Python environment and running:

```bash
$ python3

>>> import nltk
>>> nltk.download('punkt')
```

In MacOS, you can get the SSL error

```
[nltk_data] Error loading punkt: <urlopen error [SSL:
[nltk_data]     CERTIFICATE_VERIFY_FAILED] certificate verify failed:
[nltk_data]     unable to get local issuer certificate (_ssl.c:1045)>
```

this will be fixed by reinstalling certificates
```shell
$ /Applications/Python\ 3.x/Install\ Certificates.command
```

## Usage

To query for a certain keyword, run:

```bash
$ python3 -m sotawhat [keyword] -n [number of results] -hn [show only papers with numerical results]
```

For example:

```bash
$ python3 -m sotawhat perplexity -n 10
```

or 

```bash
$ python3 -m sotawhat language model -n 10 -hn
```

If you don't specify the number of results, by default, the script returns 5 results. Each result contains the title of the paper with author and published date, a summary of the abstract, and link to the paper.

We've found that this script works well with keywords that are:
+ a model (e.g. transformer, wavenet, ...)
+ a dataset (e.g. wikitext, imagenet, ...)
+ a task (e.g. language model, machine translation, fuzzing, ...)
+ a metric (e.g. BLEU, perplexity, ...)
+ random stuff
