# gradient-flask-example
Sometimes you want to serve a simple webservice from a GPU container. Maybe you want to test out a new model you have trained (not hodog?!) or want to serve a simple visualization of your machine learning model. This repo shows you how to make a simple flask app using Paperspace's [Gradient°](https://www.paperspace.com/gradient).

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
curl http://http://35.230.20.216/:5000/api?key=hellothere
```

And the output: `{"key": "hellothere"}`
