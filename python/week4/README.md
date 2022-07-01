## Week 4 

### LO
1. Read data into Pandas DataFrames
2. Detect delimiters in a large corpus of data
3. Handle missing values in raw files
4. Work with columns and index attributes
5. Select a subset of rows and columns using query operator and indexer
6. Sort data by columns
7. Perform the groupby operation to split given data into groups based on criteria.

### Flow
1. Use the [file](./code/pandas1.ipynb) to demonstrate reading data, talk about different file formats supported by pandas. [~10 minutes]
2. To set the context use the [data file](./code/athlete_events.csv) and make people do a simple filter on data using `csv` module. Then show how easy it is to do with pandas. [~30 minutes]
3. Show how indexation across rows and columns work with pandas. Introduce `query` method as an alternate way of filtering the data. [~20 minutes]
4. Now introduce how data can be sorted and then make audience work with the starbucks data problem, this problem is shared in the notebook file whose link has been given in 1. [~20 minutes]
5. Introduce the idea of groupby tasks and demonstrate different variations of `groupby()` and `agg()` methods. [~20 minutes]
6. Use the [class exercise](./code/class_excercise.md) to engage people in discussion. Make learners look at documentation and find out the relevant functions to solve for problem 2 and 3. (~30-45 minutes)
7. Bio breaks [~10 minutes]
8. Q&A [as much as time permits]

### LO 
1. Join data spread across different dataframes using the Pandas library.
2. Work with dates, timestamps and timezones
3. Clean text and use regex within a dataframe
4. Use map and apply functions
5. Create dataframes from nested json files 

### Flow
1. Use the [file](./code/pandas2.ipynb) to develop the context for treating dates as special strings. Demonstrate how `to_datetime()` method works and how relevant information (year, month ,weekday) can be obtained. [~20 minutes]
2. Also touch upon timezones and how to localise a timestamp. Discuss the [`tz_localize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html) and [`tz_convert()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_convert.html) methods. Demonstrate the use of these methods on [stores.csv](./code/stores.csv) file. [~30 minutes]
3. Work on the class exercise on flight delays given in the notebook file [here](./code/pandas2.ipynb)[~30 minutes]
4. Now use the [sample_json.json](./code/sample_json.json) dataset to demonstrate how one can flatten a json file to a dataframe. [~20 minutes]
5. Introduce the notion on `map` and `apply` constructs in a dataframe. Collaboratively work on `comey.csv` dataset (problem statement is in the notebook mentioned in 1) to use the idea of `map`. [~20 minutes]
6. Introduce the idea of joins and show inner, outer, left and right joins. [~10-15 minutes]
7. Make students work on the class exercise on joins given in the notebook [~20-30 minutes]
8. Bio breaks [10 minutes], Q&A[as much as time permits]