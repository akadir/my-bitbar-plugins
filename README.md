# my-bitbar-plugins

[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/akadir/my-bitbar-plugins/blob/master/LICENSE)

## Installation
- Install [BitBar](https://getbitbar.com/)
- Copy plugin file to your BitBar plugin directory

## Plugin List

1. [Display Yahoo Currency Rates](#01-display-yahoo-currency-rates)
2. [Display Command Output From Remote Machine](#02-display-command-output-from-remote-machine)
3. [Display Tweet Count of Twitter Account](#03-display-tweet-count-of-twitter-account)
4. [Display Subscriber Count of Youtube Account](#04-display-subscriber-count-of-youtube-account)

## Descriptions

## 01-Display Yahoo Currency Rates

Plugin to display currency rates from [Yahoo Finance](https://finance.yahoo.com)

Put yahoo currency symbols as key and id's as value into `currencies` dictionary in [currency-converter.py](/currency-converter.py) file.

<b>ex:</b>

```python
currencies['$'] = 'TRY=X'
currencies['€'] = 'EURTRY=X'
```

![currency-converter](/images/currency-converter.png)

## 02-Display Command Output From Remote Machine

Plugin to display command output from remote machine.

Set `ip` and`username` variables and add desired commands to run into `commands` variable in [display-command-output-from-remote-machine.py](/display-command-output-from-remote-machine.py) file.

<b>p.s.</b>: passwordless ssh configuration must be done before running this script.

<b>ex:</b>

```python
ip = "10.151.23.1"
username = "user"

...

commands['CurrentTime'] = 'date'
commands['Hw'] = 'echo HelloWorld'
```


![display-command-output-from-remote-machine](/images/display-command-output-from-remote-machine.png)

## 03-Display Tweet Count of Twitter Account

Plugin to display tweet count of twitter account with latest tweet's timestamp.

Set `username` variable in [display-tweet-count.py](/display-tweet-count.py) file.

<b>ex:</b>

```python
username = "VENETHIS"
```

![display-tweet-count](/images/display-tweet-count.png)

## 04-Display Subscriber Count of Youtube Account

Plugin to display subscriber count of youtube account.

Set `account_name` variable in [display-youtube-subscriber-count.py](/display-youtube-subscriber-count.py) file.

<b>ex:</b>

```python
account_name = "Besiktas"
```

![display-tweet-count](/images/display-youtube-subscriber-count.png)
