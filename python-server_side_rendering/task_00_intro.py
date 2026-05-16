import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries, each containing attendee details.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print(f"Error: Invalid input type. Template must be a string. Got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type. Attendees must be a list of dictionaries. Got {type(attendees).__name__}.")
        return

    # 2. Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # List of placeholders expected in the template
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        personalized_template = template

        for key in placeholders:
            # Check if key is missing or explicitly assigned None
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Replace placeholder with the value
            personalized_template = personalized_template.replace(f"{{{key}}}", str(value))

        # 4. Generate Output Files
        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(personalized_template)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")