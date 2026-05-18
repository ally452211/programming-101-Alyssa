invited = set({"Alyssa", "sir henry the third", "daniel", "yoyo","terrance","Young sheldon","Mr beast"})
showed_up = set({"Alyssa", "daniel", "yoyo","terrance","bob","donald trump","karen",})

no_show = invited - showed_up
crashed = showed_up - invited

print(f"lets see who showed up: {' '.join(showed_up)}")

for person in no_show:
    print(f"{person} didn't show up")

for person in crashed:
    print(f"{person} crashed the party ")

print("what a mess")