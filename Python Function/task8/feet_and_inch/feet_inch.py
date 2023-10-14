class fet:
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch

    def feet_inch(self,obj):
        feet1=self.feet+obj.feet
        inch1=self.inch+obj.inch

        while inch1 > 12:
            feet1 = feet1 +1
            inch1=inch1 - 11
        
        return feet1,inch1