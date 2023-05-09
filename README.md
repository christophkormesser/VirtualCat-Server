# Virtual Cat Server

## How it works

First of all, activate the virtual environment:

```shell
VIRTUALCAT-SERVER:$ python3 -m venv ./VirtualCat-Server
VIRTUALCAT-SERVER:$ source bin/activate
```

Install the requirements:

```shell
(VirtualCat-Server) VIRTUALCAT-SERVER:$ pip install -r requirements.txt
```

Then start the webserver:

```shell
(VirtualCat-Server) VIRTUALCAT-SERVER:$ uvicorn main:app --reload --port 8001
```

To start the `mood_setter()`, make a request to

```txt
http://localhost:8001/
```

Now an http request is periodically being sent to the microcontroller managing the OLED Display, which will display the current mood of the cat.

## Client Part

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
