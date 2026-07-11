from ai.services.chunking_service import ChunkingService

text = "A" * 3500

chunks = ChunkingService.split_text(text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"Chunk {i}: {len(chunk)} characters")