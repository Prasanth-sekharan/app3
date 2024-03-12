import os

def main():
    # Get the value of the MESSAGE environment variable
    message = os.environ.get('APP_NAME', 'Default APP!')

    # Print the message
    print(message)

if __name__ == "__main__":
    main()

