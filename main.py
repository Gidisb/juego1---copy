def on_b_pressed():
    global projectile
    if direccion == 0 and nivel == 2:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . 2 2 1 1 1 1 2 . . 
                            . . . . 2 2 3 3 1 1 1 1 1 1 . . 
                            . . 3 3 3 3 1 1 1 1 1 1 1 1 . . 
                            . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                            . . 3 3 2 2 3 1 1 1 1 1 1 1 . . 
                            . . . . . . 2 2 3 1 1 1 1 2 . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Bueno,
            200,
            0)
    if direccion == 1 and nivel == 2:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . 2 2 1 1 1 1 2 . . 
                            . . . . 2 2 3 3 1 1 1 1 1 1 . . 
                            . . 3 3 3 3 1 1 1 1 1 1 1 1 . . 
                            . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                            . . 3 3 2 2 3 1 1 1 1 1 1 1 . . 
                            . . . . . . 2 2 3 1 1 1 1 2 . . 
                            . . . . . . . . . 2 2 2 2 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Bueno,
            -200,
            0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def nivel_2():
    global nivel
    tesoro.destroy()
    tesoro1.destroy()
    tesoro2.destroy()
    tesoro3.destroy()
    tiles.set_tilemap(tilemap("""
        nivel2
    """))
    color_fondo(randint(1, 15))
    Bueno.ay = 200
    Malo.set_position(1024, 8)
    nivel = 2
    info.start_countdown(10)

def on_countdown_end():
    info.start_countdown(10)
    color_fondo(randint(1, 15))
info.on_countdown_end(on_countdown_end)

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location,
        img("""
            . b b b b b b b b b b b b b b . 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 4 b 
                    b e 4 4 4 4 4 4 4 4 4 4 4 4 e b 
                    b e e 4 4 4 4 4 4 4 4 4 4 e e b 
                    b b b b b b b d d b b b b b b b 
                    . b b b b b b c c b b b b b b . 
                    b c c c c c b c c b c c c c c b 
                    b c c c c c c b b c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b c c c c c c c c c c c c c c b 
                    b b b b b b b b b b b b b b b b 
                    b e e e e e e e e e e e e e e b 
                    b e e e e e e e e e e e e e e b 
                    b c e e e e e e e e e e e e c b 
                    b b b b b b b b b b b b b b b b 
                    . b b . . . . . . . . . . b b .
        """))
    info.change_score_by(1)
    music.ba_ding.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2, sprites.dungeon.hazard_lava1)
    game.over(False, effects.melt)
    music.ba_ding.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava1,
    on_overlap_tile2)

def on_on_overlap(sprite3, otherSprite):
    game.over(False, effects.dissolve)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_overlap_tile3(sprite4, location3):
    tiles.set_tile_at(location3, sprites.dungeon.hazard_water)
    game.over(False, effects.bubbles)
    music.ba_ding.play()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_water,
    on_overlap_tile3)

def on_on_overlap2(sprite5, otherSprite2):
    if Bueno.overlaps_with(tesoro):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro.destroy()
    if Bueno.overlaps_with(tesoro1):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro1.destroy()
    if Bueno.overlaps_with(tesoro2):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro2.destroy()
    if Bueno.overlaps_with(tesoro2):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro2.destroy()
    if Bueno.overlaps_with(tesoro3):
        info.change_score_by(1)
        music.ba_ding.play()
        tesoro3.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def color_fondo(codigo_color: number):
    if codigo_color == 1:
        scene.set_background_color(0)
    if codigo_color == 2:
        scene.set_background_color(1)
    if codigo_color == 3:
        scene.set_background_color(2)
    if codigo_color == 4:
        scene.set_background_color(3)
    if codigo_color == 5:
        scene.set_background_color(4)
    if codigo_color == 6:
        scene.set_background_color(5)
    if codigo_color == 7:
        scene.set_background_color(6)
    if codigo_color == 8:
        scene.set_background_color(13)
    if codigo_color == 9:
        scene.set_background_color(12)
    if codigo_color == 10:
        scene.set_background_color(11)
    if codigo_color == 11:
        scene.set_background_color(10)
    if codigo_color == 12:
        scene.set_background_color(12)
    if codigo_color == 13:
        scene.set_background_color(13)
    if codigo_color == 14:
        scene.set_background_color(14)
    if codigo_color == 15:
        scene.set_background_color(15)

def on_on_overlap3(sprite6, otherSprite3):
    global Malo
    Malo.destroy()
    Malo = sprites.create(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
                    2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
                    2 5 5 f 5 5 2 2 2 5 5 f 5 5 2 2 
                    2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
                    2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        SpriteKind.enemy)
    Malo.set_position(1024, 8)
    Malo.follow(Bueno, 25)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap3)

