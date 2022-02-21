
import sys
import time

Mi = 1024 * 1024

def get_available():
    lines = []
    with open('/proc/meminfo') as f:
        lines = f.readlines()
    #
    for line in lines:
        if line.startswith('MemAvailable'):
            return int(line.split()[1]) * 1024
    #
    raise KeyError('/proc/meminfo does not contain MemAvailable line')

def main(target_size):
    blocks = []
    #
    to_reserve = get_available() - target_size
    print('Will reserve:', to_reserve // Mi, 'MiB', file=sys.stderr)
    #
    urandom_count = to_reserve // (16 * Mi)
    #
    print('Random:', urandom_count, 'MiB', file=sys.stderr)
    with open('/dev/urandom', 'rb') as f:
        for _ in range(urandom_count):
            blocks.append(bytearray(f.read(Mi)))
    #
    print('Copying all that 14 times', file=sys.stderr)
    #
    for _ in range(14 * urandom_count):
        b2 = blocks[-1].copy()
        blocks.append(b2)
        # for i in range(len(b2)):
        #     b2[i] = (b2[i] + 1) & 0xFF
    #
    time.sleep(1)
    print('Copying a few more MiB', file=sys.stderr)
    #
    while get_available() - target_size > Mi:
        b2 = blocks[-1].copy()
        blocks.append(b2)
    #
    time.sleep(1)
    print('Done, undershoot by', (get_available() - target_size) // 1024, 'KiB', file=sys.stderr)
    #
    print('OK', flush=True) # at stdout to signal to proceed
    #
    try:
        while True:
            time.sleep(1000000)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    assert len(sys.argv) == 2
    target_size = int(sys.argv[1]) * 1024 * 1024 * 1024
    main(target_size=target_size)
