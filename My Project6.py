from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup WebDriver (Chrome in this case)
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # STEP 1: Open the Note Taker Page
    print("Opening the Note Taker page...")
    driver.get("https://testpages.eviltester.com/styled/apps/notes/simplenotes.html")

    # Initialize Explicit Wait
    wait = WebDriverWait(driver, 10)

    # STEP 2: Create a New Note
    print("Creating a new note...")

    # Locate 'Title' input and 'Note' textarea fields
    title_input = wait.until(EC.visibility_of_element_located((By.ID, "note-title-input")))
    note_input = wait.until(EC.visibility_of_element_located((By.ID, "note-details-input")))

    # Enter Note Title and Note Content
    note_title = "Meeting Notes"
    note_content = "Discuss project deadlines and team responsibilities."

    title_input.send_keys(note_title)
    note_input.send_keys(note_content)

    # Click the 'Add' button
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "add-note")))
    add_button.click()
    print("Note added successfully.")

    # STEP 3: Display the List of Notes
    print("Displaying the notes list...")
    show_notes_button = wait.until(EC.element_to_be_clickable((By.ID, "show-notes")))
    show_notes_button.click()
    time.sleep(2)  # Wait for the list to display

    # STEP 4: Edit the Note
    print("Editing the note...")
    edit_buttons = driver.find_elements(By.XPATH, "//button[text()='Edit']")
    if edit_buttons:
        edit_buttons[0].click()  # Click the first Edit button
        time.sleep(2)

        # Modify the Note
        title_input = wait.until(EC.visibility_of_element_located((By.ID, "note-title-input")))
        note_input = wait.until(EC.visibility_of_element_located((By.ID, "note-details-input")))

        title_input.clear()
        note_input.clear()
        updated_title = "Updated Meeting Notes"
        updated_content = "Finalize project timelines and task distribution."

        title_input.send_keys(updated_title)
        note_input.send_keys(updated_content)

        # Click the 'Update' button
        update_button = wait.until(EC.element_to_be_clickable((By.ID, "update-note")))
        update_button.click()
        print("Note updated successfully.")

    # STEP 5: Delete the Note
    print("Deleting the note...")
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
    if delete_buttons:
        delete_buttons[0].click()  # Click the first Delete button
        alert = wait.until(EC.alert_is_present())  # Handle confirmation alert
        alert.accept()
        print("Note deleted successfully.")

    # STEP 6: Clear All Notes (Optional)
    print("Clearing all notes...")
    clear_button = wait.until(EC.element_to_be_clickable((By.ID, "clear-notes")))
    clear_button.click()
    alert = wait.until(EC.alert_is_present())
    alert.accept()
    print("All notes cleared.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
