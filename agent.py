#!/usr/bin/env python3
import click
import json
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.exceptions import InvalidSignature

@click.group()
def cli():
    """Student Agent CLI"""
    pass

@cli.command()
@click.argument("request_file")
def accept(request_file):
    """Accept and verify signed request"""
    try:
        with open(request_file, "r") as f:
            data = json.load(f)

        # Extract fields
        message = json.dumps(data["request"]).encode()
        signature = bytes.fromhex(data["signature"])
        pubkey_bytes = bytes.fromhex(data["public_key"])

        # Verify
        pubkey = Ed25519PublicKey.from_public_bytes(pubkey_bytes)
        pubkey.verify(signature, message)

        # Save verified request
        with open("accepted_request.json", "w") as out:
            json.dump(data["request"], out, indent=2)

        click.echo("✅ Request verified and accepted. Saved as accepted_request.json")

    except InvalidSignature:
        click.echo("❌ Invalid signature. Request rejected.")
    except Exception as e:
        click.echo(f"⚠️ Error: {e}")

if __name__ == "__main__":
    cli()
