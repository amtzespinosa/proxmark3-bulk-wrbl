import subprocess

# Command to write a specific block with a specific key
def write_block(block_data, key, block_number):
	init = "./proxmark3 /dev/ttyACM0 -c "
	write = "'hf mf wrbl '" + f"'--blk {block_number} -k {key} -d {block_data}'"
	command = init + write
	
	result = subprocess.run(command, shell=True, capture_output=True, text=True)
	print(result.stdout) # Just for checking

# Sample data
blocks_to_write = [
    {'block_data': '11223344556677881122334455667788', 'key': 'FFFFFFFFFFFF', 'block_number': 16},
    {'block_data': 'AABBCCDDEEFF0011AABBCCDDEEFF0011', 'key': '000000000000', 'block_number': 18},
	# Add blocks as needed
]

for block in blocks_to_write:
	write_block(block['block_data'], block['key'], block['block_number'])
