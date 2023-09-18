#!/bin/bash
# install docker
sudo yum install docker -y
# start and enable docker on restart
sudo systemctl start docker
sudo systemctl enable docker
# pull the app docker image from dockerhub repo
sudo docker pull ellaangel/python-flask-subnet-calculator:version-1.0.1
# run app on port 80 (make sure sg is updated with inbound rule for the ec2 instance)
sudo docker run -p 80:5000 ellaangel/python-flask-subnet-calculator:version-1.0.1
