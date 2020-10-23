def on_button_pressed_a():
    global poz
    if poz > 0:
        led.unplot(poz, 4)
        poz += -1
        led.plot(poz, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global poz
    if poz < 4:
        led.unplot(poz, 4)
        poz += 1
        led.plot(poz, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

empty = 0
poz = 0
poz = 2
score = 0
led.set_brightness(100)
led.plot(poz, 4)

def on_forever():
    global empty, score, poz
    empty = randint(0, 4)
    for a in range(5):
        for ind in range(5):
            if empty != ind:
                led.plot(ind, a)
        basic.pause(300 - score)
        for ind2 in range(5):
            if empty != ind2:
                led.unplot(ind2, a)
        if a == 4 and poz != empty:
            basic.show_icon(IconNames.NO)
            basic.pause(2000)
            basic.clear_screen()
            basic.show_number(score)
            score = 0
            poz = 2
            led.plot(poz, 4)
    score += 1
basic.forever(on_forever)
