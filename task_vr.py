import math
from collections import Counter

def classify(immersion, sees_real):
    return "AR" if immersion and not sees_real else ("VR" if not immersion and sees_real else "MR")

def in_fov(angle, fov):
    return True if abs(angle) <= fov/2 else False

def distance_3d(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def motion_to_photon(ms):
    return "комфортно" if ms <= 20 else "риск укачивания"

def to_radians(angle):
    return math.radians(angle)

def normalize(vector:tuple):
    return vector if math.sqrt(sum(list(map(lambda x: x ** 2, vector)))) == 0 else tuple(map(lambda x: x/math.sqrt(sum(list(map(lambda y: y ** 2, vector)))), vector))

def fps_ok(frames, seconds, target=90):
    return f"FPS: {frames / seconds}, комфортно для VR: True" if frames/seconds >= target else f"FPS: {frames/seconds}, комфортно для VR: False"

def affordable(budget):
    return [x for x,price in { "Google Cardboard VR":500, "Meta Quest 3S": 29350, "PlayStation VR2": 33550, "Meta Quest 3": 50350, "Pimax Crystal Light": 75600, "Bigscreen Beyond 2": 85700, "Steam Frame": 89050, "Samsung Galaxy XR": 151300, "Magic Leap 2": 277450, "Apple Vision Pro (M5)": 294250, "Somnium VR1": 361500}.items() if price <= budget]

def counter_list(words_list: list):
    return dict(Counter(words_list))

def most_common(words_list:list):
    return "list is empty" if not words_list else f"Чаще всего {list(dict(sorted(counter_list(words_list).items(), key=lambda x: x[1], reverse=True)).keys())[0]}"

def lerp(a, b, t):
    return f"t={t}: {a+(b-a)*t}"

def can_reach(hand, obj, reach=0.3):
    return True if distance_3d(hand, obj) <= reach else False

def vr_filter(vr_list_dict : list[dict]):
    return f"VR устройства: {[info["name"] for info in vr_list_dict if info["type"] in "VR"]}"

def total_latency(network, render, display):
    return f"Суммарная задержка: {network+render+display} ms\nПригодно для VR: {(network+render+display) <= 20}"

def move(dt=1/90, speed=2, frames=3, pos=0):
    return '\n'.join([f"Кадр {x}: позиция = {(pos:=pos+(speed*dt)):.4f}" for x in range(1, frames+1)])

print(f"Фукнция classify(True, True): {classify(True, True)}\nФункция in_fov(55, 110): {in_fov(55, 110)}\nФункция distance_3d((1,1,1), (5,5,5)): {distance_3d((1,1,1), (5,5,5))}\nФункция motion_to_photon(40): {motion_to_photon(40)}\nФункция to_radians(180): {to_radians(180)}\nФункция normalize((5, 4, 0)): {normalize((5,4,0))}\nФукнция fps_ok(600, 20): {fps_ok(600, 20)}\nФункция affordable(100000): {affordable(100000)}\nФункция counter_list([игры, медицина, игры, образование, медицина, игры]): {counter_list(["игры", "медицина", "игры", "образование", "медицина", "игры"])}\nФункция most_common([игры, медицина, игры, образование, медицина, игры, медицина, медицина]): {most_common(["игры", "медицина", "игры", "образование", "медицина", "игры", "медицина", "медицина"])}\nФункция lerp(0, 10, 0.5): {lerp(0, 10, 0.5)}\nФункция can_reach((0.1, 0.1, 0.1), (0.2, 0.2, 0.2)): {can_reach((0.1, 0.1, 0.1), (0.2, 0.2, 0.2))}\nФункция vr_filter([(name: thing, type: VR), (name: not_thing, type: AR]): {vr_filter([{"name": "thing", "type": "VR"}, {"name": "not_thing", "type": "AR"}])}\nФункция total_latency(5,8,10): {total_latency(5,8,10)}\nФункция move(): {move()}")