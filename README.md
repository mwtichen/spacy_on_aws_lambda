# Training and Deploying a custom NER model using Zappa

I trained a custom named entity recognition (NER) model using the MIT movie datasets, available [here](https://groups.csail.mit.edu/sls/downloads/movie/).

Spacy's NER model requires the data to be in BILOU format.

Unfortunately, the MIT movie data was in BIO format, so I had to figure out how to convert BIO to BIOLU format.

I did this in the preparing_data.ipynb notebook.

Using the small English language model, I retrained the NER model in the Retraining_spacy_ner.ipynb notebook.

IMO, this was straightforward. The challenging part was figuring out how to deploy the model using Zappa.

First, I made a flask app, app.py, drawing inspiration from [this](https://act-labs.github.io/posts/aws-spacy-layer/) webpage.

Next, I tested the app in the flask_app_test.ipynb notebook.

After that, I followed the instructions from[this](https://pythonforundergradengineers.com/deploy-serverless-web-app-aws-lambda-zappa.html) webpage, using my app rather than their's.

Lastly, I tested the lambda function in the zappa_app_test.ipynb notebook.

All tests were successful. :)