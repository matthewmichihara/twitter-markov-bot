A vanilla implementation of a Twitter markov bot that runs on Google AppEngine.

Setup
=====
1. Fill out `config.yaml`.
2. `virtualenv --python python2 env`.
3. `source env/bin/activate`.
4. `pip install -t lib -r requirements.txt`.
5. `gcloud app deploy`.
6. `gcloud app deploy cron.yaml`.

Running locally
===============
Usually done with `dev_appserver.py app.yaml`, but there's some kind of ssl related issue that prevents tweets from being sent.
