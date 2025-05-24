with open("5_logfile.txt", "r") as f:
    content = f.read()

if "python" in content.lower():
    print("Yes, 'python' is present.")
else:
    print("No, 'python' not found.")
