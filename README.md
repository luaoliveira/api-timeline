## timeline API

This project creates an API that provides data for visualization. The API receives parameters through the URL and uses them to retrieve information from a database with the parameters used as filters. The response from the API is a json with the data.

#### Technologies

* Python 3.8.10
* Flask
* sqlite
* Marshmallow
* Pytest

#### Setup LINUX

To install all packages required to run the project, run the following command:

```
$ pip install -e .

```

To run this project, run from the parent folder:

```
$ flask run

```

### Routes

The API have two endpoints:

#### /api/info

It shows information about possible filtering (list of attributes and list of values retrieved from the database)

#### /api/timeline

This endpoint shows the data retrieved from the database according to the parameters parsed from the URL. The parameters are validated by Marshmallow library and none of the parameters are set as required. In case no parameters are passed, the API returns all data stored in database grouped by day.