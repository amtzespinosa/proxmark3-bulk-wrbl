import subprocess

# Command to write a specific block with a specific key
def write_block(block_data, key, block_number):
    command = f'hf mf wrbl {block_number} A {key} {block_data}'
    subprocess.run(['proxmark3', '-c', command], check=True, capture_output=True, text=True)

# Sample data
blocks_to_write = [
    {'block_data': '1122334455667788', 'key': 'FFFFFFFFFFFF', 'block_number': 16},
    {'block_data': 'AABBCCDDEEFF0011', 'key': '000000000000', 'block_number': 18},
    # Add blocks as needed
]

# Write blocks with the possibility of excluding some
excluded_blocks = [17, 20]  # Add here the blocks you want to excluse 

for block in blocks_to_write:
    if block['block_number'] not in excluded_blocks:
        write_block(block['block_data'], block['key'], block['block_number'])
