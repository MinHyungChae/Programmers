def solution(bridge_length, weight, truck_weights):
    on_bridge = [0 for i in range(bridge_length)]
    answer = 0
    
    while on_bridge:
        print(f'on_bridge: {on_bridge}')
        on_bridge.pop(0)
        answer += 1
        print(f'one: {on_bridge}')
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
                print(f'add: {on_bridge}')
            else:
                on_bridge.append(0)
                print(f'pass: {on_bridge}')
        print(f'total: {on_bridge}')
    return answer