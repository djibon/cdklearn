#!/usr/bin/env python3

from aws_cdk import core

from eksproject.eksproject_stack import EksprojectStack


app = core.App()
EksprojectStack(app, "eksproject")

app.synth()
