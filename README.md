# ACC0UN7-CH3CK Tool

## Overview

ACC0UN7-CH3CK Tool is an account Knocking tool that uses Selenium to check whether an account exists on popular websites such as ebay, espn, quora, spotify, and pinterest. The tool is used to avoid the manual checking of the account exists in the website using the email address by Automating the process using the Webscraping tool with Python 


## Table of Contents

- [Advantage](#Advantage_of_using_this_Tool)
- [Prerequisites](#Requirements)
- [Installation](#Setup)
- [Usage](#Usage)
- [Results](#Result)

## Advantage_of_using_this_Tool

Automating the Manual-checking process for Acount Knocking Technique.

- **Automation and Simulated User Interaction:** Selenium enables automated testing and interaction with web elements, mimicking user behavior more accurately than account knocking, which relies on manual, sequential actions.
- **Scalability and Extensibility:** Selenium can be scripted to handle a wide range of scenarios, making it suitable for testing complex web applications and scalable for various use cases, while account knocking might be limited by manual execution and scope.
- **Efficiency and Repeatability:** Selenium scripts can be reused and executed multiple times, ensuring consistent test scenarios and reducing manual effort, while account knocking might require repetitive manual actions.

## Requirements
- [Firfox-WebDriver](https://github.com/mozilla/geckodriver/releases)
- [Typer](https://github.com/tiangolo/typer)
- [Selenium](https://www.selenium.dev/)
- [Colorma](https://github.com/tartley/colorama)
- [Prettytable](https://github.com/jazzband/prettytable)


## Setup

1. Clone the repository: `git clone https://github.com/mohanrajmdev/ACC0UN7-CH3CK-T00L.git`
2. Change the directory `cd ACC0UN7-CH3CK-T00L`
3. Use FireFox Browser for this script to work and also install [Webdriver](https://github.com/mozilla/geckodriver/releases) for firefox.
4. Install the requirements using this command `pip3 install -r requirements.txt`


## Usage

    $ python3 main.py --help // To know about the tool details

```bash
$ python3 main.py --email example@gmail.com --url ebay,spotify
```

## Result

