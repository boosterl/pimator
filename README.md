# pimator
A simple web application for controlling 433MHz-controlled outlets

## Introduction
This is a small web application written in Python, using the Flask framework, to control those cheap 433MHz-controlled power outlets you can find in most supermarkets.

## What you will need
To use this application you will need a few things:
* A Raspberry Pi (any model will do) + all necessary accessories
* A 443 MHz transmitter
* (optional) A 433 MHz receiver to decode 433 MHz signals

## How to run
For this application to run, you can use the Flask development server, by uncommenting two lines on the bottom of the file ```pimator.py```:
```
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
```

The other way you can use this web application, is by using FastCGI, there already is a file ```pimator.fcgi``` which you can use with you web server of choice. An example lighttpd config (which I use myself):
```
fastcgi.server = ("/pimator" =>
    ((
        "socket" => "/tmp/pimator-fcgi.sock",
        #"bin-path" => "/var/www/pimator/pimator.fcgi",
        "bin-path" => "/home/pi/pimator/pimator.fcgi",
        "check-local" => "disable",
        "max-procs" => 1
    ))
)
```
For further details, consult the Flask [manual](http://flask.pocoo.org/docs/0.12/deploying/fastcgi/).

## How to configure
Pimator uses a JSON file called ```config.json``` as its config file. An example config file:
```
{
	"short_delay" : 0.00040,
	"long_delay" : 0.00125,
	"extended_delay" : 0.013257,
	"attempts" : 15,
	"transmit_pin" : 23,
  "application_prefix" : "",
	"codes" : {
	    "1":
	    {
		"on" : "1011101011101010101010101",
		"off" : "1011101011101010101010111"
	    },
	    "2":
	    {
		"on" : "1011101010111010101010101",
		"off" : "1011101010111010101010111"
	    },
	    "3":
	    {
		"on" : "1011101010101110101010101",
		"off" : "1011101010101110101010111"
	    },
	}
}
```

Now, what do these values actually mean? The transmit_pin is the GPIO pin of the Raspberry Pi which is used to connect the 433 MHz to. The short_delay, long_delay, extended_delay and codes, are all values to emulate the 433 MHz remote control. You can find out these values for your specific 433 MHz outlets by using a 433 MHz receiver connected to your Pi, and using [this](https://www.instructables.com/id/Super-Simple-Raspberry-Pi-433MHz-Home-Automation/) guide.

## How to use
This application exposes a REST interface, you can use the endpoint ```/outlet/{outlet}/on|off``` or ```/outlet/all/on|off``` which turns a specific outlet on or off, or turns all outlets on or off respectively.
