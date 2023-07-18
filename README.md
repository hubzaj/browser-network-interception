# network

This is an example e2e test framework responsible for verifying the display of an ad on the client side.
For the sake of example we can assume that we are working in the SSP company which is responsible for delivering the ad to the publisher.
This is only an example - we are not sending ad requests to SSP. There are defined a few sample ([hardcoded in source code](https://github.com/hubzaj/network/blob/bb8d33aa5d96e672eb5df76b67184f58a162ec94/network/banner/default.py#L5)) ads which are placed on the page.

The flow (from deliver to display ad) looks in simplification as in the below example.

<img width="480" alt="image" src="https://github.com/hubzaj/network/assets/89909315/1cb055ec-932b-4b2f-a8b8-ee898fba2aa7">

In this project we are focusing on the last part - ad display. SSP delivers the AD which is being displayed on the page for the user as in the picture below. The ad that has been displayed with success has to send all the notifications that have been attached during the delivery chain by all related companies (monetization).

<img width="480" alt="image" src="https://github.com/hubzaj/network/assets/89909315/2eb2007b-8fbd-4447-8731-e8b4d34a1e86">

This framework is responsible for validating if all the requests have been sent after the successful ad display. To intercept and collect all incoming requests (all the notifications that are sent by ad markup that is placed and fired on the page in the web browser) I have decided to use [selenium-wire](https://github.com/wkeeling/selenium-wire) as pure Selenium and its [BiDi implementation of CDP](https://www.selenium.dev/documentation/webdriver/bidirectional/bidi_api/#network-interception) doesn't support network interception for Python due the inability to mix certain async and sync commands.

# How to build project

Requirements:
- Python ^3.11
- Poetry ^1.5.1

# Compiling using terminal

1. Install `asdf` with required plugins.
 ```
  > brew install asdf
  > asdf plugin-add python
  > asdf plugin-add poetry
  > asdf install
 ```
