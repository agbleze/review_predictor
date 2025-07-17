# Review predictor: User app for predicting recommendation status from review text
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/agbleze/review_predictor/ci.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


## 📌 Table of Contents

- [Review predictor: User app for predicting recommendation status from review text](#review-predictor-user-app-for-predicting-recommendation-status-from-review-text)
  - [📌 Table of Contents](#-table-of-contents)
- [Project Description](#project-description)
  - [Running App UI standalone](#running-app-ui-standalone)
  - [Running complete prediction service: App and prediction api](#running-complete-prediction-service-app-and-prediction-api)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

---

# Project Description

This project is a shiny application that provides User Interface to use for predicting whether a customer will recommend your product based on product and service review text. The app depends on model developed using ![review classifier](https://github.com/agbleze/review_classifier.git) and ![packaged into prediction api service](https://github.com/agbleze/recommendation_predictor_API.git)

Description of those project which forms cornerstone of the app can be viewed by clicking "Project Description" from the dropdown menu while clciking on "Prediction" shows the prediction UI


## Running App UI standalone
Given the dependence of this app on a prediction api and the modular approach separating individual services, it is best to run it as a docker container.

The docker image for this app has already been built and is available as agbleze/review_recommender_ui:latest

In case, you want to rebuild one yourself, use the Dockerfile in the repo for that.

## Running complete prediction service: App and prediction api

Given that the app requires prediction api url to provide full functionality, appropriate secret management that caters for both production deplyoment and ease of local deployment test is important.

To ensure that, the secrets HOST,PORT and ENDPOINT are to be provided in .env file or read directly from your secret vaults in production scenarios.

With the appropriate secret in .env file, use the docker-compose.yml file to run the containers for both prediction api and user app as follows: 

```docker compose up```

Access the app url which defaults to localhost:8000


## Usage

The package provides a high level entrypoint to train model from the terminal. Detailed demonstration of this including dataset format expected is provided in docs/example.ipynb


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`review_predictor` was created by Agbleze. It is licensed under the terms of the MIT license.
