FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt .

RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY example_docker_lambda.py .

CMD ["example_docker_lambda.handler"]
