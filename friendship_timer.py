from datetime import datetime

# The day we first met
START = datetime(2026, 4, 13, 9, 16, 0)


def main():
    now = datetime.now()
    elapsed = now - START
    print(f"It's been {elapsed} since we first met")
    print()
    print("[Program finished]")


if __name__ == "__main__":
    main()
