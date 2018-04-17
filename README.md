Setup
=====
1. Fill out `config.yaml`.
1. `virtualenv --python python2 env`.
2. `source env/bin/activate`.
1. `pip install -t lib -r requirements.txt`.
2. `gcloud app deploy`.
3. `gcloud app deploy cron.yaml`.

Running locally
===============
Usually done with `dev_appserver.py app.yaml`. There's some kind of ssl related issue that prevents tweets from being sent though.
