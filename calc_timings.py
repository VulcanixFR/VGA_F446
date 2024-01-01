# http://tinyvga.com/vga-timing/800x600@60Hz
# https://www.artekit.eu/vga-output-using-a-36-pin-stm32/

max_sysclock = 180e6

# # General timing
# screen_refresh_rate = 60        # Hz
# vertical_refresh    = 37.87e3   # Hz
# px_refresh          = 40e6      # Hz

# # Horizontal timing
# h_visible_area      = 800       # px
# h_front_porch       = 40        # px
# h_sync_pulse        = 128       # px
# h_back_porch        = 88        # px
# h_whole_line        = 1056      # px

# # Vertical timing
# v_visible_area      = 600       # lines
# v_front_porch       = 1         # lines
# v_sync_pulse        = 4         # lines
# v_back_porch        = 23        # lines
# v_whole_frame       = 628       # lines

# General timing
screen_refresh_rate = 60        # Hz
vertical_refresh    = 31.47e3   # Hz
px_refresh          = 25.175e6  # Hz

# Horizontal timing
h_visible_area      = 640       # px
h_front_porch       = 16        # px
h_sync_pulse        = 96        # px
h_back_porch        = 48        # px
h_whole_line        = 800       # px

# Vertical timing
v_visible_area      = 480       # lines
v_front_porch       = 10        # lines
v_sync_pulse        = 2         # lines
v_back_porch        = 33        # lines
v_whole_frame       = 525       # lines

### TRUC DE TEST RAPIDE AVEC DES LEDS
# max_sysclock        = 1e6
# px_refresh          = 100        
# h_sync_pulse        = 40        
# h_back_porch        = 1  
# h_whole_line        = 100        
# v_sync_pulse        = 20
# v_back_porch        = 1
# v_whole_frame       = 100        

"""
Configurations des Timers
"""

k = (max_sysclock // px_refresh)
SYSCLOCK = k * px_refresh       

# Les timers génèrent des PWM en tant que signaux de synchro

TIM2_PSC = k - 1                # (SYSCLOCK / px_refresh) - 1
TIM2_COUNT = h_whole_line - 1      
TIM2_CH1_COUNT = h_sync_pulse + h_back_porch - 1 
TIM2_CH2_COUNT = h_sync_pulse - 1

# On utilise le TIM2 comme clock pour le TIM5
# A chaque interruption de TIM2, TIM5 reçois 1 signal de clock

TIM5_PSC = 0
TIM5_COUNT = v_whole_frame - 1
TIM5_CH1_COUNT = v_sync_pulse - 1
TIM5_CH2_COUNT = v_sync_pulse + v_back_porch -1


"""
Affichage
"""

print("Sysclock =", SYSCLOCK)

print("TIM2 :")
print(" - PSC              =", TIM2_PSC)
print(" - COUNT            =", TIM2_COUNT)
print(" - CH1 (back porch) =", TIM2_CH1_COUNT)
print(" - CH2 (HSync)      =", TIM2_CH2_COUNT)

print("TIM5 :")
print(" - PSC              =", TIM5_PSC)
print(" - COUNT            =", TIM5_COUNT)
print(" - CH1 (HSync)      =", TIM5_CH1_COUNT)
print(" - CH2 (back porch) =", TIM5_CH2_COUNT)