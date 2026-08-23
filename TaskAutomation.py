import re
import os
from datetime import datetime

def extract_emails(input_file):
    """
    Extract email addresses from the input file using regex.
    Returns a list of valid email addresses.
    """
    # Regular expression pattern for email validation
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Find all email addresses in the content
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates while preserving order
        unique_emails = list(dict.fromkeys(emails))
        
        return unique_emails
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return []

def save_emails(emails, output_file):
    """
    Save extracted email addresses to output file.
    Returns True if successful, False otherwise.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write header
            file.write("Extracted Email Addresses\n")
            file.write("-" * 50 + "\n")
            
            # Write timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Extraction Date: {timestamp}\n\n")
            
            # Write emails
            for i, email in enumerate(emails, 1):
                file.write(f"{i}. {email}\n")
            
            # Write summary
            file.write(f"\nTotal emails found: {len(emails)}")
        
        return True
    
    except Exception as e:
        print(f"An error occurred while saving the file: {str(e)}")
        return False

def main():
    print("Email Address Extractor")
    print("=" * 50)
    
    # Get input file path
    while True:
        input_file = input("\nEnter the path to your input text file: ").strip()
        if os.path.exists(input_file):
            break
        print("File not found. Please enter a valid file path.")
    
    # Extract emails
    print("\nExtracting email addresses...")
    emails = extract_emails(input_file)
    
    if not emails:
        print("No email addresses found in the file.")
        return
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"extracted_emails_{timestamp}.txt"
    
    # Save emails
    if save_emails(emails, output_file):
        print(f"\nFound {len(emails)} unique email addresses.")
        print(f"Results have been saved to: {output_file}")
        
        # Preview the first few emails
        print("\nFirst few extracted emails:")
        for i, email in enumerate(emails[:5], 1):
            print(f"{i}. {email}")
        
        if len(emails) > 5:
            print(f"... and {len(emails) - 5} more.")
    else:
        print("Failed to save the results.")

if __name__ == "__main__":
    main()
