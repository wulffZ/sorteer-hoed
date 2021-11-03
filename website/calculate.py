class Calculate:
    def __init__(self, operator, points):
        self.operator = operator
        self.points = points

    def calculate_se(self, se):
        if self.operator == '+':
            se += int(self.points)
        else:
            if se - int(self.points) < 0:
                se = 0
            else:
                se -= int(self.points)
        return se

    def calculate_fict(self, fict):
        if self.operator == '+':
            fict += int(self.points)
        else:
            if fict - int(self.points) < 0:
                fict = 0
            else:
                fict -= int(self.points)
        return fict

    def calculate_bdam(self, bdam):
        if self.operator == '+':
            bdam += int(self.points)
        else:
            if bdam - int(self.points) < 0:
                bdam = 0
            else:
                bdam -= int(self.points)
        return bdam

    def calculate_iat(self, iat):
        if self.operator == '+':
            iat += int(self.points)
        else:
            if iat - int(self.points) < 0:
                iat = 0
            else:
                iat -= int(self.points)
        return iat
