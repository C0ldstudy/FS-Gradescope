# Files Saving for Gradescope (FS-Gradescope)
FS-Gradescope is a platform including deploying the autograder for students to submit the files from gradescope and a flask server to receive and store the files on the remote server.

## Platform Structure
The flask folder support a server to save files for the remote server.
The autograder folder contains a python file to deploy the autograder. The deploying procedures are introduced on the official [website](https://gradescope-autograders.readthedocs.io/en/latest/specs/).


## Running the sever

```
cd flask
pip install -r requirement.txt
python app.py # three variables are supported: ip_addr, port, debug
```

After the server received the requests, it saves the files under the path `./submission/task_name/task_name-student_name-timestamp/`.

