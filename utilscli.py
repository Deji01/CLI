#!/usr/bin/env python
import click
import mlib
import requests

@click.group()
@click.version_option("1.0")
def cli():
    """"Machine learning utility belt"""

@cli.command("retrain")
@click.option("--tsize", default=0.1, help="Test size")
@click.option("--model_name", default="model.joblib", help="Model Name")

def retrain(tsize, model_name):
    """Retrain model
    """
    click.echo(click.style("Retraining Model", bg="green", fg="white"))
    accuracy, name = mlib.retrain(tsize, model_name)
    click.echo(
        click.style(f"Retrained Model Accuracy: {accuracy}", bg="blue", fg="white")
    )
    click.echo(
        click.style(f"Retrained Model Name: {name}", bg="red", fg="white")
    )

@cli.command("predict")
@click.option("--weight", default=225, help="Weight to pass in")
@click.option("--host", default="http://localhost:8080/predict", help="Host to query")

def mkrequest(weight, host):
    """Sends prediction to ML endpoint"""

    click.echo(
        click.style(f"Querying host {host} with weight: {weight}", bg="green", fg="white")
    )
    payload = {"Weight":weight}
    result = requests.post(url=host, json=payload)
    click.echo(
        click.style(f"result: {result.text}", bg="red", fg="white")
    )

if __name__ == "___main__":
    cli()