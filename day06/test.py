full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("venkatram   ", "   veerareddy"))

scifi_authors = [
    "Isaac Asimov", "Ray Bradbury", "Robert Heinlien", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wels", "Leigh Brackett"
]

scifi_authors.sort(key=lambda name: name.split(" ")[-1])

print(scifi_authors)