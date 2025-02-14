from aws_cdk import(
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from hitcounter import HitCounter
from cdk_dynamo_table_viewer import TableViewer

class EksprojectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        my_lambda = _lambda.Function(
            self, "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code   =_lambda.Code.asset('lambda'),
            handler="hello.handler"
        )

        hello_with_counter = HitCounter(
            self, "HelloHitCounter",
            downstream=my_lambda
        )
        
        apigw.LambdaRestApi(
            self, "Endpoint",
            handler=hello_with_counter.handler
        )

        
        TableViewer(
            self, "ViewHitCounter",
            title="Hello Hits",
            sort_by="-hits",
            table=hello_with_counter.table
        )
