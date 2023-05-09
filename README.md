# Virtual Cat Server

## How it works

First of all install python if it's not already installed (<https://www.python.org/downloads/>).
Then create and activate the virtual environment:

```shell
~:$ python3 -m venv ./vcat-env
~:$ cd vcat-env
vcat-env:$ source bin/activate
```

Clone the repo and move into it:

```shell
(vcat-env) vcat-env:$ git clone git@github.com:christophkormesser/VirtualCat-Server.git
(vcat-env) vcat-env:$ cd VirtualCat-Server
```

Install the requirements:

```shell
(vcat-env) VirtualCat-Server:$ pip3 install -r requirements.txt
```

Then start the webserver:

```shell
(vcat-env) VirtualCat-Server:$ uvicorn main:app --reload --port 8001
```

To start the `mood_setter()`, make a request to

```txt
http://localhost:8001/
```

Now an http request is periodically being sent to the microcontroller managing the OLED Display, which will display the current mood of the cat.

### Start the Client (Optional)

This step will be done on the microcontrollers, but for testing purposes, here is an implementation for the laptop.

Start the client application in a new tab of your terminal and make sure to activate the virtual environment (`source bin/activate`):

```shell
(vcat-env) VirtualCat-Server:$ uvicorn client:app --reload --port 8000
```

The client now needs to send the gathered proximity data with a post request to the server with the following url:

```txt
http://localhost:8001/pet
```

... and the following body:

```json
{
    "message" : "string", // (optional)
    "data": float
}
```

## Expected Results

When the server receives the proximity data, it will check if the value is above a certain threshold. If it is, the petting is being detected and the action is performed.
