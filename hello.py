import os, sys, time

def main():
    print("Hello from uv-test!")
    current_dir = os.getcwd()
    if os.path.exists(current_dir):
        print("Current directory: " + current_dir)
    else:
        print("Current directory not found")
        
    for i in range(5):
        time.sleep(1)
        if not i == 0:
            print(f"{i} seconds elapsed")
        if i == 3:
            break


if __name__ == "__main__":
    main()
