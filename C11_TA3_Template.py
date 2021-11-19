# Import "pygame" module 
import pygame
# Import "time" module
import time
# Initialize "pygame"
pygame.init() 

# Create a game screen and set its title 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing Game")

# Create a variable "carx" to track car position along x-axis and assign initial value a 140
carx = 140
# Create a variable "cary" to track car position along y-axis and assign initial value a 450
cary = 450
# Create a variable "bgy" to track y position of the background and name it as "bgy". Assign the value 0.
bgy = 0

# TA3-Step 1:Create a variable 'threshold' and set to zero.


# Set 'while' loop condition
carryOn = True

# TA2- Step 1: Create first timepoint "t1" here
t1 = time.time()

while carryOn:   
    # NOTE: The images files and .py file in which image is being used must be in same folder
    
    # Display the background image
    baImg_file = "road.png"
    bgImg = pygame.image.load(baImg_file).convert_alpha()
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    screen.blit(bgImg_scaled,(0,0))
    
    # Update the position of yellow car image based on user input and then display it
    # Load the yellow car image and scale it
    yellow_car_file = "yellow_car.png"
    yellow_car = pygame.image.load(yellow_car_file).convert_alpha()
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,(230,150))
    
    # Check for the event type
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False              
    
        # Check if a up, down right, left, enter or spacebar key is pressed on the keyboard. Move the car accordingly.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cary -= 10
                bgy -= 10
            if event.key == pygame.K_DOWN:
                cary += 10
                bgy += 10
            if event.key==pygame.K_RIGHT:
                if carx <= 320:
                    carx += 10
            if event.key==pygame.K_LEFT:
                if carx >= 50:                          
                    carx -= 10   
            if event.key == pygame.K_SPACE:
                if carx < 250:
                    carx += 90
            
            # TA3-Step 2: Allow boosting feature to be used only once in every 10 seconds.
            # Check if user has pressed "ENTER" key on keyboard 

                # Check if "game_time" is greater than and equal to "threshold" 
                # and if "game_time" is less than and equal to "threshold+10"

                    # Decrement "cary" to make car move forward by 50 units

                    # Increment "threshold" by 10

                    print("Car Speed boosted after", game_time, "seconds")
                    
    # Reset car and backgroun positions
    if cary <= 20:
        bgy = 0
        cary = 450 
        
    # Display yellow car image upon updating "carx" and "cary" variable values 
    screen.blit(yellow_car_scaled,(carx, cary))
    
    # TA2- Step 2: Create second time point "t2" here
    t2 = time.time()
    # TA2- Step 3: Evaluate elapsed time t2-t1 and assign it to variable "game_time" and round it off to 2 decimal places
    game_time = t2-t1
    game_time = round(game_time, 2)
    
    # Update the contents of the display
    pygame.display.flip()

# On the occurence of "pygame.QUIT" event close the game screen.
pygame.quit()