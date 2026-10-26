import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4")
text = "Hello, how are you? Harsh"
encoded_text = encoder.encode(text)
print(f"Encoded text: {encoded_text}")

decoded_text = encoder.decode(encoded_text)
print(f"Decoded text: {decoded_text}")