def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            output = output.replace(f'{{{{{key}}}}}', str(attendee.get(key, "N/A")))

        with open(f'output_{index}.txt', 'w') as file:
            file.write(output)

# Example usage
template_content = """
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
"""

generate_invitations(template_content, attendees)
