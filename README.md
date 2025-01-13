# Game recommendation website

## Table of contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)

## Introduction

The goal of this repository is to implement one of the game recommendation methods developed in the [Game recommendation system](https://github.com/Eniterusx/Game-recommendation-system) project. Specifically, it uses a nearest neighbors approach to generate recommendations based on user similarity. Despite not being the most effective method from the comparative analysis, this method can generate recommendations in a short time manner, making it suitable for a web application. The website is available [here](https://game-recommendation-web.vercel.app/).

This implementation is presented in the form of a simple web application that allows users to generate recommendations by providing a link to their Steam profile. The app processes the user's game data and generates recommendations based on user similarity, offering a practical demonstration of the methodology described in the original project.

<!-- For more details about the dataset, the other recommendation methods, and the comparative analysis, visit the [Game recommendation system](https://github.com/Eniterusx/Game-recommendation-system) repository. -->

## Requirements

- Python 3.11.11
- conda
- Django
- dotenv
- requests
- pandas
- numpy

## Installation

1. Clone the repository:
```shell
git clone https://github.com/Eniterusx/Game-recommendation-website
cd Game-recommendation-website
```

2. Create a conda environment and install the required packages:
```shell
conda env create -f requirements.yaml
conda activate game-rec-web
```

## Usage

1. Create a `.env` file with the following content:
```shell
API_KEY=your_steam_api_key
```
The `API_KEY` is the Steam API key that you can get [here](https://steamcommunity.com/dev/apikey).

2. Run the Django server:
```shell
python manage.py runserver
```

3. The application is now available at `http://127.0.0.1:8000/`.