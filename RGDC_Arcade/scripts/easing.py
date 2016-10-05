# Import modules
import math

# Easing functions
class Easing():
    def inOutCubic(currentTime, totalTime, startValue, endValue):
        deltaValue = endValue - startValue
        currentTime = currentTime / totalTime * 2
        if currentTime < 1:
            return deltaValue / 2 * currentTime * currentTime * currentTime + startValue
        else:
            currentTime = currentTime - 2
            return deltaValue / 2 * (currentTime * currentTime * currentTime + 2) + startValue

    def outElastic(currentTime, totalTime, startValue, endValue):
        deltaValue = endValue - startValue
        if currentTime == 0:
            return startValue
        currentTime = currentTime * 1.0 / totalTime
        if currentTime == 1:
            return endValue
        period = totalTime * 0.3
        amplitude = deltaValue
        s = period / 4.0
        return amplitude * math.pow(2, -10 * currentTime) * math.sin((currentTime * totalTime - s) * (2 * math.pi) / period) + deltaValue + startValue

# Test
if __name__ == "__main__":
    duration = 1.5
    import time
    startTime = time.time()
    while True:
        timeSinceStart = time.time() - startTime
        if timeSinceStart > duration:
            break
        val1 = Easing.inOutCubic(timeSinceStart, duration, 0, 50)
        val2 = Easing.outElastic(timeSinceStart, duration, 0, 50)
        print(round(val1) * " " + "@")
        print(round(val2) * " " + "@")
        time.sleep(1.0 / 60.0)
