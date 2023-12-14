# unique_bot

It is a telegram bot for photo and text uniqueization

if you have any questions, write to me in telegram
[@static_assert](https://t.me/static_assert)

## Table of Contents
- [Installation](#installation)
- [Setting](#setting)
- [Run](#run)

<a name="installation"></a>
## Installation
* instruction for Ubuntu20

- Download Python3.10
```sh
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10
python3.10 --version
```

- Download a project
```sh
git clone --recursive https://github.com/iassert/unique_bot.git
```

- Install python lib
```sh
pip install -r requirements.txt
```

<a name="setting"></a>
## Setting

in [@BotFather](https://t.me/BotFather) get a token
write your token in ./config.py

in [OpenAi](https://openai.com/) get a api token
write your api token in ./config.py

- move service
```
sudo mv unique_bot.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable unique_bot
```

<a name="run"></a>
## Run

```sh
sudo systemctl start unique_bot
```

