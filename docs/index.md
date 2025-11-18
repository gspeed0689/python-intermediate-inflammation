# Inflam

Inflam is a Python library to manage and analyze inflammation data. 

## Introduction

Inflam leverages numpy to calculate statistics on inflammation data, matplotlib to create graphs to visually understand that data.

It is not to be confused with Inflan, a recipe management system for variations on ways of cooking flan. 

### Features

- Example data
- At least a few python methods
- No mayonaise
- numpy is our base

## Installation

You can install inflam with pip using the git+https url, in the future the package will be available on pypi

    git+https://github.com/gspeed0689/python-intermediate-inflammation.git

## Usage

    from inflam import inflammation_analysis
    import numpy as np

    # load csvs
    data = inflammation_analysis.readcsv("/your/data/path.csv")

    # analyze data
    for method in [np.mean, np.median, np.max, np.min, np.std]:
        inflammation_analysis.daily_statistic(data, method)

## Contributing

If you want to contribute, please don't. If you must, you mustn't 

We are structuring the repository with the MVC architecture, all new features must have 115% (you must make new tests for things we haven't made tests for, again, don't contribute) of pytest code coverage. 

## Citation

    cff-version: 1.2.0
    message: "If you use this software, don't this is for an intermediate python programming class from the Netherlands eScience Center."
    authors: 
     - family-names: Professionales
       given-names: Programmer
       orcid: https://orcid.org/1234-5678-9101-1121
    title: "Inflam"
    version: 1.2.3
    date-released: 2025-11-18 