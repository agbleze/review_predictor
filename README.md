# Review Predictor App: Predicting Recommendation Status from Review
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/agbleze/review_predictor/ci.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


## 📌 Table of Contents

- [Project Description](#project-description)
- [Build and Run User App as Docker container (Only App UI)](#build-and-run-user-app-as-docker-container-only-app-ui)
    - [Clone repo](#clone-repo)
    - [Build Docker image for App](#build-docker-image-for-app)
- [Run complete prediction service: User App and Prediction API](#run-complete-prediction-service-user-app-and-prediction-api)
- [Contributing](#contributing)
- [License](#license)

---

## Project Description

This project is a shiny application that provides User Interface to use for predicting whether a customer will recommend your product based on product and service review text. The app depends on model developed using ![review classifier](https://github.com/agbleze/review_classifier.git) and ![packaged into prediction api service](https://github.com/agbleze/recommendation_predictor_API.git)

Description of the model development project can be viewed by clicking "Project Description" from the dropdown menu while clicking on "Prediction" shows the prediction UI on the app.


## Build and Run User App as Docker container (Only App UI)

The docker image for this app has already been built and is available as agbleze/review_recommender_ui:latest.

In case, you want to rebuild one yourself, use the Dockerfile in the repo for after cloning the repo. Use the commands below:

### Clone repo

```git clone https://github.com/agbleze/review_predictor.git```

### Build Docker image for App

While in the root of the cloned repo, build the image with command below:

```docker build -t YOUR_IMAGE_NAME:YOUR_IMAGE_TAG .```


## Run Complete Prediction Service: User App and Prediction API

Given the dependence of this app on a prediction api and the modular approach separating the individual services, it is best to run it as a docker compose.

Given that the app requires prediction api url to provide full functionality, appropriate secret management that caters for both production deplyoment and ease of local test is important.

To ensure that, the secrets HOST,PORT and ENDPOINT (of the prediction api) are to be provided in .env file or read directly from your secret vaults in production scenarios. When not provided, the user app uses the defaults HOST='0.0.0.0', PORT=8000, ENDPOINT="predict".

With the appropriate secret in .env file, use the docker-compose.yml file to run the containers for both prediction api and user app as follows: 

```docker compose up```

Access the app url which defaults to localhost:8000


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`review_predictor` was created by Agbleze. It is licensed under the terms of the MIT license.
