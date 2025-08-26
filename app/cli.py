import argparse
from app.notes import add_note

def main():
    parser = argparse.ArgumentParser(description="Team Notes CLI")
    subparsers = parser.add_subparsers(dest="command")

    # comando add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("body")

    args = parser.parse_args()

    if args.command == "add":
        note = add_note(args.title, args.body)
        print(f"Nota creada con ID: {note['id']}")

if __name__ == "__main__":
    main()