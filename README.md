# network

This is an example e2e test framework responsible for verifying the display of an ad on the client side.
For the sake of example we can assume that we are working in the SSP company which is responsible for delivering the ad to the publisher.
This is only an example - we are not sending ad requests to SSP. This example is based on a few sample ads which are placed on the page.

The flow (from deliver to display ad) looks in simplification as in the below example.
<img width="760" alt="image" src="https://github.com/hubzaj/network/assets/89909315/1cb055ec-932b-4b2f-a8b8-ee898fba2aa7">

To fetch incoming requests (all the notifications that are sent by ad markup that is placed and fired on the page in the web browser) I have decided to use [selenium-wire](https://github.com/wkeeling/selenium-wire) as Selenium and its [BiDi implementation of CDP](https://www.selenium.dev/documentation/webdriver/bidirectional/bidi_api/#network-interception) doesn't support network interception for Python due the inability to mix certain async and sync commands.

