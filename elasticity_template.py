import pygame
import pymunk
import pymunk.pygame_util

def create_ball(space, position, elasticity):
  #write the code to create ball object
def create_floor(space):
    """Creates a static floor for the balls to bounce on."""
    floor = pymunk.Segment(space.static_body, (50, 500), (750, 500), 5)
    floor.elasticity = 1.0  # Maximum bounce
    space.add(floor)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Elasticity Demo")
    clock = pygame.time.Clock()

    #create pymunk space
    

    #gravity to pull downward
    
    

    #Update physics simulation
    
    
    # Create a floor
    create_floor(space)

    # Create balls with different elasticity
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update physics simulation
        
        
        # Draw objects
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
