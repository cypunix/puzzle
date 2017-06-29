
# Technologies Used:
1. Flask <br />
2. Boto3 <br />
3. Python <br />
4. Bootstrap <br />


# puzzle

Create a new user and assign the following policy:
https://github.com/cypunix/puzzle/blob/master/aws_policy

Build an image using the following Docker file:
wget https://github.com/cypunix/puzzle/blob/master/Dockerfile

Build an image:
docker build -t {tag_of_image} .

Run the docker image:
docker run -it --rm --name webapp -p 80:5000 -e AWS_ACCESS_KEY_ID=abc -e AWS_SECRET_ACCESS_KEY=xyz webapp2 python finalcode.py

AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are the keys acquired from AWS newly created user.

Source code available at:
https://github.com/cypunix/puzzle


Enjoy.
Michal Stepinski
