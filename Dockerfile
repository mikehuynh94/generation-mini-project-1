FROM python:3.9

WORKDIR /project

# Copy everything from our project root into our WORK DIRECTORY directory
COPY . ./

EXPOSE 80

ENTRYPOINT ["python", "./my_project_w1.py"]