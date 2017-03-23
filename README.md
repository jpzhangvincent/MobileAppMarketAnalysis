Mobile App Market Analysis
==============================

The explosive growth of the mobile application (app) market has made it difficult for users to find the most interesting and relevant apps from the hundreds of thousands that exist today. We are interested to analyze the quality of apps and understand the user experiences of using mobile apps on the Itune App Store. In this project, we would go through the data science cycle including problem/data curations, data management, data analytics and result-oriented presentations through data visualization.

## To do list
- [x] Data Acquisition through Web Scraping with __Scrapy__ 
- [x] Data Management with __MongoDB__
- [x] Exploratory Data Analysis 
    - [x] Explore the distribution of Review Ratings and its possible covariates
    - [x] Do in-app purchases significantly affect the apps' ratings, especially for gaming apps?
- [x] Machine Learning Applications
    - [x] Topic Modeling: How do people comment on the quality of apps?
    - [x] Topic Modeling: Are there any different characteristics/topics in new version descriptions for apps that improved/lowered the ratings?
    - [x] Prediction: Can we predict the rating of the app when its new version is released?
- [ ] Presentation & Deployment
    - [x] Blog Post: Discuss our workflow and present it in a digestable way
    - [ ] Build a Web app with Flask(in future)
    
## Teammates
Jiaping(Vincent) Zhang, Wenyu Li, Yaorui Liu, Yuchen Li

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
