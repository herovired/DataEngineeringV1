## Week 5

### LO
1. Explain why numpy manipulations can be more performant than Pandas
2. Perform basic of NumPy indexation functions (row, col selection)
3. Perform arithematic operations on NumPy arrays
4. Work with axis parameter to implement row-wise and column-wise operations.
5. Perform basic operations such as reading and writting flat files using NumPy
6. Describe the basics of NumPy broadcasting.
7. Perform broadcasting horizontally, vertically and both ways


### Flow
1. Use the file [numpy_pandas_speed.ipynb](./codes/numpy_pandas_speed.ipynb) to discuss under which circumstances numpy code can be faster compared to pandas. (~5-10 minutes)
2. Use the file [numpy_ops.ipynb](./codes/numpy_ops.ipynb) to discuss file IO. Focus on how reading data directly using numpy can be cumbersome but writing as .npz file can save space (~20 minutes)
3. Use the class exercise mentioned on fetching data and saving it in `npz` format given  in the notebook mentioned above. The solution is [here](./codes/class_excercise/solution_class_excercise.ipynb)(~15-20 minutes)
4. Now demonstrate the idea of indexation. Demonstrate boolean indexation. Use [slicing and indexing](./codes/Slicing%20and%20indexing.ipynb) and [numpy ops](./codes/numpy_ops.ipynb) to discuss indexation in numpy [~10-15 minutes]
5. Now discuss the contents of [array concatenation](./codes/array_concat.ipynb) and [array_sorting](./codes/array_sort.ipynb)[~15-20 minutes]
6. Use [numpy broadcasting](./codes/numpy_broadcasting.md) to discuss the idea of broadcasting. [~30 minutes]

### LO
1. Use SQLAlchemy to define tables in a database
2. Establish relationships and constraints on tables in a database using SQL Alchemy
3. Push data into a database using SQL Alchemy

### Flow
1. Use the file [SQL_Python_Connectivity.ipynb](./codes/SQL_Python_Connectivity.ipynb) as the main file to drive the session. Show the benefits of pulling data from a db to python can be helpful (pull data to a dataframe and show some plotting examples)[~10-15 minutes]
2. Show how to query data from a table, all the table names from a db using sqlalchemy.[~10-20 minutes]
3. Use the dataset [films.db](./codes/data/films.db) to make students pull data into sql. Spend time giving students enough practice. [~30 minutes]
4. Next, demonstrate how to load data into a database, use [SQL_Python_Connectivity.ipynb](./codes/SQL_Python_Connectivity.ipynb) to show data dump. (~30 minutes)
5. Use the [pset1](./codes/class_excercise/Pset1.docx) as a class exercise. The solution file is [here](./codes/class_excercise/Pset1.ipynb). (~30-45 minutes)
