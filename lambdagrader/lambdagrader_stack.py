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

        # Define the Lambda function resource
        my_function = _lambda.Function(
            self, "IntroFunction", 
            runtime = _lambda.Runtime.PYTHON_3_12,
            handler = "lambda-handler.main",
            # code = _lambda.Code.from_inline(
            #     """
            #     exports.handler = async function(event) {
            #     return {
            #         statusCode: 200,
            #         body: JSON.stringify('Hello World!'),
            #     };
            #     };
            #     """
            # ),
            code = _lambda.Code.from_asset('./lambdagrader/functions'),
        )

        # Define the Lambda function URL resource
        my_function_url = my_function.add_function_url(
        auth_type = _lambda.FunctionUrlAuthType.NONE,
        )

        # Define a CloudFormation output for your URL
        CfnOutput(self, "myFunctionUrlOutput", value=my_function_url.url)
