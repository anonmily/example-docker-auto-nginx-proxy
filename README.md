# Example Docker Auto Nginx Proxy

This is an example of running a basic Flask webserver behind an automatically configuring Nginx proxy.

To start up the proxy and an instance of a web server:

```
	docker-compose up -d
```

Then, you need to edit your /etc/hosts file so that **whoamiflask.local** points to 127.0.0.1 or the IP address of your Docker machine. Now, when you go to http://whoamiflask.local, you should see:

```
Hello World. I am fdbc65aa-0dc1-11e7-8704-0242c0a80003
```

Now, let's add some more web servers.

```
docker-compose scale web=4
```
This adds three more Flask web servers behind the nginx proxy. If you go to **whoamiflask.local** and keep refreshing, you should see the UUID of the Flask server process changing/rotating through each.
