# Subnet Calculator Web Application

This repository contains a Flask-based web application that provides a user interface for IP address validation and subnet calculation.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation and Usage](#installation-and-usage)
  * [Using Docker](#using-docker)
  * [Deploying to AWS EC2 using User Data](#deploying-to-aws-ec2-using-user-data)

## Features

- Validate an IP address.
- Determine the class of the IP address.
- Calculate the subnet mask and the number of possible subnets based on the IP's class and optionally provided CIDR.

## Prerequisites

- Docker
- AWS account (if deploying to EC2)

## Installation and Usage

### Using Docker

1. **Pulling the Docker Image**:

```bash
   docker pull ellaangel/python-flask-subnet-calculator:latest
```
2. **Run the Application**
  ```bash
   docker run -p 5000:5000 ellaangel/python-flask-subnet-calculator:latest
  ``` 
### **AWS EC2 User Data Script Method**:
   1. Start the process to launch a new EC2 instance.
   2. Under **Advanced Details** in the EC2 launch wizard, paste the following User Data script. This script will automatically deploy the Docker container when the instance starts:

```bash
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
```
