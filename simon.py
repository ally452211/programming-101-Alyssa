import random

ITEMS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

sequence = []
best_score = 0
playing = True

while playing:

    new_item = random.choice(ITEMS)
    sequence.append(new_item)

    print(f"\n--- Round {len(sequence)} ---")
    print("Watch the sequence carefully!\n")

    for item in sequence:
        print(item, end="  ")
    print("\n")

    input("Press Enter when you're ready to type it back...")
    print()

    failed = False

    for i in range(len(sequence)):
        guess = input(f"Item {i + 1}: ").strip()

        if guess != sequence[i]:
            print(f"\n❌ Wrong! You typed '{guess}' but it should have been '{sequence[i]}'")
            print(f"The full sequence was: {' '.join(sequence)}")
            failed = True
            break

    if not failed:
        print(f"\n✅ Correct! You remembered all {len(sequence)} items!")
        best_score = len(sequence)
        continue

    if len(sequence) > best_score:
        best_score = len(sequence) - 1

    print(f"\nBest round reached this session: {best_score}")
    again = input("\nWould you like to play again? (yes / no): ").strip().lower()

    if again == "yes":
        sequence = []
        print("\nStarting a new game...\n")
    else:
        playing = False
        print("\nThanks for playing! Goodbye ")