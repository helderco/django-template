#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # Load environment
    import dotenv
    dotenv.read_dotenv()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
