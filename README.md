# Advertisements Test

[<img src="https://img.shields.io/badge/development-how_to_start-blue">](https://github.com/hubzaj/network/tree/main#working-with-terminal)
[<img src="https://img.shields.io/badge/configuration-OPTIONS-yellow">](https://github.com/hubzaj/network/tree/main#configuration)
[<img src="https://img.shields.io/badge/dockerhub-images-important.svg?logo=Docker">](https://hub.docker.com/r/hubertzajac6/network)

## Background

Here is an illustrative end-to-end (E2E) test framework designed to validate the appearance of an advertisement on the client side. In this example, we can assume we are operating within an SSP (Supply-Side Platform) company responsible for delivering ads to publishers.

Please note that this is a hypothetical scenario, and for the purposes of this example, we are not sending ad requests to the SSP. Instead, a few sample ads (hardcoded in the source code [here](https://github.com/hubzaj/network/blob/bb8d33aa5d96e672eb5df76b67184f58a162ec94/network/banner/default.py#L5)) are defined and placed on the page.

The simplified flow, from delivering to displaying the ad, is illustrated in the example below.

![Image](https://github.com/hubzaj/network/assets/89909315/1cb055ec-932b-4b2f-a8b8-ee898fba2aa7)

This project focuses specifically on the last part - ad display. The SSP delivers the ad, which is then displayed on the user's page, as depicted in the image below. A successfully displayed ad must send all the notifications attached during the delivery chain by all related companies involved in monetization.

![Image](https://github.com/hubzaj/network/assets/89909315/2eb2007b-8fbd-4447-8731-e8b4d34a1e86)

The primary responsibility of this framework is to validate if all the required requests have been sent after the successful display of the ad. To intercept and collect all incoming requests (notifications sent by the ad markup placed and fired on the page in the web browser), I opted to use [selenium-wire](https://github.com/wkeeling/selenium-wire). This choice was made because pure Selenium, along with its BiDi implementation of CDP, does not support network interception for Python due to constraints in mixing certain asynchronous and synchronous commands.

## How to build project

Requirements:

-     Python ^3.11
-     Poetry ^1.5.1

### How to run

* Execute from your preferred IDE (PyCharm is recommended). Tests are located in the `tests/` directory.
* Execute from the command line using the make command, e.g., `poetry run browser-tests`.
* Execute from the command line, e.g., `poetry run pytest -n auto -m browser`.
* [CI/CD] Tests can also be run on a Kubernetes cluster as a job. This is useful when the entire infrastructure (devint/qa/prod environments) relies on Kubernetes.
  * Additionally, you can experiment with it on your local machine by using [minikube](https://minikube.sigs.k8s.io/docs/start/).
  * Kubernetes configuration is managed using [Helm Charts](https://helm.sh/docs/intro/cheatsheet/).

### Working with terminal

1. Install `asdf` with required plugins.

 ```
  > brew install asdf
  > asdf plugin-add python
  > asdf plugin-add poetry
  > asdf install
 ```

### Configuration

Configuration is designed in a way to be controlled by environment variables.

    [BROWSER]

##### Default:

* Browser: `Chrome (without headless)`

#### Supported browsers:

* `CHROME`
* `CHROME_HEADLESS`
* `CHROME_IN_DOCKER` [NOT READY YET]
