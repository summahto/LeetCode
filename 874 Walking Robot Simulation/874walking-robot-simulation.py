class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # -2 : left
        # -1 : right
        #       0 = N,  1 = E   2 = S   3 = W
        dirs = [[0, 1], [1, 0], [0, -1], [-1,0]] 

        obs_set = set()

        for o in obstacles :
            obs_set.add((o[0], o[1]))
            # obs_set.add(o)

        # print(obs_set)
        dist = 0

        x = 0
        y = 0
        curr = 0 # 0 -> North
        for cmd in commands:

            if cmd == -1:
                # turn right
                curr = (curr + 1) %4

            elif cmd == -2:
                # turn left
                curr = (curr - 1) % 4

            else:
                while cmd > 0 and (x+ dirs[curr][0], y+dirs[curr][1]) not in obs_set:
                    x += dirs[curr][0]
                    y += dirs[curr][1]

                    cmd -= 1

            # prev = curr

            dist = max(dist, x**2 + y**2)
            # print("x = ", x, "y = ", y, curr)

        return dist

