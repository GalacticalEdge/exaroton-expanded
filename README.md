# Exaroton Expanded

This is a fork of CollinShark's unofficial Python Wrapper for the [exaroton API](https://developers.exaroton.com/)

To use this, the steps are as quick as getting an API Token from [your Account](https://exaroton.com/account/) and you're good to go.

[![Python: 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-red)](https://gitlab.com/ColinShark/exaroton/-/blob/master/LICENSE)
<!-- [![Gitmoji: 💻🔥](https://img.shields.io/badge/Gitmoji-%F0%9F%92%BB%F0%9F%94%A5-yellow)](https://github.com/carloscuesta/gitmoji#readme) -->

## Installation
I have not uploaded this to PyPi yet, but I will once I deem this fork sufficient enough as an extension of the original project. You can help me speed this up by testing my work and opening pull requests.

If you want to try though, you can either download the source code and build it yourself or download a prebuilt wheel from the releases. The former can be done by running the setup.py file in the same directory that you extract the source code to with the following commands (if you are downloading the prebuilt wheel, please skip over to the next step):

Windows:
>> python /path/to/setup.py bdist_wheel

MacOS/Linux:
>> python3 /path/to/setup.py bdist_wheel

Once you've done either one of those steps, look for a file in the dist folder containing the .whl extension, then run one of the following commands to install it:

Windows:
>> pip3 install /path/to/build.whl

MacOS/Linux:
>> pip install /path/to/build.whl

Once you've completed those steps, you should be good to go! Enjoy it :)

## Example Usage

Currently most methods are documented in the source code. I will consider including a more accessible form of documentation in the future.

I may create a full list of all available methods, or even utilize readthedocs.org

```python
# Import exaroton and set our token
>>> from exaroton_expanded import Exaroton
>>> exa = Exaroton("API_TOKEN")

# Get information about the authenticated account
>>> exa.get_account()
{
    "_": "Account",
    "name": "Username",
    "email": "email@example.org",
    "verified": true,
    "credits": 420.69
}

# Get a list of our servers
>>> exa.get_servers()
[
    {
        "_": "Server",
        "id": "7ZxuNK5RX879BFaH",  # Thanks, random.org!
        ...
    },
    {
        "_": "Server",
        "id": "Kf48Td5iVlr8Xu24",  # Thanks, random.org!
        ...
    }
]

# Upload logs to https://mclo.gs
>>> exa.upload_logs("7ZxuNK5RX879BFaH")
{
    "_": "Logs",
    "id": "N5FR4K2",  # Thanks, random.org!
    "url": "https://mclo.gs/N5FR4K2",
    "raw": "https://api.mclo.gs/1/raw/N5FR4K2"
}

# Print logs (this'll most likely spam your output lol)
>>> exa.get_server_logs("7ZxuNK5RX879BFaH")
'one extremely long string with lines seperated by the newline escape character \n'
# It'll print each line seperately when used with `print()`!
```

All you need to make calls to the API is the Authentication Token you can get
from your account page. If you make server-specific calls, you'll need that
servers ID, too.

## Planned Features
• Convenient access to specific attributes of a server (Preliminary)

• Complete unfinished functions (Completed)

• Improved error handling (Not started)

• New Features (Planned)

Please note that I may not be able to do much work from March to May due to upcoming tests I have around that time period

and more to come

## Legal

Licensed under [MIT](https://github.com/GalacticalEdge/exaroton-expanded/blob/master/LICENSE)
