## Week 2 (Session1)

### LO
1. Use Python's csv module to read and write flat files
2. Use file handler and context manager to automatically close file handler
3. Produce transformed data by flattening a JSON file into a csv file.

### Session Flow
1. Talk about the importance of flat files in data engineering. Allude to the idea of working with csv and json files while doing ETL tasks. Show some sample csv, json and xml files. Use can use [this json](./data/json_sample.json),[this xml](./data/xml_sample.xml) and [this csv](./data/csv_sample.csv) (~5-10 minutes)
2. Demonstrate how csv files can be read in using the `csv` module. Use the starter code example [here](./codes/session1/flat_files.py)(~30 minutes)
3. Discuss about context managers and  what `with` statement does, elaborate the idea of context managers with an example [here](./codes/session1/context_managers.py) (~30 minutes)
4. Engage the audience with problems similar to the one given [here](./codes/session1/csv_class_practice.md) (~30 minutes)
5. Discuss json file data import and how to parse the json files and fetch specific data from json. Use the file [here](./codes/session1/json_data.py) you can improvise upon it or use similar example. (~10 minutes)
6. Discuss the problem statement given [here](./codes/session1/json_problem.md)(~20 minutes)
7. Discuss the problem given [here](./codes/session1/json_problem1.md)(~20 minutes)
8. Keep (~30 minutes for Q&A and bio breaks)  

### LO
1. Create a basic Python class and write methods for it
2. Create a Python class to read, transform and write data. Make use of __len__, __iter__ methods
3. Use the TDD methodology to write a class that does a simple load, transform, and write operation.

### Session Flow
1. Elaborate on the idea of object oriented programming. Show an existing python-package's source code and make learners focus on the fact that most functionality is written as python classes. You can use [this](https://github.com/python/cpython/blob/main/Lib/csv.py) example, this is the source code of the csv module, make learner focus of `DictWriter` class (line number 133) (~15-20 minutes)
2. Now describe the basic components of a class: constructor, methods, attributes. (~5 minutes)
3. Use the code in [here](./codes/session2/oops1.py) and motivate using an example what happens if write code without packaging it into a class. (~30 minutes)
4. Now show the blueprint of a class using [this](./codes/session2/oops_blueprint.py) file. (~10 minutes)
5. Discuss the idea of attributes in a class using [this](./codes/session2/oops_attrs.py) file. Ask students to include more attributes and check their code. You will also focus on what a constructor is. (~20 minutes)
6. Now use the code [here](./codes/session2/oops2.py) to discuss about the methods in a class. Use this [file](./codes/session2/oops_run.py) to run the code (~20 minutes)
7. Use this [file] to demonstrate how dunder (__method__) methods work. Make students experiment with __len__ method. (~ 10 minutes)
8. Talk about test driven development and how it helps in reducing bugs while developing. (~5 minutes)
9. Refer to the files [etl.py](./codes/session2/etl.py) and [test_etl.py](./codes/session2/test_etl.py). Develop test first and then write class definition. One method has been written as an example you can include more methods and corresponding tests. The end objective is that the learner should be able to understand that first feature has to be thought, then interface has to be fixed, then test has to be defined and finally the code is written. (~ 30 minutes)