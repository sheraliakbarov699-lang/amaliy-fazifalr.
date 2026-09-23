import argparse


def start(args):
    print(f"Xizmat ishga tushirilmoqda... (port: {args.port})")


def stop(args):
    print("Xizmat to'xtatilmoqda...")


def main():
    parser = argparse.ArgumentParser(description="Oddiy CLI boshqaruv skripti")
    subparsers = parser.add_subparsers(dest="command", required=True)

    start_parser = subparsers.add_parser("start", help="Xizmatni ishga tushirish")
    start_parser.add_argument("--port", type=int, default=8000, help="Port raqami")
    start_parser.set_defaults(func=start)

    stop_parser = subparsers.add_parser("stop", help="Xizmatni to'xtatish")
    stop_parser.set_defaults(func=stop)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
