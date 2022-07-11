## Week 1 (Session1)

### LO
1. Create a github account and learn to push code to repo
2. Make branches and push code to different branches
3. Merge code with main branch from a development branch
4. Use linter support when working in VS code to get suggestions about code quality.
5. Use an appropriate Python data structure to solve a data problem. 


### Session Flow
1. Spend time talking about version control and why is it necessary (~5 minutes)
2. Show using github desktop client how to initialize a repo, create branches and push code to the respective branches (~30 minutes)
2. Use [this link](https://code.visualstudio.com/docs/python/linting) to show students how to add linting support. (10-15 minutes)
3. Use the file [datastructres.py](./codes/session1/datastructures.py) to discuss major python data structures. (~60 minutes)
4. Use the file [datastructures.md](./codes/session1/datastructure.md) to discuss problems based on python datastructures (~60 minutes)

## Session 2

### LO
1. Break code into functions and Python scripts to make the code more modular..   
2. Generate Python scripts that support command line arguments.
3. Use type hints while defining functions.
4. Enable type support in VS Code.
5. Use debugger in VS Code to catch errors and solve them
6. Use a logger to generate log files that can be used for tracking events and troubleshooting problems with the code.  
7. Solve simple data handling problems by writting code that is modular, generates logs and follows a project structure"

### Session flow
1. Use the file [functions.py](./codes/session1/functions.py) to discuss python functions (~ 10 minutes). Refactor some of the problems discussed above to python functions.
2. Use the file [commandline.py](./codes/session1/commandline.py) to discuss commandline args

Run the file as

```shell
python commandline.py 5
```

Refactor some of the code problems discussed in first session, to use commandline args
3. Start the discussion with static and dynamic typing and introduce the challenges in catching type errors for dynamically typed languages (~10 mins)
4. Use the file [typing.py](./codes/session2/typing.py) to demonstrate how type hints help. Show the warning messages on vs code (~ 30 mins)
5. Use the file [typing_rules.py](./codes/session2/typing_rules.py) to discuss typing rules for python types and datastructures. Use [this](https://fastapi.tiangolo.com/python-types/) for context setting and more examples (~ 30 mins)
6. Use the file [debug.py](./codes/session2/debug.py) to discuss debugging and use the article [here](https://python.land/creating-python-programs/python-in-vscode) for context. Give problems to learners to debug. (~ 30-45 mins)
7. Use the file [logs.py](./codes/session2/logs.py) to build intuition about logging (~10-15 mins)
8. Use the file [logs1.py](./codes/session2/logs1.py) to talk about log formats (~5-10 mins)
9. Use the file [logs2.py](./codes/session2/logs2.py) to talk about logging on text files (~5-10 mins)
10. Use the problems from previous lecture to make learners practice type hints, debugging and logging. (Remaining time)