import argparse
from app.notes import add_note, list_notes, find_notes, delete_note

def main():
    parser = argparse.ArgumentParser(description="Team Notes CLI")
    subparsers = parser.add_subparsers(dest="command")

    # comando add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("body")

    # comando list
    list_parser = subparsers.add_parser("list")

    # comando search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")

    # comando delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id")

    # procesar argumentos
    args = parser.parse_args()

    if args.command == "add":
        note = add_note(args.title, args.body)
        print(f"Nota creada con ID: {note['id']}")

    elif args.command == "list":
        notes = list_notes()
        for n in notes:
            print(f"{n['id']} - {n['title']}: {n['body']}")

    elif args.command == "search":
        results = find_notes(args.query)
        for n in results:
            print(f"{n['id']} - {n['title']}: {n['body']}")

    elif args.command == "delete":
        success = delete_note(args.id)
        if success:
            print(f"Nota {args.id} eliminada.")
        else:
            print(f"No se encontró la nota con ID {args.id}.")

if __name__ == "__main__":
    main()  