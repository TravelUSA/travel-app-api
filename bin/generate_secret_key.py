#!/usr/bin/env python

"""Generate a SECRET_KEY suitable for use in Django."""

from shlex import quote

from django.core.management.utils import get_random_secret_key


def main():
    """Print out the generated secret key in an .env-friendly format"""
    print(f"SECRET_KEY={quote(get_random_secret_key())}")


if __name__ == "__main__":
    main()
