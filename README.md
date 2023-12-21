 # Cobalt Labs Terminal

## Overview
The Cobalt Labs Terminal is a command-line tool that allows users to perform various tasks, such as:
- Retrieving the IP address of a website
- Determining the location of an IP address
- Selecting a random item from a list

## Installation
To install the Cobalt Labs Terminal, simply clone the repository and run the `install.sh` script:

```bash
git clone https://github.com/cobalt-labs/terminal.git
cd terminal
./install.sh
```

## Usage
Once installed, you can launch the Cobalt Labs Terminal by running the `cobalt` command in your terminal.

The terminal will present you with a prompt, where you can enter commands.

## Commands
The following commands are available in the Cobalt Labs Terminal:

- `webip`: Retrieves the IP address of a website.
- `locip`: Determines the location of an IP address.
- `pick`: Selects a random item from a list.
- `exit`: Exits the Cobalt Labs Terminal.

## Examples
Here are some examples of how to use the Cobalt Labs Terminal:

- To retrieve the IP address of `google.com`, enter the following command:

```bash
webip google.com
```

- To determine the location of the IP address `8.8.8.8`, enter the following command:

```bash
locip 8.8.8.8
```

- To select a random item from the list `apple, orange, banana`, enter the following command:

```bash
pick apple, orange, banana
```
