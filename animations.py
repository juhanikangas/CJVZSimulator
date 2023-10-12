import time
import sys
import os
import random
from pynput import keyboard
from questions import questions

questions_score = 0
# Grid (Game Window) Configuration
grid_height = 20
grid_width = 20

# Player Configuration and State Variables
player = "✈️"
exploded = "💥"
player_alive = True
health = 100
default_health = health
x = int(grid_width / 2)
y = int(grid_height - 2)
frame_duration = 0

# Plane Speed Management
plane_speed = 0
plane_max_speed = 100
accelerating = True
braking = False

# Game Loop and State Management
game = True
frame = 0
frame_delay = 0.1

# Player Movement Constraints and Flags
y_limit = 0
smooth = 0
lock_player_on_press = False

# Entity Management
entities = []
stop_entity_spawn = False
elapsed_frames = 0

def flight(flight_specs):
    global grid_height, grid_width, player, exploded, player_alive, health, default_health, x, y, plane_speed, plane_max_speed, accelerating, braking, game, frame, frame_delay, y_limit, lock_player_on_press, entities, stop_entity_spawn, elapsed_frames, smooth, frame_duration, questions_score
    flight_time = flight_specs["flight_duration"] / frame_delay
    health = flight_specs["user_plane"].hp
    default_health = health
    player = "✈️"

    frame_duration = 0
    player_alive = True
    x = int(grid_width / 2)
    y = int(grid_height - 2)

    # Plane Speed Management
    plane_speed = 0
    plane_max_speed = 100
    accelerating = True
    braking = False

    # Game Loop and State Management
    game = True
    frame = 0
    frame_delay = 0.1

    # Player Movement Constraints and Flags
    y_limit = 0
    smooth = 0
    lock_player_on_press = False

    # Entity Management
    entities = []
    stop_entity_spawn = False
    elapsed_frames = 0

    class Entity:
        def __init__(self, e, x_off, y_off):
            self.e = e
            self.x_off = x_off
            self.y_off = y_off


    class GameEntity:
        def __init__(self, enemy, x_pos, speed, damage):
            self.enemy = enemy
            self.speed = speed
            self.x_pos = x_pos
            self._y_pos = 0
            self.damage = damage

        def __iter__(self):
            # Return an iterable containing the attributes to unpack
            return iter([self.x_pos, self._y_pos, self.enemy, self.speed, self.damage])

        @property
        def y_pos(self):
            return self._y_pos

        @y_pos.setter
        def y_pos(self, new_y_pos):
            self._y_pos = new_y_pos


    birds = {
        "e": [Entity("🦅", 0, 0),
              Entity("🦅", -1, -1),
              Entity("🦅", 1, -1),
              Entity("🦅", -2, -2),
              Entity("🦅", 2, -2)], "damage": 15
    }

    thunder_cloud = {"e": [Entity("⛈️", 0, 0),
                           Entity("⛈️", -1, 0),
                           Entity("⛈️", 1, 0),
                           Entity("⛈️", 0, -1)], "damage": 5}
    ufo = {"e": [Entity("🛸", 0, 0)], "damage": 100}
    helicopter = {"e": [Entity("🚁", 0, 0)], "damage": 50}
    meteor = {"e": [Entity("☄️", 0, 0)], "damage": 150}
    hot_air_balloon = {"e": [Entity("🎈", 0, 0)], "damage": 5}

    # rainbow = {"e": [Entity("🌈", 0, 0)], "shield": True}
    # star = {"e": [Entity("⭐", 0, 0)], "bonus": 10, } ? No time to implement :/

    wall_of_death = {
        "e": [Entity("# ", x, 0) for x in range(grid_width)],
        "damage": 999
    }
    def game_stopped(player_survived):
        flight_specs["flight_successful"] = player_survived
        flight_specs["flight_exp"] = int(frame * frame_delay * 5)
        flight_specs["flight_exp"] += questions_score
        return flight_specs


    def spawn_enemy(enemy, x_pos, speed):
        """This function is used to create and add a new enemy to the game."""

        ge = GameEntity(enemy["e"], x_pos, speed, enemy["damage"])
        entities.append(ge)


    def clear_terminal():
        """This function clears the terminal or console window."""

        os.system('cls' if os.name == 'nt' else 'clear')


    def on_press(key):
        """This function defines actions to take when a key is pressed."""

        # Access global variables to manipulate the plane's speed and position.
        global plane_speed
        global x, y

        # If the player has exploded, ignore the key press and exit the function.
        if player == exploded:
            return

        # When accelerating, braking, or the player is locked, handle speed adjustment.
        if accelerating or braking or lock_player_on_press:
            # Check if the current frame is even.
            if frame % 2 == 0:
                # If the UP key is pressed and speed is below 100, increase the plane_speed.
                if key == keyboard.Key.up:
                    if plane_speed < 100:
                        plane_speed += 2
                # If the DOWN key is pressed and speed is 2 or more, decrease the plane_speed.
                if key == keyboard.Key.down:
                    if plane_speed >= 2:
                        plane_speed -= 2
        else:
            # Handle alphanumeric key presses.
            try:
                print('\nalphanumeric key {0} pressed'.format(key.char))
            except AttributeError:
                # If an arrow key is pressed, adjust the player's position within grid boundaries.
                # RIGHT: Move right if not at the right boundary.
                if key == keyboard.Key.right:
                    x = min(grid_width - 2, x + 1)
                # LEFT: Move left if not at the left boundary.
                elif key == keyboard.Key.left:
                    x = max(0, x - 1)
                # UP: Move up if not at the upper boundary.
                elif key == keyboard.Key.up:
                    y = max(y_limit, y - 1)
                # DOWN: Move down if not at the bottom boundary.
                elif key == keyboard.Key.down:
                    y = min(grid_height - 1, y + 1)


    # Initialize or reset the 'smooth' variable, which is used to manage the incremental
    # movement or appearance of grid lines during acceleration or braking phases.


    def draw_grid():
        """This function is responsible for rendering the game grid, player entity,
         and other visual elements to the terminal."""

        global smooth, accelerating, elapsed_frames, questions_score

        # Initialize a 2D grid with empty spaces and place the player in it.
        x_grid = ['  '] * grid_width
        view = [x_grid.copy() for _ in range(grid_height)]
        view[y][x] = player

        # Determine the speed factor and set the default smooth increment.
        speed_factor = int(max(0, min(13, plane_speed)) / 5)
        smooth_increment = 2

        # Adjust smooth increment if plane speed is within a certain range.
        if 0 < plane_speed <= 10:
            smooth_increment = 1

        # Handle acceleration, braking, and enemy spawning.
        if accelerating or braking:
            if elapsed_frames < 150:
                elapsed_frames += 1
            else:
                spawn_enemy(wall_of_death, 0, 1)

            # Loop through each line in the grid to draw vertical lines.
            for line_y in range(grid_height):
                draw_line = False

                # Determine whether to draw a line based on frame, speed, and line position.
                # There are different conditions for various speed_factor values.
                if 0 < plane_speed <= 10:
                    draw_line = (frame % 5 == 0 and line_y % 2 == 0) or (frame % 5 != 0 and line_y % 2 == 1)
                else:
                    if speed_factor == 0:
                        draw_line = (line_y % 2 == 0)
                    elif (frame % speed_factor == 0 and line_y % 2 == 0) or (frame % speed_factor != 0 and line_y % 2 == 1):
                        draw_line = True

                # If a line should be drawn, calculate the new position and add it to the view.
                if draw_line:
                    new_line_y = (line_y + smooth) if accelerating else (line_y - smooth)
                    new_line_y = max(0, min(grid_height - 1, new_line_y))
                    if new_line_y != y:
                        view[new_line_y][x] = " |"

            # Adjust the smooth value based on acceleration, braking, and plane speed.
            if plane_speed >= 100:
                if accelerating:
                    smooth += smooth_increment
                elif braking and smooth > 0:
                    smooth -= smooth_increment

            # Reset states if a certain smooth value is reached.
            if smooth == 20:
                accelerating = False
                elapsed_frames = 0

        # Adding player and enemies to the view
        for entity in entities:
            # Iterate through each part of the entity
            for part in entity.enemy:
                # Calculate the position of each part in the grid
                e_x = entity.x_pos + part.x_off
                e_y = entity.y_pos + part.y_off
                # Check if the part is inside the grid boundaries
                if 0 <= e_x < grid_width and 0 <= e_y < grid_height and not (e_x == x and e_y == y):
                    # Update the grid cell with the entity's character
                    view[e_y][e_x] = part.e

        # Printing the view
        print(f"Speed: {plane_speed / 1.852:.1f}kn      Health: {(health / default_health) * 100:.0f}%      Time left: {max((flight_time - frame_duration) * frame_delay, 0.0):.1f}s")
        for x_row in view:
            row = (f"| {''.join(x_row)} |\n")
            sys.stdout.write(row)
        if frame_duration > 0 and frame_duration % 200 == 0:
            questions_score += questions()


    def check_collision(player_x, player_y):
        """This function checks for collisions between the player and other entities on the game grid."""

        global game, player, player_alive
        global health

        for i, entity in enumerate(entities):
            entity_x, entity_y, enemy, _, damage = entity
            # Check collision with main entity position
            if player_x == entity_x and player_y == entity_y:
                health -= damage
                if health <= 0:
                    player = exploded
                    player_alive = False
                    game = False
                entities.pop(i)
                return True, i  # Collision with entity itself

            # Check collision with parts of the entity
            for part in enemy:
                part_x = entity_x + part.x_off
                part_y = entity_y + part.y_off
                if player_x == part_x and player_y == part_y:
                    health -= damage  # Decrease health by the entity's damage
                    if health <= 0:
                        player = exploded
                        player_alive = False
                        game = False
                    return True, i  # Collision with a part of the entity

        # Check if health has depleted
        if health <= 0:
            health = 0  # Ensure health doesn't go below zero
            player = exploded
            player_alive = False
            game = False

        return False, None  # No collision


    def update_enemies():
        """This function updates the positions of enemy entities on the game grid and handles their behavior each frame."""
        global player
        global game
        check_collision(x, y)
        for i, entity in enumerate(entities):
            _, y_pos, _, speed, _ = entity
            if frame > 0 and frame % speed == 0:
                # Check if entity has reached the grid height
                if y_pos == grid_height:
                    del entities[i]
                else:
                    entity.y_pos += 1
        check_collision(x, y)


    def update_values():
        """This function manages the main game loop and updates various game values each frame."""
        # Make use of global variables to be able to modify them within the function.
        global player, game, frame, braking, lock_player_on_press, stop_entity_spawn, frame_duration

        # Main game loop: continues to execute while the 'game' variable is True.
        while game:
            # Clear the terminal/console to refresh the game display.
            clear_terminal()

            # Update the state or position of enemies in the game.
            update_enemies()

            # Condition to check if the player is not accelerating or braking.
            if not (accelerating or braking):

                # If entity spawning is enabled and the current frame is a multiple of 4:
                if not stop_entity_spawn:
                    if frame % 3 == 0:
                        # List of all possible entities to spawn.
                        all_entities = [birds, ufo, thunder_cloud, helicopter, meteor, hot_air_balloon]

                        # Spawn a random enemy entity at a random position.
                        spawn_enemy(random.choice(all_entities),
                                    random.randint(0, 19), random.randint(1, 5))

            # Condition to disable entity spawning after 200 frames.
            if frame > flight_time:
                stop_entity_spawn = True

            # If entity spawning is stopped and there are no entities left:
            if stop_entity_spawn and not entities:
                # Lock the player's position and align it before braking.
                lock_player_on_press = True
                align_player_before_braking()

            # If braking is active and the plane_speed is 0, end the game.
            if braking and plane_speed == 0:
                game = False

            # Draw the grid, update the display, and show the player’s coordinates and frame count.
            draw_grid()
            # sys.stdout.write(f"X: {x} Y: {y} \n")
            # sys.stdout.write(f"Frame: {frame} \n")
            sys.stdout.flush()

            # Pause the game for a specified delay and increment the frame count.
            time.sleep(frame_delay)
            frame += 1
            if not (accelerating or braking):
                frame_duration += 1


    def align_player_before_braking():
        """This function adjusts the player's position, aligning it towards a specific point on the grid."""
        global x, y, braking

        # Default positions
        default_x = int(grid_width / 2)
        default_y = int(grid_height - 5)

        # Move x closer to default_x
        if x < default_x:
            x += 1
        elif x > default_x:
            x -= 1

        # Move y closer to default_y
        if y < default_y:
            y += 1
        elif y > default_y:
            y -= 1

        # Check if player is aligned to default position
        if x == default_x and y == default_y:
            braking = True


    # Check if the script is being run as the main module
    try:
        # Initialize a keyboard listener to trigger the 'on_press' function when a key is pressed.
        listener = keyboard.Listener(
            on_press=on_press
        )
        # Start the keyboard listener in its thread.
        listener.start()
        # Start the game loop to update entities, game state, and manage user input.
        update_values()
        return game_stopped(player_alive)


    # Gracefully handle a keyboard interrupt (Ctrl+C) to exit the script without traceback.
    except KeyboardInterrupt:
        pass
