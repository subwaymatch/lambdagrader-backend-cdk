cdk synth
sam build -t ./cdk.out/LambdagraderStack.template.json
sam local invoke -t ./cdk.out/LambdagraderStack.template.json ExampleDockerFunction