## 3.0 Deploying your Webapp to Heroku

> **Note:** Make sure you sign up for [a free Docker Hub account](http://hub.docker.com/) before starting this chapter.


Now that you’ve created you first Docker Image, you can publish it on Docker Hub for later use.  You can make your Docker Hub images available to developers everywhere or just keep them privately for yourself.  The same way GitHub is a place for you to store and collaborate on git repos, Docker Hub is place for you to store and collaborate on Docker Images.

### 3.1 Login to your Docker Hub Account

In order to publish your image on Docker Hub, you need to login on the command line.  You can do that by using the following command:

```
$ docker login
```

Your username is the Docker ID you created on Docker Hub.  You password will be hidden when you type it, so don’t worry about displaying it to anyone.

### 3.2 Push your image to Docker Hub

Now that you've created and tested your image, you can push it to [Docker Hub](https://hub.docker.com). All you have to do is:

```
$ docker push YOUR_USERNAME/myfirstapp
```
Now that you are done with this container, stop and remove it since you won't be using it again.

Open another terminal window and execute the following commands:

```
$ docker stop myfirstapp
$ docker rm myfirstapp
```

or

```
$ docker rm -f myfirstapp
```

### 3.3 Deploy your Image on Docker Cloud

Now that you’ve created a web application using Docker, you may want to deploy it to the Internet.  Docker has a service called [Docker Cloud](http://cloud.docker.com) that enables you to easily deploy and manage applications.  It supports everything from simple, one container apps to complex micro-service stacks.

You can bring your own server with you if you have one or sign up for a popular cloud hosting provider like Amazon Web Services (AWS). 

To learn how to deploy on Docker Cloud, follow [this tutorial](https://docs.docker.com/docker-cloud/getting-started/deploy-app/1_introduction/).

### 3.4 Next steps
Now that you've built some images and pushed them to the web, you can explore more of Docker by checking out [the documentation](https://docs.docker.com). And if you need any help, check out the [Docker Forums](forums.docker.com) or [StackOverflow](https://stackoverflow.com/tags/docker/).
