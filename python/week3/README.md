## Week 3 

### LO
1. Use anchors and metacharacters to create regex patterns that help search through text.
2. Use  quantifiers to repeat a pattern for specifying the number of occurrences to match in a text.
3. Use lookahead to define complex patterns
4. Write simple patterns such as email, website, address (format defined) validators

### Session Flow

1. Spend time introducing the motivation for learning regex, ask people to write a program to find email addresses from a document containing many of them. [10-15 minutes]
2. Now start with the idea of regular expressions. Use the notebook [here](./code/regex.ipynb) to drive the class. Start with the idea of simple patterns. Introduce the notion of creating a pattern and then finding it within the text. [~30 minutes]
3. Now introduce them to metacharacters such as `\d`,`[a-zA-Z0-9]` etc. Use problems such as the ones given [here](./code/regex_problems.md). Also introduce the notion of `+,$,^,{}` to control the number of times a pattern is repeated [~45 minutes]
4. Talk about lookahead and lookbehind expressions. Use [this](https://queirozf.com/entries/python-regular-expressions-lookahead-and-lookbehind-examples) as a reference. [~30 minutes]
5. Discuss problems involving creating regex to parse html markup, email ids, patterns in log files (time stamps, url, user-agents) [~30 minutes] 
6. Bio Breaks [~10 minutes]
7. Q&A [~20 minutes]

### LO
1. Doing api calls using the requests package
2. Parse an API response to restructure the resultant data in an analysis-friendly format. 
3. Use authentication tokens to authorize access to an API
5. Use multiprocessing to speed up multiple file manipulations for CPU-intensive tasks.

### Flow
1. Introduce api as a common data-source. Use [this](https://api.chucknorris.io) to introduce the idea of idea of endpoints and request methods. [~15 minutes]
2. Use the file [here](./code/api1.py) to demonstrate the access to an api endpoint using `requests` library. [~10 minutes]
3. Now make the students access random jokes from category details fetched in 2 above by reading the documentation.[sample here](./code/api2.py) [~10 minutes]
4. Lead a class discussion on how to access as much data as is possible using the endpoints given in the docs. Make the learners develop their own code to access data. Write a class to write non-duplicated data as a csv file, there should be logic to log application status etc. [sample solution here](./code/api3.py)[~30-45 minutes]
5. Discuss how sometimes api data can be behind a paywall and now api keys are used to address this issue. Have students generate a developer key [here](https://developer.nytimes.com). Create an environment variable to set the key. Instructor must be prepared with process to set environment variables both on linux and windows. [~20 minutes]
6. Now access one endpoint use the code template provided [here](./code/api4.py)[~10 minutes]
7. Ask students to explore other endpoints and gather data [~20 minutes]
8. Introduce the ideas of pools, locks and multiprocessing using [this](./code/multiprocessing.md) file. [~30 minutes]
9. Optional, show basic multithreaded code.