projectile: Sprite = None
direccion = 0
nivel = 0
Malo: Sprite = None
Bueno: Sprite = None
tesoro3: Sprite = None
tesoro2: Sprite = None
tesoro1: Sprite = None
tesoro: Sprite = None
game.splash("COME-COME", "AUTOR Giovanni")
game.set_dialog_text_color(9)
game.set_dialog_frame(img("""
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
"""))
game.set_dialog_cursor(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . 6 6 6 5 5 6 6 6 . . . . 
        . . . 7 7 7 7 6 6 6 6 6 6 . . . 
        . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
        . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
        . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
        . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
        . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
        . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
        . . . 6 8 8 8 8 8 8 8 8 6 . . . 
        . . . . 6 6 8 8 8 8 6 6 . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . . . . . . . . . . . . .
"""))
game.show_long_text("Tienes que recoger los 4 tesoros e impedir que el malo te detenga",
    DialogLayout.CENTER)
info.set_score(0)
tiles.set_tilemap(tilemap("""
    nivel1
"""))
tesoro = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . 6 6 6 5 5 6 6 6 . . . . 
            . . . 7 7 7 7 6 6 6 6 6 6 . . . 
            . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
            . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
            . . . . 6 6 8 8 8 8 6 6 . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro.set_position(120, 21)
tesoro1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . 6 6 6 5 5 6 6 6 . . . . 
            . . . 7 7 7 7 6 6 6 6 6 6 . . . 
            . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
            . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
            . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
            . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
            . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
            . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
            . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
            . . . 6 8 8 8 8 8 8 8 8 6 . . . 
            . . . . 6 6 8 8 8 8 6 6 . . . . 
            . . . . . . 6 6 6 6 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro1.set_position(26, 136)
tesoro2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro2.set_position(168, 184)
tesoro3 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . 4 4 4 5 5 4 4 4 . . . . 
            . . . 3 3 3 3 4 4 4 4 4 4 . . . 
            . . 4 3 3 3 3 2 2 2 1 1 4 4 . . 
            . . 3 3 3 3 3 2 2 2 1 1 5 4 . . 
            . 4 3 3 3 3 2 2 2 2 2 5 5 4 4 . 
            . 4 3 3 3 2 2 2 4 4 4 4 5 4 4 . 
            . 4 4 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . 4 2 3 3 2 2 4 4 4 4 4 4 4 4 . 
            . . 4 2 3 3 2 4 4 4 4 4 2 4 . . 
            . . 4 2 2 3 2 2 4 4 4 2 4 4 . . 
            . . . 4 2 2 2 2 2 2 2 2 4 . . . 
            . . . . 4 4 2 2 2 2 4 4 . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.food)
tesoro3.set_position(232, 56)
nivel1 = sprites.create(img("""
        6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 6 6 9 9 c c 6 9 9 9 6 6 9 6 
            6 6 6 9 9 9 9 c 6 6 9 9 9 6 6 6 
            6 6 9 9 9 9 9 9 6 6 9 9 9 9 6 6 
            6 9 9 9 6 6 6 6 9 6 9 9 c 9 9 6 
            6 9 c 6 6 6 9 9 9 6 9 c c c 9 6 
            6 9 c c c 9 6 9 9 9 6 6 6 c 9 6 
            6 9 9 c 9 9 6 9 6 6 6 6 9 9 9 6 
            6 6 9 9 9 9 6 6 9 9 9 9 9 9 6 6 
            6 6 6 9 9 9 6 6 c 9 9 9 9 6 6 6 
            6 9 6 6 9 9 9 6 c c 9 9 6 6 9 6 
            6 9 9 6 6 9 9 c c 9 9 6 6 9 9 6 
            6 9 9 9 6 6 9 9 9 9 6 6 9 9 9 6 
            6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6
    """),
    SpriteKind.food)
nivel1.set_position(88, 200)
Bueno = sprites.create(img("""
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 5 5 5 5 5 8 8 5 5 5 5 5 8 8 
            8 8 5 5 5 5 5 8 8 5 5 5 5 5 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 5 5 f f f 8 8 5 5 f f f 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 6 6 6 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """),
    SpriteKind.player)
Bueno.set_position(8, 104)
Malo = sprites.create(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
            2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
            2 5 5 f 5 5 2 2 2 5 5 f 5 5 2 2 
            2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
            2 5 5 5 5 5 2 2 2 5 5 5 5 5 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
            2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
            2 2 2 2 2 2 5 5 5 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    """),
    SpriteKind.enemy)
Malo.set_position(150, 110)
Malo.follow(Bueno, 25)
controller.move_sprite(Bueno, 100, 100)
scene.camera_follow_sprite(Bueno)
nivel = 1
direccion = 0
game.set_dialog_cursor(img("""
    . . . . . . . . . . . . . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . 6 6 6 5 5 6 6 6 . . . . 
        . . . 7 7 7 7 6 6 6 6 6 6 . . . 
        . . 6 7 7 7 7 8 8 8 1 1 6 6 . . 
        . . 7 7 7 7 7 8 8 8 1 1 5 6 . . 
        . 6 7 7 7 7 8 8 8 8 8 5 5 6 6 . 
        . 6 7 7 7 8 8 8 6 6 6 6 5 6 6 . 
        . 6 6 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . 6 8 7 7 8 8 6 6 6 6 6 6 6 6 . 
        . . 6 8 7 7 8 6 6 6 6 6 8 6 . . 
        . . 6 8 8 7 8 8 6 6 6 8 6 6 . . 
        . . . 6 8 8 8 8 8 8 8 8 6 . . . 
        . . . . 6 6 8 8 8 8 6 6 . . . . 
        . . . . . . 6 6 6 6 . . . . . . 
        . . . . . . . . . . . . . . . .
"""))

def on_forever():
    global direccion
    if info.score() == 4 and Bueno.overlaps_with(nivel1):
        info.change_score_by(10)
        nivel1.destroy()
        music.magic_wand.play()
        nivel_2()
    if info.score() == 27:
        game.over(True, effects.confetti)
        music.magic_wand.play()
    if controller.right.is_pressed() and nivel == 2:
        direccion = 0
    if controller.left.is_pressed() and nivel == 2:
        direccion = 1
forever(on_forever)
