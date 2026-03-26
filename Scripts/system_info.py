import platform
import psutil

print("=== SYSTEM INFORMATION ===")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Processor: {platform.processor()}")

print("\n=== CPU USAGE ===")
print(f"CPU Usage: {psutil.cpu_percent()}%")

print("\n=== MEMORY USAGE ===")
memory = psutil.virtual_memory()
print(f"Total: {memory.total}")
print(f"Available: {memory.available}")
print(f"Used: {memory.used}")