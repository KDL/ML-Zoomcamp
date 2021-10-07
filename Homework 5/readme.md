# Documentation for Week 5
*Ahmed Y. Kallel*

Below are the files, and possible explanation, used during homework week 5.

## Q1: installing pipenv and checking the version
> [homework-5.ipynb](homework-5.ipynb) (Preparation part)

## Q2: Scikit-learn 1.0's hashcode 
> [homework-5.ipynb](homework-5.ipynb) (Preparation part)

## Q3: Local :: Probability of chruning
> [homework-5.ipynb](homework-5.ipynb)

For this, VS Code (Jupyter) was forced to run using the kernel managed by virtual env (pipenv). The Pipfile and Pipfile.lock were later copied from user folder.


> [local_getcust.py](local_getcust.py),

Also, the same experiment was done in a normal python script inside the folder to ensure the same output.

## Q4:: Localhost :: Probability of Churning
> **Client:** [homework-5.ipynb](homework-5.ipynb)
> 
> **Server:** [predict.py](predict.py) (can be launched via launch_server.cmd), served through waitress

Here, a first local server test was done to ensure an intrathread communication. Due to the port 9696 being inaccessible, port 8001 was used instead.


## Q5/Q6 Docker
> **Server:** [Dockerfile](Dockerfile), [output_docker.log](output_docker.log), *served through VirtualBox/Linux Mint*

> **Client:** [homework-5.ipynb](homework-5.ipynb)

Here, I had with Windows very serious problems. It *may be probably linked to Hyper-V not being correctly enabled?*. Eventually and after many trials, I changed to virtualbox VM based on Linux Mint. Installed Docker there and forwarded port 9696 for communication. I also used `ipconfig` to identify the ip address. 

For the output I used:
`sudo docker build -t main . > output_docker.log` to log the output into a log/text file.

~~**<ins>Note</ins>: The output file is not from the last build**~~
