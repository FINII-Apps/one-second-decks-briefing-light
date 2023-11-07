import config as config

from pres import Deliverable
from ki import functions as ki_f

# pip3 install playsound==1.2.2
# pip3 install openai python-dotenv python-pptx



if __name__ == "__main__":

    try:

        config_list = []

        with open(f"{config.userfolder_path}config.py", "r") as file:
            lines = file.readlines()

        for line in lines:
            if "=" in line and "ki_request" in line:
                var_name = line.split("=")[0].strip()
                config_list.append(var_name)
                
        anzahl_eintraege = len(config_list)
        print(f"Die Anzahl der Einträge in der Liste beträgt: {anzahl_eintraege}")
        
        for config_variable in config_list:
            exec(f"{config_variable} = ki_f.initOpenAI(config.{config_variable})")

    finally: 
        
        print("KI done")
                
        report = Deliverable.OneSecondDeck(config.output_file, config.output_folder, config.input_file, config.input_folder)

    
# SLIDE 1
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 1 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"Creative Brief", slide, "Titel 1")
        
        #report.insertTextOnSlide(f"Was die App dir abnimmt:\n{content[0]}", slide, "Inhaltsplatzhalter 4")
        
        #report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None


    finally: 
        print(f"#### Slide {slide} done ####")

# SLIDE 2
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 2 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"Produkt: {ki_request_003}", slide, "Titel 1")
        
        content = ki_request_001.splitlines()
        content = [element for element in content if element != '']
        content = [element for element in content if element != ':']
        print(content)
        report.insertTextOnSlide(f"Was das Produkt dir abnimmt:\n{content[0]}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"Wie es das macht:\n{content[1]}", slide, "Inhaltsplatzhalter 2")
        report.insertTextOnSlide(f"Woraus es besteht:\n{content[2]}", slide, "Inhaltsplatzhalter 3")
        
        report.writeNotes(f"Markt:\n{ki_request_007}", slide)
        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None


    finally: 
        print(f"#### Slide {slide} done ####")

# SLIDE 3
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 3 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"Zielgruppe: {ki_request_010}", slide, "Titel 1")
        report.insertTextOnSlide(f"Customer Journey:\n{ki_request_008}", slide, "Inhaltsplatzhalter 2")
        report.insertTextOnSlide(f"Peak Moment of Delight:\n{ki_request_009}", slide, "Inhaltsplatzhalter 3")
        
        report.writeNotes(f"Inspiration: \n{ki_request_002}", slide)
        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None

    finally: 
        print(f"#### Slide {slide} done ####")

# SLIDE 4
    try:
    
        #abschnitte = report_explainer.split('\n\n')

        slide = 4 # Verwendeter Master-Slide: Drei Inhalte
        report.insertTextOnSlide(f"Creative Brief: {ki_request_003}", slide, "Titel 1")
        
        report.insertTextOnSlide(f"Goal of Communication:\n{ki_request_004}", slide, "Inhaltsplatzhalter 4")
        report.insertTextOnSlide(f"Wettbwerbsvorteil:\n{ki_request_005}", slide, "Inhaltsplatzhalter 2")
        report.insertTextOnSlide(f"Brand Positioning:\n{ki_request_006}", slide, "Inhaltsplatzhalter 3")
        
        report.writeNotes(f"Inspiration: \n{ki_request_002}", slide)
        report.insertImageOnSlide(f'{config.img_folder}{config.background_picture}', slide, 'Titel 1', 0, 0, 33.87, 19.05, True) if config.background_fix == 1 else None


    finally: 
        print(f"#### Slide {slide} done ####")

    report.createPres()
