## Week 1 (Session1)

### LO
1. Use linter support when working in VS code to get suggestions about code quality.
2. Use an appropriate Python data structure to solve a data problem. 
3. Break code into functions and Python scripts to make the code more modular..   
4. Generate Python scripts that support command line arguments.

### Session Flow
1. Use [this link](https://code.visualstudio.com/docs/python/linting) to show students how to add linting support. (10-15 minutes)
2. Use the file [datastructres.py](./codes/session1/datastructures.py) to discuss major python data structures. (~60 minutes)
3. Use the file [datastructures.md](./codes/session1/datastructure.md) to discuss problems based on python datastructures (~60 minutes)
4. Use the file [functions.py](./codes/session1/functions.py) to discuss python functions (~ 20 minutes). Refactor some of the problems discussed above to python functions.
5. Use the file [commandline.py](./codes/session1/commandline.py) to discuss commandline args

Run the file as

```shell
python commandline.py 5
```

Refactor some of the code problems to use commandline args

## Session 2

### LO
1. Use type hints while defining functions.
2. Enable type support in VS Code.
3. Use debugger in VS Code to catch errors and solve them
4. Use a logger to generate log files that can be used for tracking events and troubleshooting problems with the code.  
5. Solve simple data handling problems by writting code that is modular, generates logs and follows a project structure

### Session flow
1. Start the discussion with static and dynamic typing and introduce the challenges in catching type errors for dynamically typed languages (~10 mins)
2. Use the file [typing.py](./codes/session2/typing.py) to demonstrate how type hints help. Show the warning messages on vs code (~ 30 mins)
3. Use the file [typing_rules.py](./codes/session2/typing_rules.py) to discuss typing rules for python types and datastructures. Use [this](https://fastapi.tiangolo.com/python-types/) for context setting and more examples (~ 30 mins)
4. Use the file [debug.py](./codes/session2/debug.py) to discuss debugging and use the article [here](https://python.land/creating-python-programs/python-in-vscode) for context. Give problems to learners to debug. (~ 30-45 mins)
5. Use the file [logs.py](./codes/session2/logs.py) to build intuition about logging (~10-15 mins)
6. Use the file [logs1.py](./codes/session2/logs1.py) to talk about log formats (~5-10 mins)
7. Use the file [logs2.py](./codes/session2/logs2.py) to talk about logging on text files (~5-10 mins)
8. Use the problems from previous lecture to make learners practice type hints, debugging and logging. (Remaining time)