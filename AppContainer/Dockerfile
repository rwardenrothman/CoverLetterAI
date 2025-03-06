FROM public.ecr.aws/lambda/python:3.12

# Install the function's dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}" -U --no-cache-dir

# Copy function code
COPY /app ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["app.handler"]