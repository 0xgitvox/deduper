"""Minimal example for Deduper."""

from deduper import deduper


def main():
 runner = deduper({"name": "Deduper", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()