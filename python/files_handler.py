try:
    with open("mydata.txt", "r") as f:
        #f.write("Hello World.\n")
        content = f.read()
        print(content)
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("File operation completed.")