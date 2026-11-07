from dotenv import load_dotenv
from mem0 import Memory

load_dotenv()

config = {
    # 1) Fact NIKAALNE ke liye kaunsa LLM
    "llm": {
        "provider": "openai",
        "config": {"model": "gpt-4.1-mini"},
    },
    # 2) Yaadon ko NUMBERS (embedding) me badalne ke liye
    "embedder": {
        "provider": "openai",
        "config": {"model": "text-embedding-3-small"},
    },
    # 3) Save KAHAN hoga — apna purana dost Qdrant!
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "collection_name": "agent_memories",
        },
    },
}

m = Memory.from_config(config)   # apni marzi ki settings wala Memory

m.add("Main Nagpur me rehta hoon aur mujhe cricket dekhna pasand hai",
      user_id="piyush")

print(m.search("User kahan rehta hai?", filters={"user_id": "piyush"}))

# Ek user ki SAARI yaadein dekhni hon toh:
print(m.get_all(filters={"user_id": "piyush"}))