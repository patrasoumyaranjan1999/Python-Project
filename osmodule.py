import os

for i in range(0, 10):
    os.rename(f'test/tutorial{i}', f"test/tutorial {i}")
