import configparser
import os


def get_packet_location():
    # Check if the configuration file exists
    config_file = 'config.ini'
    if not os.path.exists(config_file):
        # If the configuration file doesn't exist, ask the user for the packet location
        packet_location = input("Enter the packet storage location(absolute location): ")

        # Create the directory if it doesn't exist
        try:
            os.makedirs(packet_location)
        except OSError as e:
            print(f"Error creating directory: {e}")
            exit(1)

        # Create a new configuration file
        config = configparser.ConfigParser()
        config['Capture'] = {'packet_location': packet_location}

        # Write the configuration to the file
        with open(config_file, 'w') as configfile:
            config.write(configfile)
    else:
        # Load the configuration file
        config = configparser.ConfigParser()
        config.read(config_file)

    # Retrieve and return the packet location
    return config.get('Capture', 'packet_location')
