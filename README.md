
# Technologies Used:
1. Flask <br />
2. Boto3 <br />
3. Python <br />


# puzzle

Create a new user and assign the following policy:
https://github.com/cypunix/puzzle/blob/master/aws_policy

Docker file:
https://github.com/cypunix/puzzle/blob/master/Dockerfile

Source code available at:
https://github.com/cypunix/puzzle

How to:

git clone https://github.com/cypunix/puzzle
cd puzzle/
#Build an image:
docker build -t {tag_of_image} .

Run the docker image:
docker run -it --rm --name webapp -p 80:5000 -e AWS_ACCESS_KEY_ID=abc -e AWS_SECRET_ACCESS_KEY=xyz {tag_of_image} python finalcode.py

<p>Run a test run on different port with debugging on</p>
docker run -it --rm --name webapp -p 80:4444 -e AWS_ACCESS_KEY_ID=abc -e AWS_SECRET_ACCESS_KEY=xyz {tag_of_image} python finalcode.py --test

<p>The keys that needs to be fetched from AWS</p>
AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are the keys acquired from AWS newly created user.


Enjoy.
M.Stepinski
