# gradient-flask-example
Sometimes you want to serve a simple webservice from a GPU container. Maybe you want to test out a new model you have trained (not hodog?!) or want to serve a simple visualization of your machine learning model. This repo shows you how to make a simple flask app using Paperspace's [Gradient°](https://www.paperspace.com/gradient).

Things to note when running flask:
1. You need to have the flask server listen on all interfaces by specifying `app.run(host="0.0.0.0")` for the interface to listen on.
2. You need to install the `flask` and `flask_restful` packages as part of running the job if it is not already part of the container.  (The `flask_restful` package optional if you are not using its functionality in your flask server.)
The example here shows both these actions. 

Also note, flask by default does not provide SSL/TLS security.  See the flask package documentation for options on how to secure flask.  Here is an article on [running your flask-application over https](https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https).

## Run the job

```
paperspace jobs create --machineType P5000 --container Test-Container --ports 5000:5000 --command 'pip install flask flask_restful && python myapp.py' --workspace https://github.com/Paperspace/gradient-flask-example.git
```

or alternatively you can pull down this repo and run from your local machine:

```
> git clone https://github.com/Paperspace/gradient-flask-example.git && cd gradient-flask-example

> paperspace project init 

> paperspace jobs create --machineType P5000 --container Test-Container --ports 5000:5000 --command 'pip install flask flask_restful && python myapp.py' 

```


## Testing the web service

Your flask app is now running on the Gradient job container. Grab the public IP address of the container from the [Gradient jobs console](https://www.paperspace.com/console/jobs) or from the CLI.

<img width="350" alt="screen shot 2018-04-23 at 11 50 12 am" src="https://user-images.githubusercontent.com/585865/39146765-888c0686-46ec-11e8-8347-d99c08607647.png">

Once you have found your public IP you can hit the web service from a command line or from a web browser. Try it out!

```
curl http://35.230.20.216:5000/api?key=hellothere
```

And the output: `{"key": "hellothere"}`

<img width="1136" alt="screen shot 2018-04-23 at 12 15 57 pm" src="https://user-images.githubusercontent.com/585865/39148077-42f441b6-46f0-11e8-9ebf-3b3741e9340d.png">
