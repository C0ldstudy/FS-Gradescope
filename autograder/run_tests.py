import requests
import json
from os import listdir
from os.path import isfile, join, splitext
import os

if __name__ == '__main__':
    onlyfiles = [f for f in listdir('/autograder/source') if isfile(join('/autograder/source', f))]
    mypath = '/autograder/source/'
    filename = None
    with open('/autograder/submission_metadata.json', 'r') as f:
        meta_data = json.load(f)['users']
    name = ''
    for member in meta_data:
        name += member['name'].replace(" ", "")

    # parameters that need to be updated
    task_name = "task_name"
    ip_addr = "127.0.0.1"
    port = "5000"

    temp = {"task": task_name, "student_name": str(name)}
    files = os.listdir('/autograder/submission/')
    # assume all the files are in the one folder
    if (len(files) == 1) and (os.path.isdir(files[0])):
        second_files = os.listdir('/autograder/submission/'+files[0])
        paths = []
        for second_file in second_files:
            paths.append((second_file, open('/autograder/submission/'+files[0]+'/'+second_file, mode="rb")))

        if len(paths)<1:
            print("ERROR! Please check the submission requirements!")
            with open('/autograder/results/results.json', 'w') as f:
                output = {"output": "ERROR! Please check the submission requirements!", "stdout_visibility": "visible"}
                f.write(json.dumps(output))
            exit()
        paths.append(("submission_metadata.json", open('/autograder/submission_metadata.json', 'r')))
        # update the 127.0.0.1 to the real ip address
        response = requests.post(url='http://'+ip_addr+'/save_files', files=paths, data=temp)
    # assume the all files are on the root path
    # if len(files) > 1:
    else:
        second_files = os.listdir('/autograder/submission/')
        paths = []
        for second_file in second_files:
            paths.append((second_file, open('/autograder/submission/'+second_file, mode="rb")))
        if len(paths)<1:
            with open('/autograder/results/results.json', 'w') as f:
                output = {"output": "ERROR! Please check the submission requirements!", "stdout_visibility": "visible"}
                f.write(json.dumps(output))
            exit()

        paths.append(("submission_metadata.json", open('/autograder/submission_metadata.json', 'r')))
        response = requests.post(url='http://'+ip_addr+':'+port+'/save_files', files=paths, data=temp)


    # set the score of the gradescope
    with open('/autograder/results/results.json', 'w') as f:
        temp = json.loads(response.text)
        output = {"score": 100, "output": temp['feedback'],"stdout_visibility": "visible"}
        # print(output)
        f.write(json.dumps(output))
