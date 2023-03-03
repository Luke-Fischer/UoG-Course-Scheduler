## Overview
I built this web app with 5 other students at the University of Guelph. This is a scheduling web app for university of guelph courses. It provides users with a clean UX to view and select UoG classes as well as some unique auto course selecting features. My primary contribution to this project was designing, implementing and quering the PSQL database as well as some minor testing using pytest. 


Figma UX Design URL: https://www.figma.com/file/qZglav2OeAa6JItNeaTvld/Main?node-id=0%3A1

## Dev Setup
- Ensure that npm is installed locally
- Ensure that python3 is installed locally
- Install local vue dependencies, run `cd vue` then `npm install`
- Install local python modules, run `cd flask` then `pip3 install -r requirements.txt`
- Generate a local SSC, run `cd flask` then `openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out server.crt -keyout server.key` (Set the Common Name field to localhost)

## Dev Environments
- To launch nginx, run `docker compose up --build`. The server is located at [https://localhost](https://localhost)
- To close nginx, press CTRL+C in terminal, then run `docker compose down -v`
- To launch the vue dev server, run `cd vue` then `npm run serve`
- To launch the flask dev server, run `cd flask` then `python3 ./app.py`

## SSL Setup

- Run `sudo certbot certonly --manual --manual-auth-hook /etc/letsencrypt/acme-dns-auth.py --preferred-challenges dns --debug-challenges -d uog-course-scheduler.page` and follow the given steps
- Copy the new crt and key files to aws with `scp -i "Course Scheduler Key.pem" ./server.crt ec2-user@ec2-18-222-134-0.us-east-2.compute.amazonaws.com:~/cis3760/flask/server.crt` and `scp -i "Course Scheduler Key.pem" ./server.key ec2-user@ec2-18-222-134-0.us-east-2.compute.amazonaws.com:~/cis3760/flask/server.key`

## Testing
- Download and install pytest: `sudo apt install python-pytest`
- Run using: `cd flask` then `pytest`
