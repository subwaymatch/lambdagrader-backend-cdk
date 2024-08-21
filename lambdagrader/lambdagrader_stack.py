from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    CfnOutput,
)
from constructs import Construct

class LambdagraderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.build_container_example()

        # Define the Lambda function resource
        my_function = _lambda.Function(
            self, "IntroFunction", 
            runtime = _lambda.Runtime.PYTHON_3_12,
            handler = "lambda-handler.main",
            code = _lambda.Code.from_asset('./lambdagrader/functions/hello-world'),
        )

        # Define the Lambda function URL resource
        my_function_url = my_function.add_function_url(
            auth_type = _lambda.FunctionUrlAuthType.NONE,
        )

        # Define a CloudFormation output for your URL
        CfnOutput(self, "myFunctionUrlOutput", value=my_function_url.url)

    def build_container_example(self):
        self.docker_lambda = _lambda.DockerImageFunction(
            scope=self,
            id="ExampleDockerFunction",
            # Function name on AWS
            function_name="ExampleDockerFunction",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=_lambda.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile
                directory="./lambdagrader/functions/example-docker"
            ),
        )