def get_max(sequence, pulse):
    sum_up = 0
    ret = -1
    for now in sequence:
        if sum_up < 0:
            sum_up = now * pulse
        else:
            sum_up += now * pulse

        ret = max(ret, sum_up)
        pulse *= -1

    return ret

def solution(sequence):
    return max(get_max(sequence, 1), get_max(sequence, -1))