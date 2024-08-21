import aws_cdk as core
import aws_cdk.assertions as assertions

from lambdagrader.lambdagrader_stack import LambdagraderStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambdagrader_cdk/lambdagrader_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdagraderStack(app, "lambdagrader-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
