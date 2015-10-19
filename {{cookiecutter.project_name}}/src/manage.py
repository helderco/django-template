#!/usr/bin/env python
import sys

if __name__ == "__main__":
    # Load environment variables
    from unipath import Path
    BASE_DIR = Path(__file__).absolute().ancestor(2)
    try:
        import dotenv
        env_file = BASE_DIR.child('.env')
        if env_file.exists():
            dotenv.read_dotenv(env_file)
    except ImportError:
        pass

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
