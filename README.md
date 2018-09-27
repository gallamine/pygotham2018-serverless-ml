# PyGotham 2018
## Serverless Machine Learning: Manage Models, Not Servers

### Create the environment

```
$ python -m venv pg2018
$ pip install -r requirements.txt
```

### Test app locally

```
$ cd webapp
$ FLASK_APP=start.py FLASK_ENV=development flask run
```

### Setup Zappa

```
zappa init
```

accept all the defaults.



## AWS Lambda Deploy

From https://blog.zappa.io/posts/docker-zappa-and-python3

Build Docker container:

```
docker build -t myzappa .
```

Add alias:

```
alias zappashell='docker run -ti -e AWS_PROFILE=zappa -v $(pwd):/var/task -v ~/.aws/:/root/.aws  --rm myzappa'
alias zappashell >> ~/.bash_profile
```

Run `zappashell` from this direcotry:

Then

```
python -m venv ve && source ve/bin/activate && pip install -r requirements.txt

```

To run in container:

```
FLASK_APP=start.py FLASK_ENV=development flask run
```

to deploy via Zappa to AWS Lambda:

```
zappa deploy dev
```

to update

```
zappa update dev
```

#### Note

Zappa had some odd behavior where it wouldn't be able to update until I ran:

```
pip install --upgrade --force-reinstall future
```