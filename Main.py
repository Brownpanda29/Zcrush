import io
import zipfile

# Define the non-breaking space character
non_breaking_space = '\u00A0'

# Function to generate data in chunks
def generate_data_chunk(chunk_size):
    for _ in range(chunk_size):
        # Generate data by repeating the non-breaking space character 10 million times
        data = non_breaking_space * (10_000_000)
        yield data

# Create an in-memory buffer to hold the compressed data
buffer = io.BytesIO()

# Create a zip file in memory
with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
    # Batch processing: Process 10 data items at a time
    batch_size = 10
    num_batches = 10

    for batch_num in range(num_batches):
        print(f"Processing batch {batch_num + 1}/{num_batches}...")

        # Generate data in chunks
        chunk_size = 10_000  # Process 10,000 chunks per batch
        for chunk in generate_data_chunk(chunk_size):
            # Write data to zip file
            zipf.writestr(f'data_{batch_num * chunk_size + chunk_num}.txt', chunk)

# Get the compressed data as bytes
compressed_data = buffer.getvalue()

# Write the compressed data to a file named data.rar
with open('data.rar', 'wb') as f:
    f.write(compressed_data)

print("Compression complete. 'data.rar' file created.")
      
